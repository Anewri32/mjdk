import os
import sys
from modules import VarEnvironment, Download, Compress, JdkData


# ------------------------------------FUNCIONES--------------------------------------
def run():
    while True:
        command = input("Enter the mjdk command:")
        if "install" in command:
            jdk = ("install", command.removeprefix("install "))
        elif "use" in command:
            jdk = ("use", command.removeprefix("use "))
        elif command == "-h" or command == "-help":
            print("""
                install [jdk-version]           Allows to download the jdk, needs to be specified the version.
                use [jdk-version]               Sets the jdk to use, needs the version to be specified.
                exit                            Close the program.

                """)
            continue
        elif command.lower() == "exit":
            break
        else:
            print("Error, type a valid command\ntype -h or -help to get a list of commands that can be used.\n")
            continue
        # jdk_name("Aqui el nombre del jdk", "Aqui la extencion del archivo comprimido")
        jdk_name = detect_jdk(jdk[1])
        if jdk_name:
            if jdk[0] == "install":
                install(jdk_name[0], jdk_name[1])
            elif jdk[0] == "use":
                use(jdk_name[0])


def detect_jdk(i):
    i = i.lower()
    file = ".zip"
    if i == "9.0.4" or i == "9" or i == "jdk9" or i == "jdk=9" or i == "jdk@9":
        i = "jdk-9.0.4"
        file = ".tar.gz"
    elif i == "10.0.2" or i == "10" or i == "jdk10" or i == "jdk=10" or i == "jdk@10":
        i = "jdk-10.0.2"
        file = ".tar.gz"
    elif i == "11.0.2" or i == "11" or i == "jdk11" or i == "jdk=11" or i == "jdk@11":
        i = "jdk-11.0.2"
    elif i == "12.0.2" or i == "12" or i == "jdk12" or i == "jdk=12" or i == "jdk@12":
        i = "jdk-12.0.2"
    elif i == "13.0.2" or i == "13" or i == "jdk13" or i == "jdk=13" or i == "jdk@13":
        i = "jdk-13.0.2"
    elif i == "14.0.2" or i == "14" or i == "jdk14" or i == "jdk=14" or i == "jdk@14":
        i = "jdk-14.0.2"
    elif i == "15.0.2" or i == "15" or i == "jdk15" or i == "jdk=15" or i == "jdk@15":
        i = "jdk-15.0.2"
    elif i == "16.0.2" or i == "16" or i == "jdk16" or i == "jdk=16" or i == "jdk@16":
        i = "jdk-16.0.2"
    elif i == "17.0.2" or i == "17" or i == "jdk17" or i == "jdk=17" or i == "jdk@17":
        i = "jdk-17.0.2"
    elif i == "18.0.1.1" or i == "18" or i == "jdk18" or i == "jdk=18" or i == "jdk@18":
        i = "jdk-18.0.1.1"
    else:
        print("Enter a valid JDK version.")
        return None
    return i, file


def ruta():
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.abspath('.')


def install(i, file):
    jdk_path = ruta() + "\\" + i
    jdk_path_file = jdk_path + file
    if os.path.exists(jdk_path):
        print("The jdk is already installed.\n")
        return
    else:
        if os.path.exists(jdk_path_file):
            os.remove(jdk_path_file)
        Download.file(JdkData.jdk_list[i], jdk_path_file)
    print("Extracting...")
    if file == ".zip":
        result = Compress.extract_zip(jdk_path_file, ruta())
    else:
        result = Compress.extract_tar(jdk_path_file, ruta())
    if result:
        print("Jdk extracted.")
        print("To use the jdk type 'mjdk use " + i + "'\n")


def use(jdk_name):
    jdk_path = ruta() + "\\" + jdk_name
    if not os.path.exists(jdk_path):
        print("Error, jdk is not installed.")
    else:
        VarEnvironment.setx_var("JAVA_HOME", jdk_path)
        VarEnvironment.setx_add_path("%JAVA_HOME%\\bin")

        print(jdk_name + "it is now in use.\n")


if __name__ == '__main__':
    run()
