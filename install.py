import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
	
if __name__ == "__main__":
	packages = ("Pillow", "pynput", 
			 "Desktopmagic", "numpy", 
			 "pyautogui", "opencv-python", 
			 "configparser", 
			 "psutil", "PyQt5")

	for p in packages:
		install(p)