import subprocess
import os
from datetime import datetime
import sys
from dotenv import load_dotenv
load_dotenv()

def change_mp4_speed(input_mp4_path:str, output_mp4_path:str, speed: float): 
    ffmpeg = os.getenv("FFMPEG")
    try:
        subprocess.run(
            [ffmpeg, '-i', input_mp4_path, '-vf', f'setpts=1/{speed}*PTS', output_mp4_path],
            check=True
        )
    except subprocess.CalledProcessError:
        print('Speed-altered MP4 file creation failed.', file=sys.stderr)
        sys.exit(1)