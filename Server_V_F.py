import subprocess

def receive_and_save_frames(port, output_folder, num_images, interval):
    command = [
        'ffmpeg',
        '-i', f'udp://0.0.0.0:{port}',
        '-vf', f'select=not(mod(n\,{interval}))',  # Select one frame every 'interval' frames
        '-vsync', 'vfr',  # Output variable frame rate
        '-frame_pts', 'true',  # Use presentation timestamp for filenames
        '-frames:v', str(num_images),  # Number of frames to capture
        f'{output_folder}/img_%03d.png'  # Output file pattern
    ]
    subprocess.run(command)

if __name__ == "__main__":
    PORT = '12345'  # The UDP port to listen to
    OUTPUT_FOLDER = '/home/wifi/Desktop/codes/SVR_0_loss' # Path to the folder where images will be saved
    NUM_IMAGES = 20  # Total number of images to save
    INTERVAL = 10  # Save every 10th frame
    receive_and_save_frames(PORT, OUTPUT_FOLDER, NUM_IMAGES, INTERVAL)
