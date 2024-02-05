import keyboard
import subprocess

# Define the path to NirCmd - adjust the path as necessary
nircmd_path = r"C:\Users\weswa\AppData\Local\Programs\Python\Python312\nircmd.exe"

# Define your screen resolutions (add more if you like)
resolutions = [(1920, 1080), (1600, 900)]
current_index = 0  # Start with the first resolution

def change_resolution():
    global current_index
    # Toggle between resolutions
    current_index = (current_index + 1) % len(resolutions)
    width, height = resolutions[current_index]
    
    # Construct the command to change screen resolution
    command = f'"{nircmd_path}" setdisplay {width} {height} 32'
    
    # Execute the command
    subprocess.run(command, shell=True)
    print(f"Resolution changed to: {width}x{height}")  # Optional: Print the new resolution

# Set a hotkey for changing the resolution, e.g., ctrl+shift+r
keyboard.add_hotkey('ctrl+shift+r', change_resolution)

# Keep the script running
print("Press ESC to stop.")
keyboard.wait('esc')
