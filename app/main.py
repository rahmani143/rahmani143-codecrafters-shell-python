import sys
from pathlib import Path
import os

def find_in_path(command_path):
    path_env = os.environ.get("PATH", "")
    if not path_env:
        return None

    directories = path_env.split(os.pathsep)
    for directory in directories:
        if not os.path.isdir(directory):
            continue
        fullpath = os.path.join(directory,command_path)

        if os.path.isfile(full_path) and os.access(fullpath, os.X_OK):
            return fullpath
    return None

def handle_type(cmd_arg, builtin_cmds):
    if cmd_arg in builtin_cmds:
        print(f"{cmd_arg} is a shell builtin")
        return
    
    path_location = find_in_path(cmd_arg)
    if path_location:
        print(f"{cmd_arg} is {path_location}")
        return
    
    print(f"{cmd_arg}: not found")

def main():
    builtin_cmd = {
        "exit": lambda args:sys.exit(0),
        "type": lambda args:handle_type(args) ,
        "echo": lambda args:print(args),
    }
    while True:
        print("$ ",end="")
        command, *args = input().strip().split()

        if command in builtin_cmd:
            builtin_cmd[command](" ".join(args))
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
