'''
Copyright (C) 2022 Kiet Pham <kiet.riley2005@gmail.com>
This software/program has a copyright license, more information is in the 'LICENSE' file
IF YOU WANT TO USE/COPY/MODIFY/REPRODUCE/RE-DISTRIBUTE THIS PROGRAM, YOU MUST INCLUDE A COPY OF THE LICENSE

Author Name: Kiet Pham
Author Contact: kiet.riley2005@gmail.com
Discord: CaptainVietnam6#0001
Discord Server: https://discord.gg/3z76p8H5yj
GitHub: https://github.com/CaptainVietnam6
Instagram: @itzkiettttt_fpv
Program Status: ACTIVE

'''
#ok literally this is really inefficient
#but i wanted to do this for fun
import os
import termcolor
from termcolor import colored

def clear():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

def generator():
    write_type = int(input("Write single file[1] or multiple files[2]?: "))
    clear()

    #checks to see if an outout folder is already made
    #if False, will make a folder named "output"
    if os.path.isdir("output") == False:
        os.mkdir("output")

    if write_type == 1:
        file_size_check = False
        while file_size_check == False:
            file_size = int(input("Please enter the file size you desire in kilobytes (1024 bytes, 8192 bits):\n"))
            if file_size_check < 1:
                print("Minimum file size is 1 kilobyte, please re-enter a valid number")


generator()