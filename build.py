import json
import os
import shutil
import sys
import subprocess,signal
from datetime import datetime

MARLIN_PATH = "Marlin/"
OUTPUT_DIR = "bin/"
ENVI_NAME = "LPC1768"
AUTO_COMPILE_VERSION = "v0.2.0"
PLATFORMIO_PATH = "/usr/bin/platformio"
WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
BUILD_TEMP_FILE = [".pio/build",".pio/libdeps"]
PLATFORMIO_OUTPUT_DIR = ".pio/build/"
VERSION_FILE = WORKING_DIR + "/" + MARLIN_PATH + "Version.h"
VERSION_FILE_BACKUP = VERSION_FILE + ".bak"

STRING_DISTRIBUTION_DATE = "#define STRING_DISTRIBUTION_DATE \"" + datetime.now().strftime("%Y-%m-%d") + "\"\n"
DETAILED_BUILD_VERSION = "#define DETAILED_BUILD_VERSION SHORT_BUILD_VERSION \" (MagiNeko)\"\n"

print("Marlin 2 firmware cli compiler " + AUTO_COMPILE_VERSION + "\n")

# try to delete the old files
try:
    os.remove(WORKING_DIR + "/" + OUTPUT_DIR + "firmware.bin")
    for tempDir in BUILD_TEMP_FILE:
        shutil.rmtree(tempDir)
except Exception:
    pass


# make folder for output file
try:
    os.makedirs(WORKING_DIR + "/" + OUTPUT_DIR, exist_ok=True)
except FileExistsError:
    # directory already exists
    pass

# Update version.h
try:
    os.rename(VERSION_FILE, VERSION_FILE_BACKUP)
    with open(VERSION_FILE_BACKUP) as versionFileTemplate:
        lines = versionFileTemplate.readlines()
        # replace the content
        for i in range(0,len(lines)):
            if "#define STRING_DISTRIBUTION_DATE" in lines[i]:
                lines[i] = STRING_DISTRIBUTION_DATE
            if "#define DETAILED_BUILD_VERSION" in lines[i]:
                lines[i] = DETAILED_BUILD_VERSION
        # write new version file
        with open(VERSION_FILE,"w") as versionFile:
            versionFile.writelines(lines)
except Exception as e:
    print(e)
    exit(1)


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
    print("\nCopy binary output file to " + WORKING_DIR + "/" + OUTPUT_DIR + "firmware.bin")
    shutil.copy(WORKING_DIR + "/" + PLATFORMIO_OUTPUT_DIR + ENVI_NAME +"/firmware.bin",WORKING_DIR + "/" + OUTPUT_DIR + "firmware.bin")
    print("Done :3")
else:
    print("Ground control to Major Tom : Your config file is suck, there is some thing wrong.")
print("Press ENTER to exit.")
input()
sys.exit(0)
