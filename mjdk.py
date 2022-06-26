import platform
from Commands import Command


# ------------------------------------FUNCTIONLESS--------------------------------------

def run():
    system_type = platform.system()
    system_architect = platform.architecture()
    print(system_type, system_architect)
    if system_type.__eq__("Windows") and system_architect.__contains__("64bit"):
        command = Command()
        while True:
            if command.detect_Command(input("Enter the mjdk command:")) is False:
                break
    else:
        print("Error, Operating System not support \n"
              "This tool only work in Windows operating system with architecture 64Bit")


if __name__ == '__main__':
    run()
