import os
import sys
import wget
import zipfile

# ------------------VARIABLES----------------------------------------------------------
# Variable de JDK para windows.
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
    "jdk_18": "https://download.java.net/java/GA/jdk17.0.2/dfd4a8d0985749f896bed50d7138ee7f/8/GPL/openjdk-17.0.2_windows-x64_bin.zip",
}


# ------------------------------------FUNCIONES--------------------------------------
def run():
    jdk_install = input("Introduce la version JDK a usar:")
    download(jdk_install)


def ruta():
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.abspath('.')


def download(i):
    if i == "jdk_9" or i == "9" or i == "jdk9" or i == "jdk=9" or i == "jdk@9":
        print("Downloading " + jdk_list[i])
        wget.download(jdk_list[i], str(ruta() + "/" + i + ".tar.gz"))
        print("Extracting...")
    elif i == "jdk_10" or i == "10" or i == "jdk10" or i == "jdk=10" or i == "jdk@10":
        print("Downloading " + jdk_list[i])
        wget.download(jdk_list[i], str(ruta() + "/" + i + ".tar.gz"))
        print("Extracting...")

    elif i == "jdk_11" or i == "11" or i == "jdk11" or i == "jdk=11" or i == "jdk@11":
        print("Downloading " + jdk_list[i])
        wget.download(jdk_list[i], str(ruta() + "/" + i + ".zip"))
        print("Extracting...")

    elif i == "jdk_12" or i == "12" or i == "jdk12" or i == "jdk=12" or i == "jdk@12":
        print("Downloading " + jdk_list[i])
        wget.download(jdk_list[i], str(ruta() + "/" + i + ".zip"))
        print("Extracting...")
    elif i == "jdk_13" or i == "13" or i == "jdk13" or i == "jdk=13" or i == "jdk@13":
        print("Downloading " + jdk_list[i])
        wget.download(jdk_list[i], str(ruta() + "/" + i + ".zip"))
        print("Extracting...")
    elif i == "jdk_14" or i == "14" or i == "jdk14" or i == "jdk=14" or i == "jdk@14":
        print("Downloading " + jdk_list[i])
        wget.download(jdk_list[i], str(ruta() + "/" + i + ".zip"))
        print("Extracting...")
    elif i == "jdk_15" or i == "15" or i == "jdk15" or i == "jdk=15" or i == "jdk@15":
        print("Downloading " + jdk_list[i])
        wget.download(jdk_list[i], str(ruta() + "/" + i + ".zip"))
        print("Extracting...")
    elif i == "jdk_16" or i == "16" or i == "jdk16" or i == "jdk=16" or i == "jdk@16":
        print("Downloading " + jdk_list[i])
        wget.download(jdk_list[i], str(ruta() + "/" + i + ".zip"))
        print("Extracting...")
    elif i == "jdk_17" or i == "17" or i == "jdk17" or i == "jdk=17" or i == "jdk@17":
        print("Downloading " + jdk_list[i])
        wget.download(jdk_list[i], str(ruta() + "/" + i + ".zip"))
        print("Extracting...")
    elif i == "jdk_18" or i == "18" or i == "jdk18" or i == "jdk=18" or i == "jdk@18":
        print("Downloading " + jdk_list[i])
        wget.download(jdk_list[i], str(ruta() + "/" + i + ".zip"))
        print("Extracting...")
    else:
        print("Introduce una version JDK valida.")
        print(ruta())
        return


def extraer_zip(jdk_name):
    if zipfile.is_zipfile(jdk_name):

        z = zipfile.ZipFile(jdk_name, "r")
        try:
            z.extractall(pwd=None, path=ruta() + "/" + jdk_name + "/")
        except:
            print('Error')
            pass
        z.close()

    else:
        print("Error, el archivo zip no es valido.")


if __name__ == '__main__':
    run()
