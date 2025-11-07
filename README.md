# Veo3 Video Generation Experiment

This repository contains scripts for generating videos using Google's Veo3 video generation model.

## Overview

Veo3 is Google's state-of-the-art video generation model that can create high-quality videos from text prompts. This project provides both simple and advanced scripts for working with the Veo-3.1 API.

## Prerequisites

- Python 3.7 or higher
- Google GenAI Python SDK
- VEO3_API_KEY environment variable set

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your API key:
```bash
export VEO3_API_KEY="your-api-key-here"
```

## Usage

### Simple Example

The `example_simple.py` script demonstrates basic usage:

```bash
python example_simple.py
```

This will generate a video of a golden retriever playing in sunflowers and save it as `golden_retriever.mp4`.

### Advanced Script with CLI

The `generate_video.py` script provides a full-featured command-line interface:

```bash
# Basic usage
python generate_video.py "a close-up shot of a golden retriever playing in a field of sunflowers"

# Custom output filename
python generate_video.py "ocean waves at sunset" --output sunset.mp4

# Specify aspect ratio and resolution
python generate_video.py "a cat playing piano" --aspect-ratio "16:9" --resolution "1080p"

# Use negative prompts to avoid certain elements
python generate_video.py "a dog running in park" --negative-prompt "barking, cars, people"

# Combine multiple options
python generate_video.py "northern lights over mountains" \
  --output aurora.mp4 \
  --aspect-ratio "16:9" \
  --resolution "1080p" \
  --negative-prompt "clouds, rain"
```

### Command-line Options

- `prompt` - Text description of the video to generate (required)
- `-o, --output` - Output filename (default: generated_video.mp4)
- `-n, --negative-prompt` - Things to avoid in the video
- `-a, --aspect-ratio` - Aspect ratio: 9:16, 16:9, or 1:1 (default: 9:16)
- `-r, --resolution` - Resolution: 720p or 1080p (default: 720p)
- `-m, --model` - Veo model to use (default: veo-3.1-fast-generate-preview)
- `-p, --poll-interval` - Polling interval in seconds (default: 20)

## Files

- `generate_video.py` - Advanced CLI script with full customization options
- `example_simple.py` - Minimal example showing basic API usage
- `requirements.txt` - Python package dependencies

## Examples

### Portrait Mode Video (9:16)
```bash
python generate_video.py "a hummingbird feeding from flowers" --aspect-ratio "9:16"
```

### Landscape Video (16:9)
```bash
python generate_video.py "cinematic drone shot of coastal cliffs" --aspect-ratio "16:9"
```

### Square Video (1:1)
```bash
python generate_video.py "abstract paint swirls mixing colors" --aspect-ratio "1:1"
```

## API Reference

The script uses the Google GenAI Python SDK. Key components:

- `genai.Client()` - Initializes the API client
- `client.models.generate_videos()` - Starts video generation
- `types.GenerateVideosConfig` - Configuration for video generation
- `client.operations.get()` - Polls for operation status
- `client.files.download()` - Downloads the generated video

## Notes

- Video generation can take several minutes depending on complexity
- The script polls every 20 seconds by default (configurable)
- Generated videos are saved in MP4 format
- Ensure you have sufficient API quota for video generation

## License

This is an experimental project for testing Google's Veo3 video generation capabilities.
