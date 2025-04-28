from datetime import *
import os
import json
def file_writer_personal(user, message_user, message_ai):
    file = open(f"history/session_{user}_individual.txt", "a+")
    file.writelines(f"{message_user} \n")
    file.writelines(f"{message_ai} \n")
    file.close()

def file_writer_group(name_grup, user, message_user, message_ai):
    file = open(f"history/session_{name_grup}.txt", "a+")
    file.writelines(f"{user}: {message_user} \n")
    file.writelines(f"AI: {message_ai} \n")
    file.close()

def file_reader(user):
    file = open(f"history/session_{user}.txt", "r+")
    return ''.join(file.readlines())

def path(user):
    file = os.path.abspath(f"history/session_{user}.txt")
    return file

def clear_file(name):
    open(f'history/session_{name}.txt', 'w').close()

def add_user_json(user):
    with open("status.json", 'r') as file:
        name = json.load(file)

    with open("status.json", 'w') as fort:
        if user not in name['users']:
            name['users'].append(user)
        json.dump(name, fort, indent=4)

def open_json(name_file):
    with open(name_file, 'r') as file:
        name = json.load(file)
    return name

def clear_user_json():
    with open("status.json", 'r') as file:
        name = json.load(file)

    with open("status.json", 'w') as fort:
        for i in range(len(name['users'])):
            name['users'].pop(i)
        json.dump(name, fort, indent=4)