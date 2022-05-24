#This script will change your wallpaper at random times to a random wallpaper in the c:\scripts\wallpaper folder. Must create a wallpapers.dat file with a list of all wallpapers in that dir. one per line ex: C:\\scripts\\wallpapers\\bananas4.jpg 

# Loop forever
while True:

    # Import needed modules

    import random
    import time
    import os
    import shutil
    import getpass

    # Define random seconds variable for wait
    random_seconds = random.randint(300, 1800)

    # Get random line in .dat file
    line = open('c:\\scripts\\wallpapers.dat').read().splitlines()
    randomline = random.choice(line)
    print(randomline)

    # Copy wallpaper to user folder
    username = getpass.getuser()

    # Sleep random seconds and copy wallpaper and overwrite current wallpaper
    time.sleep(random_seconds)
    path = os.path.join('C:\\users', getpass.getuser(), 'AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper')
    shutil.copyfile(randomline, path)

    # Run rundll32.exe command to refresh desktop
    os.system('rundll32.exe USER32.DLL,UpdatePerUserSystemParameters 1, True')

    # Sleep for random number of seconds between 300 and 1800 seconds before looping
    time.sleep(random_seconds)
