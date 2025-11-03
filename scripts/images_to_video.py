#!/usr/bin/env python3
"""
Script to create a video from a sequence of images.
"""
import argparse
import cv2
import os
from pathlib import Path


def images_to_video(image_folder, output_file, fps=30, codec='mp4v'):
    """
    Create a video from images in a folder.
    
    Args:
        image_folder: Path to folder containing images
        output_file: Output video file path
        fps: Frames per second (default: 30)
        codec: Video codec (default: 'mp4v')
    """
    images = sorted([img for img in os.listdir(image_folder) 
                     if img.endswith(('.png', '.jpg', '.jpeg', '.bmp'))])
    
    if not images:
        print("No images found in the specified folder.")
        return
    
    # Read the first image to get dimensions
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, _ = frame.shape
    
    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*codec)
    video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
    
    # Write all images to video
    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        video.write(frame)
        print(f"Added frame: {image}")
    
    video.release()
    print(f"\nVideo created successfully: {output_file}")
    print(f"Total frames: {len(images)}, FPS: {fps}, Duration: {len(images)/fps:.2f}s")


def main():
    parser = argparse.ArgumentParser(
        description='Create a video from a sequence of images'
    )
    parser.add_argument(
        'image_folder',
        help='Path to folder containing images'
    )
    parser.add_argument(
        'output_file',
        help='Output video file path (e.g., output.mp4)'
    )
    parser.add_argument(
        '--fps',
        type=int,
        default=30,
        help='Frames per second (default: 30)'
    )
    parser.add_argument(
        '--codec',
        default='mp4v',
        help='Video codec (default: mp4v)'
    )
    
    args = parser.parse_args()
    
    images_to_video(args.image_folder, args.output_file, args.fps, args.codec)


if __name__ == '__main__':
    main()
