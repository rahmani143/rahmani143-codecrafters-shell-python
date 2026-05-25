import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while(True):
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            break
        commands = ["echo","exit","type"]
        part = command.split(maxsplit = 2)
        first = part[0]
        second = part[1]
        if first == "type":
            
            if second in commands:
                print(f"{second} is a shell builtin")
            else:
                print(f"{part[1]}: not found")
        if first == "echo":
            argument = " ".join(part[1:])
            print(argument)
            # if first == "type":
            #     if part[1] in commands:
            #         print(f"{part[1]} is a shell builtin")
            #     else:
            #         print(f"{part[1]}: not found")
        else:
            print(f"{command}: command not found")
    pass


if __name__ == "__main__":
    main()
