from datetime import *
import os
def file_writer_personal(user, message_user, message_ai):
    file = open(f"history/session_{user}_individual_{date.today()}.txt", "a+")
    file.writelines(f"{message_user} \n")
    file.writelines(f"{message_ai} \n")
    file.close()

def file_writer_group(name_grup, user, message_user, message_ai):
    file = open(f"history/session_{name_grup}_{date.today()}.txt", "a+")
    file.writelines(f"{user}: {message_user} \n")
    file.writelines(f"AI: {message_ai} \n")
    file.close()

def file_reader(user):
    file = open(f"history/session_{user}_{date.today()}.txt", "r+")
    return ''.join(file.readlines())

def path(user):
    file = os.path.abspath(f"history/session_{user}_{date.today()}.txt")
    return file

