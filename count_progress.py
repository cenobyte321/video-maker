from PIL import Image, ImageDraw, ImageFont
import numpy as np
from moviepy import ImageSequenceClip

# Video settings
width, height = 1080, 1920
duration  = 4
fps = 30
frames = []

# Load a default font
font = ImageFont.truetype("arial.ttf", 750)

total_frames = duration * fps

for i in range(total_frames):
    t = i / fps
    progress = min(max(t / duration, 0), 1)

    # Create background
    img = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Progress bar color (green -> red)
    r = int(255 * progress)
    g = int(255 * (1 - progress))
    bar_color = (r, g, 0)

    bar_width = int(width * 0.15)
    bar_height = int(height * progress)

    # Draw bar from bottom to top
    bar_top = height - bar_height
    draw.rectangle([0, bar_top, bar_width, height], fill=bar_color)

    # Determine number
    number = str(int(min(t // 1 + 1, 4)))

    # Draw number
    bbox = draw.textbbox((0, 0), number, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    draw.text((width * 0.55, height / 2 - text_h / 2), number, font=font, fill=(255, 255, 255))

    frames.append(np.array(img))

# Create video
clip = ImageSequenceClip(frames, fps=fps)
clip.write_videofile("progress_video.mp4", codec="libx264", audio=False)

print("Video created successfully!")