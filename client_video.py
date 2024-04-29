import subprocess

def stream_video_file_udp(host, port, file_path):
    ffmpeg_command = [
        'ffmpeg',
        '-re',                           							# Read input at native frame rate
        '-i', '/home/wifi/Desktop/codes/pothole_video.mp4',         # Input file path
        '-c', 'copy',                    							# Use the same codec for copying the stream
        '-f', 'mpegts',                  							# MPEGTS format for transport stream
        f'udp://{host}:{port}'           							# Destination UDP address
    ]

    # Run the FFmpeg command in a subprocess
    subprocess.run(ffmpeg_command)

if __name__ == "__main__":
    HOST = '0.0.0.0'  # Replace with the server's actual IP address
    PORT = 12345        # The UDP port to stream to
    FILE_PATH = '/home/wifi/Desktop/codes/pothole_video.mp4'   # Replace with the path to your video file
    stream_video_file_udp(HOST, PORT, FILE_PATH)
