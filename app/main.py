import sys
from pathlib import Path
import os
import subprocess

def find_in_path(command_path):
    path_env = os.environ.get("PATH", "")
    if not path_env:
        return None

    directories = path_env.split(os.pathsep)
    for directory in directories:
        if not os.path.isdir(directory):
            continue
        fullpath = os.path.join(directory,command_path)

        if os.path.isfile(fullpath) and os.access(fullpath, os.X_OK):
            return fullpath
    return None
def handle_pwd(args):
    return print(os.getcwd());

def handle_type(cmd_arg, builtin_cmds):
    if cmd_arg in builtin_cmds:
        print(f"{cmd_arg} is a shell builtin")
        return
    
    path_location = find_in_path(cmd_arg)
    if path_location:
        print(f"{cmd_arg} is {path_location}")
        return
    
    print(f"{cmd_arg}: not found")

def handle_cd(arguments_string):
    target = arguments_string.strip()

    if not target or target == "~":
        target = os.path.expanduser("~")
    
    if os.path.isdir(target):
        try:
            os.chdir(target)
        except PermissionError:
            print(f"cd: {target}: Permission denied")


def main():
    builtin_cmd = {
        "exit": lambda args:sys.exit(0),
        "type": lambda args:handle_type(args,builtin_cmd.keys()) ,
        "echo": lambda args:print(args),
        "pwd" : handle_pwd,
        "cd"  : handle_cd,
    }
    while True:
        print("$ ",end="")
        raw_input = input().strip()
        if not raw_input:
            continue

        command, *args_list = raw_input.split()

        if command in builtin_cmd:
            arguments_string = " ".join(args_list)
            builtin_cmd[command](arguments_string)
        else:
            external_path = find_in_path(command)

            if external_path:
                spawn_args = [command] + args_list
                subprocess.run(spawn_args)
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
