from flask import Flask, request, send_from_directory, abort
import subprocess
import os

app = Flask(__name__)

# Folder for uploaded files
UPLOAD_FOLDER = 'uploads'
# Folder for converted files
CONVERTED_FOLDER = 'converted'
# Ensure these folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    # Save the uploaded file
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    # Define output paths
    output_mkv = os.path.join(CONVERTED_FOLDER, os.path.splitext(file.filename)[0] + '.mkv')
    output_gif = os.path.join(CONVERTED_FOLDER, os.path.splitext(file.filename)[0] + '.gif')

    # Process the file (you'll need to adapt this to your actual script and requirements)
    try:
        # Convert video to MKV (example command)
        subprocess.run(['ffmpeg', '-i', input_path, output_mkv], check=True)
        # Convert MKV to GIF (example command)
        subprocess.run(['ffmpeg', '-i', output_mkv, '-f', 'gif', output_gif], check=True)
    except subprocess.CalledProcessError as e:
        return str(e), 500

    # Optional: clean up input and MKV files
    os.remove(input_path)
    os.remove(output_mkv)

    # Send the GIF file back
    return send_from_directory(CONVERTED_FOLDER, os.path.basename(output_gif), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
