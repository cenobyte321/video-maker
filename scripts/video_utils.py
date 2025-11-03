#!/usr/bin/env python3
"""
Utility script for common video operations.
"""
import argparse
import cv2
from moviepy.editor import VideoFileClip


def get_video_info(video_file):
    """Get detailed information about a video file."""
    cap = cv2.VideoCapture(video_file)
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = frame_count / fps if fps > 0 else 0
    
    cap.release()
    
    # Try to get audio info using moviepy
    try:
        clip = VideoFileClip(video_file)
        has_audio = clip.audio is not None
        audio_fps = clip.audio.fps if has_audio else None
        clip.close()
    except:
        has_audio = False
        audio_fps = None
    
    print(f"\nVideo Information: {video_file}")
    print(f"=" * 50)
    print(f"Resolution: {width}x{height}")
    print(f"FPS: {fps:.2f}")
    print(f"Frame Count: {frame_count}")
    print(f"Duration: {duration:.2f} seconds ({duration/60:.2f} minutes)")
    print(f"Has Audio: {has_audio}")
    if audio_fps:
        print(f"Audio Sample Rate: {audio_fps} Hz")
    print(f"=" * 50)


def resize_video(input_file, output_file, width=None, height=None, scale=None):
    """
    Resize a video.
    
    Args:
        input_file: Input video file
        output_file: Output video file
        width: Target width (if height is None, maintains aspect ratio)
        height: Target height (if width is None, maintains aspect ratio)
        scale: Scale factor (e.g., 0.5 for half size)
    """
    cap = cv2.VideoCapture(input_file)
    
    # Get original properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    orig_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    orig_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Calculate new dimensions
    if scale:
        new_width = int(orig_width * scale)
        new_height = int(orig_height * scale)
    elif width and height:
        new_width = width
        new_height = height
    elif width:
        new_width = width
        new_height = int(orig_height * (width / orig_width))
    elif height:
        new_height = height
        new_width = int(orig_width * (height / orig_height))
    else:
        raise ValueError("Must specify width, height, or scale")
    
    print(f"Resizing from {orig_width}x{orig_height} to {new_width}x{new_height}")
    
    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (new_width, new_height))
    
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Resize frame
        resized_frame = cv2.resize(frame, (new_width, new_height))
        out.write(resized_frame)
        
        frame_count += 1
        if frame_count % 30 == 0:
            print(f"Processing: {frame_count}/{total_frames} frames", end='\r')
    
    cap.release()
    out.release()
    print(f"\nVideo resized successfully: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Utility for common video operations'
    )
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Get video information')
    info_parser.add_argument('video_file', help='Video file path')
    
    # Resize command
    resize_parser = subparsers.add_parser('resize', help='Resize a video')
    resize_parser.add_argument('input_file', help='Input video file')
    resize_parser.add_argument('output_file', help='Output video file')
    resize_parser.add_argument('--width', type=int, help='Target width')
    resize_parser.add_argument('--height', type=int, help='Target height')
    resize_parser.add_argument('--scale', type=float, help='Scale factor (e.g., 0.5)')
    
    args = parser.parse_args()
    
    if args.command == 'info':
        get_video_info(args.video_file)
    elif args.command == 'resize':
        resize_video(args.input_file, args.output_file, 
                    args.width, args.height, args.scale)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
