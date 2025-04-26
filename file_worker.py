from datetime import *
import os
def file_writer(user, message_user, message_ai):
    file = open(f"session_{user}_{date.today()}.txt", "a+")
    file.writelines(f"{message_user} \n")
    file.writelines(f"{message_ai} \n")
    file.writelines("_______________________________________\n")
    file.close()

def file_reader(user):#сделать массивом
    file = open(f"session_{user}_{date.today()}.txt", "r+")
    return file.readline()

def path(user):
    file = os.path.abspath(f"session_{user}_{date.today()}.txt")
    return file

file_writer('Alex', 'Hello', 'Hello, how are you')
print(file_reader("Alex"))
print(path("Alex"))
