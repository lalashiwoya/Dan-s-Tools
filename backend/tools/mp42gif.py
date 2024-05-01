import subprocess
import os
from datetime import datetime
import sys
from .mp4_play_speed import change_mp4_speed
from dotenv import load_dotenv
load_dotenv()

def convert_mp4_to_gif(input_mp4_path:str, gif_path: str, speed: float):
    temp_mp4_path = os.path.join(os.path.dirname(input_mp4_path), f"{datetime.now().strftime('%Y-%m-%d-%H:%M:%S')}.mp4")
    ffmpeg = os.getenv("FFMPEG")
    
    change_mp4_speed(input_mp4_path, temp_mp4_path, speed)
    
    try:
        subprocess.run(
            [ffmpeg, '-i', temp_mp4_path, gif_path],
            check=True
        )
    except subprocess.CalledProcessError:
        print('Failed to create GIF file.', file=sys.stderr)
        sys.exit(1)
        
    try:
        os.remove(temp_mp4_path)
        print(f"Removed intermediate file: {temp_mp4_path}")
    except OSError as e:
        print(f"Error: {e.strerror}, while trying to delete {temp_mp4_path}")
        
    print('Your GIF has been successfully generated.')