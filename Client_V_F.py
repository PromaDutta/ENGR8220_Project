import subprocess

def stream_video(file_path, destination_ip, port):
    command = [
        'ffmpeg',
        '-re',
        '-i', file_path,
        '-c:v', 'libx264',
        '-preset', 'ultrafast',
        '-tune', 'zerolatency',
        '-f', 'mpegts',
        f'udp://{destination_ip}:{port}'
    ]
    subprocess.run(command)

if __name__ == "__main__":
    VIDEO_FILE_PATH = '/home/wifi/Desktop/codes/pothole_video.mp4'  # Path to the video file
    DESTINATION_IP = '10.0.0.2'  # Replace with your server's IP address
    PORT = '12345'  # The port to stream to
    stream_video(VIDEO_FILE_PATH, DESTINATION_IP, PORT)
