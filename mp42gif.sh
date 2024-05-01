#!/bin/bash

if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <input file> <output MKV file> <output GIF file> <speed>"
    exit 1
fi

input_mp4="$1"
output_mkv="$2"
output_gif="$3"
speed="$4"

# Run FFmpeg to adjust video speed and output as MKV
ffmpeg -i "$input_mp4" -vf "setpts=1/$speed*PTS" "$output_mkv"

# Check if FFmpeg process was successful before proceeding
if [ $? -eq 0 ]; then
    # Convert the resulting MKV to a GIF
    ffmpeg -i "$output_mkv" "$output_gif"

    # Check if GIF conversion was successful
    if [ $? -eq 0 ]; then
        echo "GIF created successfully. Removing intermediate MKV file..."
        rm "$output_mkv"  # This command deletes the intermediate MKV file
        echo "Intermediate MKV file removed."
    else
        echo "Failed to create GIF. Intermediate MKV file not removed."
    fi
else
    echo "Failed to create MKV file. Check input file and parameters."
fi

echo "Script completed."
