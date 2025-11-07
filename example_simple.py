#!/usr/bin/env python3
"""
Simple example script for generating a video with Google's Veo3.
This is a minimal implementation based on the basic usage pattern.
"""

import time
from google import genai
from google.genai import types

# Initialize the client
client = genai.Client()

# Start video generation with custom prompt
operation = client.models.generate_videos(
    model="veo-3.1-fast-generate-preview",
    prompt="a close-up shot of a golden retriever playing in a field of sunflowers",
    config=types.GenerateVideosConfig(
        negative_prompt="barking, woofing",
        aspect_ratio="9:16",
        resolution="720p",
    ),
)

# Wait for the video to be generated
print("Generating video...")
while not operation.done:
    time.sleep(20)
    operation = client.operations.get(operation)
    print("Still processing...")

print("Video generation complete!")

# Download and save the video
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video)
generated_video.video.save("golden_retriever.mp4")

print("Video saved as golden_retriever.mp4")
