import sys


def main():
    builtin_cmd = {
        "exit": lambda user_input:sys.exit(0),
        "type": lambda cmd: print(f"{cmd} is a shell builtin")
        if cmd in builtin_cmd
        else print(f"{cmd}: not found"),
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
