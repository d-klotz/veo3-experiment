# Veo3 Video Generation Experiment

This repository contains scripts for generating videos using Google's Veo3 video generation model.

## Overview

Veo3 is Google's state-of-the-art video generation model that can create high-quality videos from text prompts. This project provides both simple and advanced scripts for working with the Veo-3.1 API.

## Prerequisites

- Python 3.7 or higher
- Google Cloud account with Veo3 API access
- Google API key with GenAI permissions

## Installation & Setup

1. **Clone the repository** (if not already done):
```bash
git clone <your-repo-url>
cd veo3-experiment
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Configure authentication**:

   Option A - Environment variable:
   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   ```

   Option B - Create a .env file:
   ```bash
   cp .env.example .env
   # Edit .env and add your API key
   ```

4. **Verify setup** (optional):
```bash
python -c "from google import genai; print('SDK installed successfully')"
```

## Where Videos Are Saved

- **Simple script** (`example_simple.py`): Saves to `golden_retriever.mp4` in the current directory
- **Advanced script** (`generate_video.py`):
  - Default: `generated_video.mp4` in the current directory
  - Custom: Use `-o` flag to specify any path, e.g., `--output /path/to/my_video.mp4`

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

- `prompt` - Text description of the video to generate (required) - **YES, you can use any prompt!**
- `-o, --output` - Output filename (default: generated_video.mp4)
- `-n, --negative-prompt` - Things to avoid in the video
- `-a, --aspect-ratio` - Aspect ratio: 9:16, 16:9, or 1:1 (default: 9:16)
- `-r, --resolution` - Resolution: 720p or 1080p (default: 720p)
- `-m, --model` - Veo model to use (default: veo-3.1-fast-generate-preview)
- `-p, --poll-interval` - Polling interval in seconds (default: 20)

### Custom Prompts

Yes! You can use **any text prompt** you want. The script accepts any description and passes it to the Veo3 model. Examples:

```bash
# Nature scenes
python generate_video.py "time-lapse of cherry blossoms blooming in spring"

# Action scenes
python generate_video.py "skateboard trick in slow motion at sunset"

# Abstract concepts
python generate_video.py "colorful paint mixing in water, macro shot"

# Cinematic shots
python generate_video.py "dramatic overhead drone shot of a winding mountain road"
```

The model works best with:
- Clear, descriptive language
- Specific camera angles/movements
- Lighting and mood descriptors
- Concrete visual elements

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
