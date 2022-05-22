import os
import sys
import wget
import zipfile
import tarfile
from subprocess import call

# ------------------VARIABLES----------------------------------------------------------
# Variable de JDK para windows.
# Es necesario realizar pruebas, asi que se usaran urls con archivos mas ligeros
jdk_list = {
    "jdk_9": "https://download.java.net/java/GA/jdk9/9.0.4/binaries/openjdk-9.0.4_windows-x64_bin.tar.gz",
    "jdk_10": "https://download.java.net/java/GA/jdk10/10.0.2/19aef61b38124481863b1413dce1855f/13/openjdk-10.0.2_windows-x64_bin.tar.gz",
    "jdk_11": "https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_windows-x64_bin.zip",
    "jdk_12": "https://download.java.net/java/GA/jdk12.0.2/e482c34c86bd4bf8b56c0b35558996b9/10/GPL/openjdk-12.0.2_windows-x64_bin.zip",
    "jkd_13": "https://download.java.net/java/GA/jdk13.0.2/d4173c853231432d94f001e99d882ca7/8/GPL/openjdk-13.0.2_windows-x64_bin.zip",
    "jdk_14": "https://download.java.net/java/GA/jdk14.0.2/205943a0976c4ed48cb16f1043c5c647/12/GPL/openjdk-14.0.2_windows-x64_bin.zip",
    "jdk_15": "https://download.java.net/java/GA/jdk15.0.2/0d1cfde4252546c6931946de8db48ee2/7/GPL/openjdk-15.0.2_windows-x64_bin.zip",
    "jdk_16": "https://download.java.net/java/GA/jdk16.0.2/d4a915d82b4c4fbb9bde534da945d746/7/GPL/openjdk-16.0.2_windows-x64_bin.zip",
    "jdk_17": "https://download.java.net/java/GA/jdk17.0.2/dfd4a8d0985749f896bed50d7138ee7f/8/GPL/openjdk-17.0.2_windows-x64_bin.zip",
    "jdk_18": "https://download.java.net/java/GA/jdk18.0.1.1/65ae32619e2f40f3a9af3af1851d6e19/2/GPL/openjdk-18.0.1.1_windows-x64_bin.zip",
}
# jdk_list de prueba
"""
jdk_list = {
    "jdk_11": "https://github.com/coreybutler/nvm-windows/releases/download/1.1.9/nvm-setup.zip"
}
"""

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
                exit                            close the program.

                """)
            continue
        elif command.lower() == "exit":
            break
        else:
            print("Error, type a valid command\ntype -h or -help to get a list of commands that can be used.\n")
            continue

        # jdk_name("Aqui elnombre del jdk", "Aqui la extencion del archivo comprimido")
        jdk_name = detect_jdk(jdk[1])

        if jdk_name:
            if jdk[0] == "install":
                install(jdk_name[0], jdk_name[1])
            elif jdk[0] == "use":
                use(jdk_name[0])



def detect_jdk(i):
    i = i.lower()
    file = ".zip"
    if i == "jdk_9" or i == "9" or i == "jdk9" or i == "jdk=9" or i == "jdk@9":
        i = "jdk_9"
        file = ".tar.gz"
    elif i == "jdk_10" or i == "10" or i == "jdk10" or i == "jdk=10" or i == "jdk@10":
        i = "jdk_10"
        file = ".tar.gz"
    elif i == "jdk_11" or i == "11" or i == "jdk11" or i == "jdk=11" or i == "jdk@11":
        i = "jdk_11"
    elif i == "jdk_12" or i == "12" or i == "jdk12" or i == "jdk=12" or i == "jdk@12":
        i = "jdk_12"
    elif i == "jdk_13" or i == "13" or i == "jdk13" or i == "jdk=13" or i == "jdk@13":
        i = "jdk_13"
    elif i == "jdk_14" or i == "14" or i == "jdk14" or i == "jdk=14" or i == "jdk@14":
        i = "jdk_14"
    elif i == "jdk_15" or i == "15" or i == "jdk15" or i == "jdk=15" or i == "jdk@15":
        i = "jdk_15"
    elif i == "jdk_16" or i == "16" or i == "jdk16" or i == "jdk=16" or i == "jdk@16":
        i = "jdk_16"
    elif i == "jdk_17" or i == "17" or i == "jdk17" or i == "jdk=17" or i == "jdk@17":
        i = "jdk_17"
    elif i == "jdk_18" or i == "18" or i == "jdk18" or i == "jdk=18" or i == "jdk@18":
        i = "jdk_18"
    else:
        print("Enter a valid JDK version.")
        return None
    return (i, file)


def ruta():
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.abspath('.')


def install(i, file):
    if os.path.exists(i):
        print("The jdk is already installed.\n")
        return
    else:
        file_name = i + file
        if os.path.exists(file_name):
            os.remove(file_name)
        print("Downloading " + jdk_list[i])
        wget.download(jdk_list[i], file_name)

    print("Extracting...")
    if file == ".zip":
        result = extract_zip(file_name, i)
    else:
        result = extract_tar(file_name, i)

    if result:
        print("Jdk extracted.")

        print("To use the jdk type 'mjdk use " + i + "'\n")


def use(jdk_name):
    if not os.path.exists(jdk_name):
        print("Error, jdk is not installed.")
        return False
    else:
        ruta_jdk = ruta() + "/" + jdk_name
        call("setx JAVA_HOME " + ruta_jdk)
        call("setx PATH %PATH%;%JAVA_HOME%")
        print(jdk_name + "it is now in use.")


def extract_tar(jdk_name, dir):
    if tarfile.is_tarfile():
        z = tarfile.open(jdk_name)
        try:
            z.extractall(dir)
            return True
        except Exception as e:
            print("Error", e)
            return False
        z.close()
    else:
        print("Error, the tar.gz file is not valid.")
        return False


def extract_zip(jdk_name, dir):
    if zipfile.is_zipfile(jdk_name):

        z = zipfile.ZipFile(jdk_name, "r")
        try:
            z.extractall(pwd=None, path=ruta() + "/" + dir + "/")
            return True
        except Exception as e:
            print("Error", e)
            return False
        z.close()

    else:
        print("Error, the zip file is not valid.")
        return False


if __name__ == '__main__':
    run()
