Resolution Changer Script
Description
The Resolution Changer Script is a Python utility designed for Windows users who need a quick and easy way to switch between different screen resolutions. Leveraging the power of NirCmd and the Python keyboard library, it allows the user to change their screen resolution with a simple keyboard shortcut, enhancing productivity and ease of use.

Features
Instantly toggle between predefined screen resolutions.
Customizable keyboard shortcut for easy access.
Utilizes the NirCmd command-line tool for efficient screen resolution changes.
Installation
Prerequisites
Python 3.6 or newer.
NirCmd utility by NirSoft.
Setup Instructions
Clone the Repository
Clone the project to your local machine using the following command:

Copy code
git clone https://github.com/CWoods-Dev/CWoods-Dev.git
Install Python Dependencies
Navigate to the project directory and install the required Python library:

Copy code
pip install keyboard
Configure NirCmd

Download NirCmd from NirSoft's website.
Extract nircmd.exe into the project directory or a directory included in your system's PATH.
Usage
Run the script from a command prompt with administrative rights:

Copy code
python change_resolution.py
Keyboard Shortcuts
Change Resolution: Alt + Shift + R
Exit Script: Press the Backtick (`) key
Customizing Shortcuts
Edit the change_resolution.py file to modify the keyboard.add_hotkey command with your preferred key combination for changing the screen resolution or stopping the script.

Acknowledgments
Special thanks to NirSoft for the NirCmd utility, enabling the core functionality of this script.
This project was developed to offer a streamlined solution for users frequently needing to adjust their display settings across different tasks and workflows.
