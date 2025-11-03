#!/usr/bin/env python3
"""
Script to concatenate multiple videos into one.
"""
import argparse
from moviepy.editor import VideoFileClip, concatenate_videoclips


def concatenate_videos(input_files, output_file, method='compose'):
    """
    Concatenate multiple videos into one.
    
    Args:
        input_files: List of input video file paths
        output_file: Output video file path
        method: Concatenation method ('compose' or 'chain')
    """
    print(f"Loading {len(input_files)} videos...")
    clips = []
    
    for i, video_file in enumerate(input_files, 1):
        print(f"Loading video {i}/{len(input_files)}: {video_file}")
        clip = VideoFileClip(video_file)
        clips.append(clip)
    
    print("Concatenating videos...")
    final_clip = concatenate_videoclips(clips, method=method)
    
    print(f"Writing output to {output_file}...")
    final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
    
    # Close clips
    for clip in clips:
        clip.close()
    final_clip.close()
    
    print(f"\nVideos concatenated successfully: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Concatenate multiple videos into one'
    )
    parser.add_argument(
        'input_files',
        nargs='+',
        help='Input video files to concatenate'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output video file path'
    )
    parser.add_argument(
        '--method',
        default='compose',
        choices=['compose', 'chain'],
        help='Concatenation method (default: compose)'
    )
    
    args = parser.parse_args()
    
    concatenate_videos(args.input_files, args.output, args.method)


if __name__ == '__main__':
    main()
