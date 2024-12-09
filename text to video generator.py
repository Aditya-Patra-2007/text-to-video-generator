import PyPDF2
from g4f.client import Client
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from PIL import Image
import os
import requests

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = []
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                page_text = page.extract_text()
                text.append(page_text)
            return text
    except Exception as e:
        print(f"Error occurred while extracting text from PDF: {e}")

def summarize_text(text):
    summary=""
    try:
        for i in text:
            client = Client()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"remove every which is not related to context and Summarize the following text: {i}"}]
            )
            line_summary = response.choices[0].message.content
            summary += line_summary + "\n"
        return summary
    except Exception as e:
        print(f"Error occurred while summarizing text: {e}")


def text_to_speech(text, audio_path):
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(audio_path)
    except Exception as e:
        print(f"Error occurred while converting text to speech: {e}")

def download_image(url, save_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image successfully downloaded: {save_path}")
        else:
            print(f"Failed to retrieve image. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while downloading immage : {e}")

def generate_images_url(summery):
    url=[]
    output = summery.replace(" ", "").split(",")
    for i in output:
        client = Client()
        try:
            response = client.images.generate(
                model="playground-v2.5",
                prompt=f"create a picture from{i}",
            )
            image_url = response.data[0].url
            url.append(image_url)
        except Exception as e:
            continue
    return url
def generate_images(url):
    image_paths=[]
    x=0
    try:
        for i in url:
            download_image(i,r"C:\Users\adity\OneDrive\Desktop\project\image\image"+str(x)+".jpg")
            image_paths.append(r"C:\Users\adity\OneDrive\Desktop\project\image\image"+str(x)+".jpg")
            x+=1
    except Exception as e:
        print(f"Error occurred while downloading images: {e}")
    return image_paths
        
def create_video_with_audio(image_paths, audio_path, output_path):
    try:
        audio_clip = AudioFileClip(audio_path)
        image_clips = []
        duration_per_image = audio_clip.duration / len(image_paths)
        for img_path in image_paths:
            img = ImageClip(img_path).set_duration(duration_per_image)
            image_clips.append(img)
        video = concatenate_videoclips(image_clips, method="compose")
        video = video.set_audio(audio_clip)
        video.write_videofile(output_path, fps=24)
    except Exception as e:
        print(f"Error occurred while creating video: {e}")

def main(pdf_path, output_video_path):
    extracted_text = extract_text_from_pdf(pdf_path)
    print("Extracted text from PDF")
    summary = summarize_text(extracted_text)
    print("Summarized text")
    audio_path = r"C:\Users\adity\OneDrive\Desktop\project\audio\audio.mp3"
    text_to_speech(summary, audio_path)
    print("mp3 file created")
    url=generate_images_url(summary)
    print("Generated image URLs")
    image_paths = generate_images(url)
    print("downloded images")
    create_video_with_audio(image_paths, audio_path, output_video_path)
    print("Video created")
    os.remove(audio_path)
    for img_path in image_paths:
        os.remove(img_path)

pdf_path = r"C:\Users\adity\OneDrive\Desktop\project\pdf\lefl112.pdf"
output_video_path = r"C:\Users\adity\OneDrive\Desktop\project\video pool\video1.mp4"
main(pdf_path, output_video_path)