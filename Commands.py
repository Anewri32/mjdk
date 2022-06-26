import os
import sys
from modules import VarEnvironment, Download, Compress, JdkData


class Command:
    def __init__(self):
        self.__jdk_data = JdkData.JDK

    def detect_Command(self, command):
        if "install " in command.lower():
            jdk = command.removeprefix("install ").removeprefix("INSTALL ")
            self.__install(jdk)
            return True
        elif "use " in command.lower():
            jdk = command.removeprefix("use ").removeprefix("USE ")
            self.__use(jdk)
            return True
        elif "uninstall " in command.lower():
            jdk = command.removeprefix("uninstall ").removeprefix("UNINSTALL     ")
            self.__uninstall(jdk)
            return True
        elif command.lower().__eq__("list"):
            self.__list()
            return True
        elif command.__eq__("-h") or command.__eq__("--h") or command.__eq__("-help") or command.__eq__("--help"):
            self.__help()
            return True
        elif command.lower().__eq__("exit"):
            return False
        else:
            print("Error, type a valid command\ntype -h or -help to get a list of commands that can be used.\n")
            return True

    def __install(self, jdk):
        jdk = self.__jdk_data.detect_jdk(jdk)
        jdk_path = self.__ruta() + "\\" + jdk[2]
        jdk_path_file = jdk_path + jdk[3]
        if os.path.exists(jdk_path):
            print("The jdk is already installed.\n")
            return
        else:
            if os.path.exists(jdk_path_file):
                os.remove(jdk_path_file)
            Download.download_file(jdk[1][0], jdk_path_file)
            if Download.Compare_SHA256(jdk_path_file, jdk[1][1]) is False:
                print("Error, fail SHA256 check")
                return
        print("Extracting...")
        if jdk[3].__eq__(".zip"):
            result = Compress.extract_zip(jdk_path_file, self.__ruta())
        elif jdk[3].__eq__(".tar.gz"):
            result = Compress.extract_tar(jdk_path_file, self.__ruta())
        if result:
            print("Jdk extracted.")
            print("To use the jdk type 'mjdk use " + jdk[0] + "'\n")

    def __use(self, jdk):
        jdk = self.__jdk_data.detect_jdk(jdk)
        jdk_path = self.__ruta() + "\\" + jdk[2]
        if not os.path.exists(jdk_path):
            print("Error, jdk is not installed.")
        else:
            VarEnvironment.setx_var("JAVA_HOME", jdk_path)
            VarEnvironment.setx_add_path("%JAVA_HOME%\\bin")
            print(jdk[2] + " it is now in use.\n")

    def __uninstall(self, jdk):
        jdk = self.__jdk_data.detect_jdk(jdk)
        jdk_path = self.__ruta() + "\\" + jdk[2]
        if os.path.exists(jdk_path):
            print("Uninstalling " + jdk[2])
            os.remove(jdk_path)
            VarEnvironment.setx_var("JAVA_HOME", "")
            print(jdk[2] + " removed")
        else:
            print("Error, " + jdk[2] + " is not installed")

    def __list(self):
        self.__jdk_data.jdk_list()

    def __help(self):
        print("""
                        install [jdk-version]           Allows to download the jdk, needs to be specified the version.
                        use [jdk-version]               Sets the jdk to use, needs the version to be specified.
                        exit                            Close the program.
                        uninstall [jdk-version]         Remove the jdk selected
                        list                            Show all jdk versions available to install.

                        """)

    def __ruta(self):
        if hasattr(sys, '_MEIPASS'):
            return sys._MEIPASS
        return os.path.abspath('modules')
