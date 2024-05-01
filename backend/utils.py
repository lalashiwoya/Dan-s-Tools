import os
from dotenv import load_dotenv
load_dotenv()

def add_ffmpeg_path_to_env():
    ffmpeg = os.getenv("FFMPEG")
    print(ffmpeg_path)
    current_path = os.environ.get("PATH", "")
    new_path = f"{current_path}:{ffmpeg_path}"
    os.environ['PATH'] = new_path