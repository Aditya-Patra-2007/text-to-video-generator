# Text to Video Generator

This project converts text from PDF files into video presentations with audio narration and relevant images. It extracts text from a PDF, summarizes it, converts the summary to speech, generates relevant images, and combines everything into a video.

## Features

- PDF text extraction
- Text summarization using GPT-3.5
- Text-to-speech conversion
- Automatic image generation based on text content
- Video generation with synchronized audio and images

## Prerequisites

Before running this project, make sure you have Python installed on your system. The following Python packages are required:

- PyPDF2
- g4f
- gTTS (Google Text-to-Speech)
- moviepy
- Pillow (PIL)
- requests

## Installation

1. Clone or download this repository
2. Install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```

## Project Structure

The project expects the following directory structure:

```
project/
├── code/
│   ├── text to video generator.py
│   └── requirements.txt
├── pdf/
│   └── (your PDF files)
├── image/
│   └── (temporary images will be stored here)
├── audio/
│   └── (temporary audio will be stored here)
└── video pool/
    └── (output videos will be stored here)
```

## Usage

1. Place your PDF file in the `pdf` directory
2. Update the file paths in the script if necessary:
   - `pdf_path`: Path to your input PDF file
   - `output_video_path`: Path where you want to save the output video

3. Run the script:
   ```
   python text to video generator.py
   ```

The script will:
1. Extract text from the PDF
2. Generate a summary using GPT-3.5
3. Convert the summary to speech
4. Generate relevant images
5. Create a video combining the images and audio
6. Clean up temporary files automatically

## Demonstrations and Examples

### Tutorial Video
A comprehensive video tutorial demonstrating how to use this code is available [here](https://drive.google.com/file/d/1-28BGQKzAlR0DqwsgeQnPlwSvbFXcD83/view?usp=drive_link).

### Sample Outputs
Here are some example videos generated using this code:
- [Sample Video 1](https://drive.google.com/file/d/100fTCTRnrg7bDcw9a1LE837MgsSw3Hdj/view?usp=drive_link)
- [Sample Video 2](https://drive.google.com/file/d/1nfgbvvxq1j_qSZez8WxfAETyFCbHta_u/view?usp=drive_link)

## Note

- Make sure all the required directories (pdf, image, audio, video pool) exist before running the script
- The script automatically cleans up temporary audio and image files after video creation
- Internet connection is required for text summarization and image generation

## Error Handling

The script includes error handling for various operations:
- PDF text extraction
- Text summarization
- Text-to-speech conversion
- Image downloading
- Video creation

If any errors occur during execution, they will be printed to the console with appropriate error messages.
