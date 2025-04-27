from datetime import *
import os
def file_writer(user, message_user, message_ai):
    file = open(f"history/session_{user}_{date.today()}.txt", "a+")
    file.writelines(f"{message_user} \n")
    file.writelines(f"{message_ai} \n")
    file.close()

def file_reader(user):
    file = open(f"history/session_{user}_{date.today()}.txt", "r+")
    return ''.join(file.readlines())

def path(user):
    file = os.path.abspath(f"history/session_{user}_{date.today()}.txt")
    return file

