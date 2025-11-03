#!/usr/bin/env python3
"""
Script to add text overlay to a video.
"""
import argparse
import cv2


def add_text_overlay(input_file, output_file, text, position='bottom-center', 
                     font_scale=1.0, color=(255, 255, 255), thickness=2):
    """
    Add text overlay to a video.
    
    Args:
        input_file: Input video file path
        output_file: Output video file path
        text: Text to overlay on the video
        position: Text position (top-left, top-center, top-right, 
                  bottom-left, bottom-center, bottom-right, center)
        font_scale: Font size scale (default: 1.0)
        color: Text color in BGR format (default: white)
        thickness: Text thickness (default: 2)
    """
    # Open the video
    cap = cv2.VideoCapture(input_file)
    
    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
    
    # Calculate text position
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    
    position_map = {
        'top-left': (10, text_size[1] + 10),
        'top-center': ((width - text_size[0]) // 2, text_size[1] + 10),
        'top-right': (width - text_size[0] - 10, text_size[1] + 10),
        'center': ((width - text_size[0]) // 2, (height + text_size[1]) // 2),
        'bottom-left': (10, height - 10),
        'bottom-center': ((width - text_size[0]) // 2, height - 10),
        'bottom-right': (width - text_size[0] - 10, height - 10),
    }
    
    text_position = position_map.get(position, position_map['bottom-center'])
    
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Add text to frame
        cv2.putText(frame, text, text_position, font, font_scale, 
                    color, thickness, cv2.LINE_AA)
        
        out.write(frame)
        frame_count += 1
        
        if frame_count % 30 == 0:
            print(f"Processing: {frame_count}/{total_frames} frames", end='\r')
    
    cap.release()
    out.release()
    print(f"\nVideo with text overlay created: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Add text overlay to a video'
    )
    parser.add_argument(
        'input_file',
        help='Input video file path'
    )
    parser.add_argument(
        'output_file',
        help='Output video file path'
    )
    parser.add_argument(
        'text',
        help='Text to overlay on the video'
    )
    parser.add_argument(
        '--position',
        default='bottom-center',
        choices=['top-left', 'top-center', 'top-right', 'center',
                 'bottom-left', 'bottom-center', 'bottom-right'],
        help='Text position (default: bottom-center)'
    )
    parser.add_argument(
        '--font-scale',
        type=float,
        default=1.0,
        help='Font size scale (default: 1.0)'
    )
    parser.add_argument(
        '--color',
        default='255,255,255',
        help='Text color in BGR format (default: 255,255,255 for white)'
    )
    parser.add_argument(
        '--thickness',
        type=int,
        default=2,
        help='Text thickness (default: 2)'
    )
    
    args = parser.parse_args()
    
    # Parse color
    color = tuple(map(int, args.color.split(',')))
    
    add_text_overlay(args.input_file, args.output_file, args.text,
                     args.position, args.font_scale, color, args.thickness)


if __name__ == '__main__':
    main()
