import argparse
import os
from pathlib import Path
from .settings import Settings
from .compare import extract_faces, group_faces

parser = argparse.ArgumentParser(
    prog="FaceExtractor", description="Extracts faces from images in provided source directory"
)
parser.add_argument("source_dir", type=Path, help="Directory containing source images")
parser.add_argument(
    "--model",
    dest="model",
    choices=["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"],
    default="Facenet512",
    type=str,
    help="Model to use (default: Facenet512)",
)
parser.add_argument(
    "--size",
    dest="size",
    default=224,
    type=int,
    help="Resolution of saved faces (default: 224)",
)
args = parser.parse_args()


SOURCE_DIR = args.source_dir
TARGET_DIR = SOURCE_DIR.joinpath("faces")
DB_PATH = TARGET_DIR.joinpath("db")
SETTINGS = Settings(
    **{
        "source_dir": SOURCE_DIR,
        "target_dir": TARGET_DIR,
        "db_path": DB_PATH,
        "supported_extensions": [".jpg", ".jpeg", ".png"],
        "size": args.size,
    }
)


if SOURCE_DIR.exists():
    os.makedirs(TARGET_DIR, exist_ok=True)
    extract_faces(SETTINGS)
    group_faces(SETTINGS)
else:
    print(f"{args.source_dir} does not exist")
