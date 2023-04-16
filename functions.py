from pydub import AudioSegment
import os


def convert_audio_files(input_folder, output_folder, input_format):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

