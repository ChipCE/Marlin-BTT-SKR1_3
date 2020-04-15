import json
import os
import shutil
import sys
import subprocess,signal

MARLIN_PATH = "Marlin/"
OUTPUT_DIR = "bin/"
ENVI_NAME = "LPC1768"
AUTO_COMPILE_VERSION = "v0.2.0"
PLATFORMIO_PATH = "/usr/bin/platformio"
WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
BUILD_TEMP_FILE = [".pio/build",".pio/libdeps"]
PLATFORMIO_OUTPUT_DIR = ".pio/build/"

print("Marlin 2 firmware cli compiler " + AUTO_COMPILE_VERSION + "\n")

# try to delete the old files
try:
    os.remove(OUTPUT_DIR + "firmware.bin")
    for tempDir in BUILD_TEMP_FILE:
        shutil.rmtree(tempDir)
except Exception:
    pass


# make folder for output file
try:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
except FileExistsError:
    # directory already exists
    pass

# Execute platformio build
# os.system("platformio run -e "+ENVI_NAME)
proc = subprocess.Popen([PLATFORMIO_PATH + " " + "run -e " + ENVI_NAME], cwd = WORKING_DIR, shell=True)

try:
    proc.communicate()
except Exception as e:
    proc.kill()
    print(e)

if proc.returncode == 0:
    # copy binary file to OUTPUT_DIR
    print("\nCopy binary output file to " + OUTPUT_DIR + "firmware.bin")
    shutil.copy(PLATFORMIO_OUTPUT_DIR + ENVI_NAME +"/firmware.bin", OUTPUT_DIR + "firmware.bin")
    print("Done :3")
else:
    print("Ground control to Major Tom : Your config file is suck, there is some thing wrong.")
print("Press ENTER to exit.")
input()
sys.exit(0)
