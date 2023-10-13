# ai-face-extractor
A command line program that detects faces in photos and makes thumbnail groups of each unique face. This can be helpful when gathering photos for Stable Diffusion model training.

# Setup

Install dependencies
```bash
pipenv install
```

# Run

```bash
pipenv run python -m extract_faces /path/to/photos
```

This will create a `faces` sub-directory in the provided photos directory, which will have `group#` sub-directories within it. Each `group#` directory will contain thumbnails of the extracted faces, grouped by similarity.

> Known Issue: Grouped photos are a little hit-and-miss at the moment. In a future version, furture similarify measurements will be taken into account to group photos more accuratly.

# Help
```bash
usage: FaceExtractor [-h] [--model {VGG-Face,Facenet,Facenet512,OpenFace,DeepFace,DeepID,ArcFace,Dlib,SFace}] [--size SIZE] source_dir

Extracts faces from images in provided source directory

positional arguments:
  source_dir            Directory containing source images

options:
  -h, --help            show this help message and exit
  --model {VGG-Face,Facenet,Facenet512,OpenFace,DeepFace,DeepID,ArcFace,Dlib,SFace}
                        Model to use (default: Facenet512)
  --size SIZE           Resolution of saved faces (default: 224)
```
