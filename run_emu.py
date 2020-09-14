# // Run Android emulator without opening Android Studio
# // This script is written in Python and will merely
# // run two commands. Change Directory and execute emulator.

import os

# Make sure you have an existing Android Studio with downloaded emulator.
# Repalce the name of the emulator if necessary.
print('Attempting to run ./emulator -avd Pixel_2_API_R')
os.system('~/Library/Android/sdk/emulator/emulator -avd Pixel_2_API_R')
