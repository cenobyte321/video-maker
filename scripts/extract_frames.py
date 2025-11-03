#!/usr/bin/env python3
"""
Script to extract frames from a video.
"""
import argparse
import cv2
import os


def extract_frames(input_file, output_folder, interval=1, format='jpg'):
    """
    Extract frames from a video.
    
    Args:
        input_file: Input video file path
        output_folder: Output folder for extracted frames
        interval: Extract every nth frame (default: 1 for all frames)
        format: Output image format (default: jpg)
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the video
    cap = cv2.VideoCapture(input_file)
    
    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if fps <= 0:
        print("Error: Invalid FPS value. Video file may be corrupted.")
        cap.release()
        return
    
    print(f"Video FPS: {fps}")
    print(f"Total frames: {total_frames}")
    print(f"Extracting every {interval} frame(s)...")
    
    frame_count = 0
    extracted_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Save frame at specified interval
        if frame_count % interval == 0:
            output_path = os.path.join(
                output_folder, 
                f"frame_{frame_count:06d}.{format}"
            )
            cv2.imwrite(output_path, frame)
            extracted_count += 1
            
            if extracted_count % 10 == 0:
                print(f"Extracted {extracted_count} frames", end='\r')
        
        frame_count += 1
    
    cap.release()
    print(f"\nExtracted {extracted_count} frames to {output_folder}")
    print(f"Duration: {total_frames/fps:.2f}s")


def main():
    parser = argparse.ArgumentParser(
        description='Extract frames from a video'
    )
    parser.add_argument(
        'input_file',
        help='Input video file path'
    )
    parser.add_argument(
        'output_folder',
        help='Output folder for extracted frames'
    )
    parser.add_argument(
        '--interval',
        type=int,
        default=1,
        help='Extract every nth frame (default: 1 for all frames)'
    )
    parser.add_argument(
        '--format',
        default='jpg',
        choices=['jpg', 'png', 'bmp'],
        help='Output image format (default: jpg)'
    )
    
    args = parser.parse_args()
    
    extract_frames(args.input_file, args.output_folder, 
                   args.interval, args.format)


if __name__ == '__main__':
    main()
