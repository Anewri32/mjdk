import os
import sys
import wget
import zipfile
import tarfile

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
    pass
    


def ruta():
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.abspath('.')


def install():
    i = input("Enter the JDK version to install:")
    
    
    file = "zip"
    if i == "jdk_9" or i == "9" or i == "jdk9" or i == "jdk=9" or i == "jdk@9":
        file = "tar.gz"
    elif i == "jdk_10" or i == "10" or i == "jdk10" or i == "jdk=10" or i == "jdk@10":
        file = "tar.gz"
    elif i == "jdk_11" or i == "11" or i == "jdk11" or i == "jdk=11" or i == "jdk@11":
        pass
    elif i == "jdk_12" or i == "12" or i == "jdk12" or i == "jdk=12" or i == "jdk@12":
        pass
    elif i == "jdk_13" or i == "13" or i == "jdk13" or i == "jdk=13" or i == "jdk@13":
        pass
    elif i == "jdk_14" or i == "14" or i == "jdk14" or i == "jdk=14" or i == "jdk@14":
        pass
    elif i == "jdk_15" or i == "15" or i == "jdk15" or i == "jdk=15" or i == "jdk@15":
        pass
    elif i == "jdk_16" or i == "16" or i == "jdk16" or i == "jdk=16" or i == "jdk@16":
        pass
    elif i == "jdk_17" or i == "17" or i == "jdk17" or i == "jdk=17" or i == "jdk@17":
        pass
    elif i == "jdk_18" or i == "18" or i == "jdk18" or i == "jdk=18" or i == "jdk@18":
        pass
    else:
        print("Enter a valid JDK version.")
        return

    print("Downloading " + jdk_list[i])
    path_file = ruta() + "/" + i + file
    wget.download(jdk_list[i], path_file)

    print("Extracting...")
    if file == "zip":
        result = extract_zip(path_file, i)
    else:
        result = extract_tar(path_file, i)

    if result:
        print("Extracted file.\n")

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
