# video-maker

This repository contains miscellaneous scripts to generate videos.

## Scripts

### count_progress.py

A script that generates a countdown progress video. The video displays:
- A countdown number (1-4) in the center
- A progress bar on the left side that fills from bottom to top
- The progress bar color transitions from green to red as it fills
- Video resolution: 1080x1920 (portrait orientation)
- Duration: 4 seconds at 30 fps

#### Requirements

Before running the script, install the required dependencies using the requirements file:

```bash
pip install -r requirements.txt
```

**Note:** The script uses the Arial font. PIL/Pillow's `ImageFont.truetype()` will automatically search system font directories (e.g., `/usr/share/fonts/` on Linux, `C:\Windows\Fonts\` on Windows) if the font file is not found in the current directory. As long as Arial is installed on your system, the script will work without needing the font file in the same directory.

#### Usage

1. Ensure you have Python 3 installed
2. Install dependencies using the requirements file:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure Arial font is installed on your system (most systems have it by default)
4. Run the script:
   ```bash
   python count_progress.py
   ```

The script will generate `progress_video.mp4` in the same directory when complete.
