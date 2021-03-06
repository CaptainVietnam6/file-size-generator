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
from termcolor import colored
from timeit import default_timer as timer

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
        #checks the requested file size to be over 1 kilobyte and under 16 gigabyte
        #restricted to 16 gigabyte just to reduce processing times, feel free to change to your needs
        size_limit = 16000000 #in kilobytes
        file_size_check = False
        while file_size_check == False:
            file_size = float(input("Please enter the file size you desire in kilobytes (1024 bytes, 8192 bits):\n"))
            if file_size >= 1 and file_size <= size_limit:
                file_size_check = True
            else:
                if file_size < 1:
                    clear()
                    print(colored("Minimum file size is 1 kilobyte, please re-enter a valid number", "red"))
                elif file_size > size_limit:
                    clear()
                     #round function to remove ".0" at the end
                    print(colored(f"Cannot generate a file over {round(size_limit / 1000000)} gigabytes ({round(size_limit / 1000000)} million kilobytes)\nplease re-enter a valid number", "red"))
        
        #generate file
        start = timer()
        kilobyte = "0" * 1024
        file_output = ""
        write_cycle = 0
        for i in range(int(file_size)):
            file_output = file_output + kilobyte
            write_cycle += 1
            print(f"Wrote {write_cycle} kilobytes or {write_cycle * 1024} bytes")

        #write & create file
        f = open(f"{file_size}KB_file.txt", "w")
        f.write(file_output)
        end = timer()
        print(colored(f"File generation & write took {round(end - start, 5)} seconds", "green"))


generator()
