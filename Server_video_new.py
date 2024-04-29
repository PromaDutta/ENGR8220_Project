import subprocess

def save_and_play_video_stream_udp(port, output_filename):
    # Command to save the incoming UDP stream to a file
    ffmpeg_save_command = [
        'ffmpeg',
        '-i', f'udp://:{port}',  # Input from the specified UDP port
        '-vcodec', 'mpeg4',
        '-c', 'copy',            # Copy the stream without re-encoding
        '-f', 'mpegts',          # Use MPEG-TS format for compatibility
        output_filename          # Output filename
    ]

  
    # Command to play the incoming UDP stream
    #ffmpeg_play_command = [
    #   'ffplay',
    #   '-i', f'udp://:{port}',  # Input from the specified UDP port
    #   '-window_title', 'Video Stream',  # Set the window title
    #   '-x', '640', '-y', '480'  # Set the window size (optional)
    #]

    # Start the subprocess to save the stream
    save_process = subprocess.Popen(ffmpeg_save_command)

    # Start the subprocess to play the stream
    #play_process = subprocess.Popen(ffmpeg_play_command)

    # Wait for the save process to complete
    save_process.wait()

    # Stop the play process after the save process is finished
    #play_process.terminate()

if __name__ == "__main__":
    PORT = 12345 # The UDP port to listen to
    OUTPUT_FILENAME = '/home/wifi/Desktop/codes/received_pothole_video.mp4'  # The filename to save the video
    save_and_play_video_stream_udp(PORT, OUTPUT_FILENAME)
