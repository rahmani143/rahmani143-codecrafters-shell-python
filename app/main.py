import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while(True):
        sys.stdout.write("$ ")
        command = input()
        part = command.split(maxsplit = 1)
        first = part[0]
        if command == "exit":
            break
        if command == "echo":
            print(part[1])
        else:
            print(f"{command}: command not found")
    pass


if __name__ == "__main__":
    main()
