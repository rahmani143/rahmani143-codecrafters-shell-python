import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while(True):
        sys.stdout.write("$ ")
        command = input()
        commands = ["echo","exit","type"]
        part = command.split(maxsplit = 1)
        first = part[0]
        if command == "exit":
            break
        if first == "echo":
            print(part[1])
        if first == "type":
            if part[1] in commands:
                print(f"{part[1]} is a shell builtin")
            else:
                print(f"{part[1]}: not found")
        else:
            print(f"{command}: command not found")
    pass


if __name__ == "__main__":
    main()
