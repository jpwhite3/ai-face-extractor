from deepface import DeepFace
import cv2
import os
from .settings import Settings


def extract_faces(settings: Settings):
    for source_image_path in settings.source_dir.glob("**/*"):
        # Ignore images stored in target_dir
        if source_image_path.parent == settings.target_dir:
            continue

        if source_image_path.suffix.lower() in settings.supported_extensions:
            print(f"Extracting faces in {source_image_path}")
            # detect faces using DeepFace
            try:
                detected_faces = DeepFace.extract_faces(
                    str(source_image_path),
                    target_size=(settings.size, settings.size),
                    detector_backend="retinaface",
                    grayscale=False,
                )
            except ValueError:
                print(f"Could not find face in {source_image_path}")
                continue

            # save the detected faces in the target folder
            for counter, detected_face in enumerate(detected_faces):
                # These 2 lines somehow magically convert the negative image to color
                detected_face = detected_face["face"] * 255
                detected_face = detected_face[:, :, ::-1]

                target_image_name = f"{source_image_path.stem}-face{counter}{source_image_path.suffix}"
                new_image_path = settings.target_dir.joinpath(target_image_name)
                cv2.imwrite(str(new_image_path), detected_face)


def group_faces(settings: Settings):
    detected_face_image_paths = [
        i for i in settings.target_dir.glob("**/*") if i.suffix.lower() in settings.supported_extensions
    ]
    for i, detected_face_image_path in enumerate(detected_face_image_paths):
        if detected_face_image_path.parent.name.startswith("group_"):
            continue
        if detected_face_image_path.exists():
            group_dir_path = settings.target_dir.joinpath(f"group{i}")
            os.makedirs(group_dir_path, exist_ok=True)
            for img_path in detected_face_image_paths:
                if img_path.exists() and detected_face_image_path != img_path:
                    try:
                        result = DeepFace.verify(img1_path=str(detected_face_image_path), img2_path=str(img_path))
                        if result.get("verified", False):
                            print("Grouping matched face")
                            img_path.rename(group_dir_path.joinpath(img_path.name))
                    except ValueError:
                        continue
            detected_face_image_path.rename(group_dir_path.joinpath(detected_face_image_path.name))
