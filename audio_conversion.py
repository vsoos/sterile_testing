from pydub import AudioSegment
import os


def convert_audio_files(input_folder, output_folder, input_format):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

# Convert each file with the specified input format to .wav and save to output directory
    for file in os.listdir(input_folder):
        if file.endswith(input_format):
            filepath = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".wav")
            sound = AudioSegment.from_file(filepath, format=input_format)
            sound.export(output_path, format="wav")
