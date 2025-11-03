# video-maker
Miscellaneous scripts to generate and manipulate videos.

## Overview
This repository contains a collection of Python scripts for common video processing tasks including creating videos from images, adding text overlays, concatenating videos, extracting frames, and other utility operations.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Scripts

### 1. images_to_video.py
Create a video from a sequence of images.

**Usage:**
```bash
python scripts/images_to_video.py <image_folder> <output_file> [options]
```

**Example:**
```bash
python scripts/images_to_video.py ./images output.mp4 --fps 30
```

**Options:**
- `--fps`: Frames per second (default: 30)
- `--codec`: Video codec (default: mp4v)

### 2. add_text_overlay.py
Add text overlay to an existing video.

**Usage:**
```bash
python scripts/add_text_overlay.py <input_file> <output_file> <text> [options]
```

**Example:**
```bash
python scripts/add_text_overlay.py input.mp4 output.mp4 "Hello World" --position bottom-center --font-scale 1.5
```

**Options:**
- `--position`: Text position (choices: top-left, top-center, top-right, center, bottom-left, bottom-center, bottom-right)
- `--font-scale`: Font size scale (default: 1.0)
- `--color`: Text color in BGR format (default: 255,255,255)
- `--thickness`: Text thickness (default: 2)

### 3. concatenate_videos.py
Concatenate multiple videos into one.

**Usage:**
```bash
python scripts/concatenate_videos.py <input_files...> -o <output_file> [options]
```

**Example:**
```bash
python scripts/concatenate_videos.py video1.mp4 video2.mp4 video3.mp4 -o combined.mp4
```

**Options:**
- `-o, --output`: Output video file path (required)
- `--method`: Concatenation method (choices: compose, chain; default: compose)

### 4. extract_frames.py
Extract frames from a video file.

**Usage:**
```bash
python scripts/extract_frames.py <input_file> <output_folder> [options]
```

**Example:**
```bash
python scripts/extract_frames.py input.mp4 ./frames --interval 10 --format jpg
```

**Options:**
- `--interval`: Extract every nth frame (default: 1 for all frames)
- `--format`: Output image format (choices: jpg, png, bmp; default: jpg)

### 5. video_utils.py
Utility script for common video operations.

#### Get Video Information
```bash
python scripts/video_utils.py info <video_file>
```

**Example:**
```bash
python scripts/video_utils.py info input.mp4
```

#### Resize Video
```bash
python scripts/video_utils.py resize <input_file> <output_file> [options]
```

**Example:**
```bash
# Resize to specific width (maintains aspect ratio)
python scripts/video_utils.py resize input.mp4 output.mp4 --width 1280

# Resize to specific dimensions
python scripts/video_utils.py resize input.mp4 output.mp4 --width 1920 --height 1080

# Scale by factor
python scripts/video_utils.py resize input.mp4 output.mp4 --scale 0.5
```

**Options:**
- `--width`: Target width
- `--height`: Target height
- `--scale`: Scale factor (e.g., 0.5 for half size)

## Common Workflows

### Create a slideshow from images
```bash
# Put your images in a folder (e.g., ./images)
# Images should be named in order (e.g., img001.jpg, img002.jpg, etc.)
python scripts/images_to_video.py ./images slideshow.mp4 --fps 2
```

### Add a watermark/title to a video
```bash
python scripts/add_text_overlay.py input.mp4 watermarked.mp4 "© 2025" --position bottom-right --font-scale 0.7
```

### Combine multiple video clips
```bash
python scripts/concatenate_videos.py intro.mp4 main.mp4 outro.mp4 -o final.mp4
```

### Extract key frames for analysis
```bash
# Extract every 30th frame
python scripts/extract_frames.py input.mp4 ./frames --interval 30
```

## Dependencies
- **opencv-python**: Video and image processing
- **moviepy**: Video editing and manipulation
- **numpy**: Numerical operations
- **Pillow**: Image processing support

## License
This project is open source and available for educational and personal use.
