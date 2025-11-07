#!/usr/bin/env python3
"""
Video generation script using Google's Veo3 video generation model.

This script demonstrates how to generate videos using the Veo-3.1 model
with customizable prompts, aspect ratios, and resolutions.
"""

import time
import argparse
from google import genai
from google.genai import types


def generate_video(
    prompt: str,
    output_filename: str = "generated_video.mp4",
    negative_prompt: str = "",
    aspect_ratio: str = "9:16",
    resolution: str = "720p",
    model: str = "veo-3.1-fast-generate-preview",
    poll_interval: int = 20,
) -> None:
    """
    Generate a video using Google's Veo3 model.

    Args:
        prompt: The text prompt describing the video to generate
        output_filename: Output filename for the generated video
        negative_prompt: Things to avoid in the generated video
        aspect_ratio: Video aspect ratio (e.g., "9:16", "16:9", "1:1")
        resolution: Video resolution (e.g., "720p", "1080p")
        model: The Veo model to use
        poll_interval: Time in seconds between polling for completion
    """
    print(f"Initializing Veo3 video generation...")
    print(f"Prompt: {prompt}")
    print(f"Model: {model}")
    print(f"Aspect Ratio: {aspect_ratio}")
    print(f"Resolution: {resolution}")
    if negative_prompt:
        print(f"Negative Prompt: {negative_prompt}")
    print()

    # Initialize the client
    client = genai.Client()

    # Start video generation
    config = types.GenerateVideosConfig(
        aspect_ratio=aspect_ratio,
        resolution=resolution,
    )

    if negative_prompt:
        config.negative_prompt = negative_prompt

    print("Starting video generation operation...")
    operation = client.models.generate_videos(
        model=model,
        prompt=prompt,
        config=config,
    )

    # Poll for completion
    print("Waiting for video generation to complete...")
    while not operation.done:
        time.sleep(poll_interval)
        operation = client.operations.get(operation)
        print(f"Status: {operation.metadata.get('state', 'PROCESSING')}...")

    print("\nVideo generation complete!")

    # Download and save the video
    generated_video = operation.response.generated_videos[0]
    print(f"Downloading video to {output_filename}...")
    client.files.download(file=generated_video.video)
    generated_video.video.save(output_filename)

    print(f"✓ Video saved successfully to {output_filename}")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Generate videos using Google's Veo3 model",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate a video with default settings
  python generate_video.py "a close-up shot of a golden retriever playing in a field of sunflowers"

  # Generate with custom aspect ratio and resolution
  python generate_video.py "ocean waves at sunset" --aspect-ratio "16:9" --resolution "1080p"

  # Generate with negative prompt to avoid certain elements
  python generate_video.py "a cat playing piano" --negative-prompt "dogs, drums" --output "cat_piano.mp4"
        """
    )

    parser.add_argument(
        "prompt",
        type=str,
        help="Text prompt describing the video to generate"
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default="generated_video.mp4",
        help="Output filename for the generated video (default: generated_video.mp4)"
    )

    parser.add_argument(
        "-n", "--negative-prompt",
        type=str,
        default="",
        help="Negative prompt - things to avoid in the generated video"
    )

    parser.add_argument(
        "-a", "--aspect-ratio",
        type=str,
        default="9:16",
        choices=["9:16", "16:9", "1:1"],
        help="Video aspect ratio (default: 9:16)"
    )

    parser.add_argument(
        "-r", "--resolution",
        type=str,
        default="720p",
        choices=["720p", "1080p"],
        help="Video resolution (default: 720p)"
    )

    parser.add_argument(
        "-m", "--model",
        type=str,
        default="veo-3.1-fast-generate-preview",
        help="Veo model to use (default: veo-3.1-fast-generate-preview)"
    )

    parser.add_argument(
        "-p", "--poll-interval",
        type=int,
        default=20,
        help="Polling interval in seconds (default: 20)"
    )

    args = parser.parse_args()

    try:
        generate_video(
            prompt=args.prompt,
            output_filename=args.output,
            negative_prompt=args.negative_prompt,
            aspect_ratio=args.aspect_ratio,
            resolution=args.resolution,
            model=args.model,
            poll_interval=args.poll_interval,
        )
    except Exception as e:
        print(f"Error generating video: {e}")
        raise


if __name__ == "__main__":
    main()
