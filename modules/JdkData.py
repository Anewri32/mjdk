
class JDK:
    def __init__(self):
        self.__jdk_versions_urls = {
            "9": {
                "9": ("https://download.java.net/java/GA/jdk9/9.0.4/binaries/openjdk-9.0.4_windows-x64_bin.tar.gz",
                      "https://download.java.net/java/GA/jdk9/9.0.4/binaries/openjdk-9.0.4_windows-x64_bin.tar.gz.sha256"),
                "9.0.4": ("https://download.java.net/java/GA/jdk9/9.0.4/binaries/openjdk-9.0.4_windows-x64_bin.tar.gz",
                          "https://download.java.net/java/GA/jdk9/9.0.4/binaries/openjdk-9.0.4_windows-x64_bin.tar.gz.sha256")
            },
            "10": {
                "10": ("https://download.java.net/java/GA/jdk10/10/binaries/openjdk-10_windows-x64_bin.tar.gz",
                       "https://download.java.net/java/GA/jdk10/10/binaries/openjdk-10_windows-x64_bin.tar.gz.sha256"),
                "10.0.1": (
                "https://download.java.net/java/GA/jdk10/10.0.1/fb4372174a714e6b8c52526dc134031e/10/openjdk-10.0.1_windows-x64_bin.tar.gz",
                "https://download.java.net/java/GA/jdk10/10.0.1/fb4372174a714e6b8c52526dc134031e/10/openjdk-10.0.1_windows-x64_bin.tar.gz.sha256"),
                "10.0.2": (
                "https://download.java.net/java/GA/jdk10/10.0.2/19aef61b38124481863b1413dce1855f/13/openjdk-10.0.2_windows-x64_bin.tar.gz",
                "https://download.java.net/java/GA/jdk10/10.0.2/19aef61b38124481863b1413dce1855f/13/openjdk-10.0.2_windows-x64_bin.tar.gz.sha256")
            },
            "11": {
                "11": ("https://download.java.net/java/ga/jdk11/openjdk-11_windows-x64_bin.zip",
                       "https://download.java.net/java/ga/jdk11/openjdk-11_windows-x64_bin.zip.sha256"),
                "11.0.1": ("https://download.java.net/java/GA/jdk11/13/GPL/openjdk-11.0.1_windows-x64_bin.zip",
                           "https://download.java.net/java/GA/jdk11/13/GPL/openjdk-11.0.1_windows-x64_bin.zip.sha256"),
                "11.0.2": ("https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_windows-x64_bin.zip",
                           "https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_windows-x64_bin.zip.sha256")
            },
            "12": {
                "12": ("https://download.java.net/java/GA/jdk12/33/GPL/openjdk-12_windows-x64_bin.zip",
                       "https://download.java.net/java/GA/jdk12/33/GPL/openjdk-12_windows-x64_bin.zip.sha256"),
                "12.0.1": (
                "https://download.java.net/java/GA/jdk12.0.1/69cfe15208a647278a19ef0990eea691/12/GPL/openjdk-12.0.1_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk12.0.1/69cfe15208a647278a19ef0990eea691/12/GPL/openjdk-12.0.1_windows-x64_bin.zip.sha256"),
                "12.0.2": (
                "https://download.java.net/java/GA/jdk12.0.2/e482c34c86bd4bf8b56c0b35558996b9/10/GPL/openjdk-12.0.2_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk12.0.2/e482c34c86bd4bf8b56c0b35558996b9/10/GPL/openjdk-12.0.2_windows-x64_bin.zip.sha256")
            },
            "13": {
                "13": (
                "https://download.java.net/java/GA/jdk13/5b8a42f3905b406298b72d750b6919f6/33/GPL/openjdk-13_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk13/5b8a42f3905b406298b72d750b6919f6/33/GPL/openjdk-13_windows-x64_bin.zip.sha256"),
                "13.0.1": (
                "https://download.java.net/java/GA/jdk13.0.1/cec27d702aa74d5a8630c65ae61e4305/9/GPL/openjdk-13.0.1_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk13.0.1/cec27d702aa74d5a8630c65ae61e4305/9/GPL/openjdk-13.0.1_windows-x64_bin.zip.sha256"),
                "13.0.2": (
                "https://download.java.net/java/GA/jdk13.0.2/d4173c853231432d94f001e99d882ca7/8/GPL/openjdk-13.0.2_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk13.0.2/d4173c853231432d94f001e99d882ca7/8/GPL/openjdk-13.0.2_windows-x64_bin.zip.sha256")
            },
            "14": {
                "14": (
                "https://download.java.net/java/GA/jdk14/076bab302c7b4508975440c56f6cc26a/36/GPL/openjdk-14_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk14/076bab302c7b4508975440c56f6cc26a/36/GPL/openjdk-14_windows-x64_bin.zip.sha256"),
                "14.0.1": (
                "https://download.java.net/java/GA/jdk14.0.1/664493ef4a6946b186ff29eb326336a2/7/GPL/openjdk-14.0.1_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk14.0.1/664493ef4a6946b186ff29eb326336a2/7/GPL/openjdk-14.0.1_windows-x64_bin.zip.sha256"),
                "14.0.2": (
                "https://download.java.net/java/GA/jdk14.0.2/205943a0976c4ed48cb16f1043c5c647/12/GPL/openjdk-14.0.2_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk14.0.2/205943a0976c4ed48cb16f1043c5c647/12/GPL/openjdk-14.0.2_windows-x64_bin.zip.sha256")
            },
            "15": {
                "15": (
                "https://download.java.net/java/GA/jdk15/779bf45e88a44cbd9ea6621d33e33db1/36/GPL/openjdk-15_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk15/779bf45e88a44cbd9ea6621d33e33db1/36/GPL/openjdk-15_windows-x64_bin.zip.sha256"),
                "15.0.1": (
                "https://download.java.net/java/GA/jdk15.0.1/51f4f36ad4ef43e39d0dfdbaf6549e32/9/GPL/openjdk-15.0.1_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk15.0.1/51f4f36ad4ef43e39d0dfdbaf6549e32/9/GPL/openjdk-15.0.1_windows-x64_bin.zip.sha256"),
                "15.0.2": (
                "https://download.java.net/java/GA/jdk15.0.2/0d1cfde4252546c6931946de8db48ee2/7/GPL/openjdk-15.0.2_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk15.0.2/0d1cfde4252546c6931946de8db48ee2/7/GPL/openjdk-15.0.2_windows-x64_bin.zip.sha256")
            },
            "16": {
                "16": (
                "https://download.java.net/java/GA/jdk16/7863447f0ab643c585b9bdebf67c69db/36/GPL/openjdk-16_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk16/7863447f0ab643c585b9bdebf67c69db/36/GPL/openjdk-16_windows-x64_bin.zip.sha256"),
                "16.0.1": (
                "https://download.java.net/java/GA/jdk16.0.1/7147401fd7354114ac51ef3e1328291f/9/GPL/openjdk-16.0.1_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk16.0.1/7147401fd7354114ac51ef3e1328291f/9/GPL/openjdk-16.0.1_windows-x64_bin.zip.sha256"),
                "16.0.2": (
                "https://download.java.net/java/GA/jdk16.0.2/d4a915d82b4c4fbb9bde534da945d746/7/GPL/openjdk-16.0.2_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk16.0.2/d4a915d82b4c4fbb9bde534da945d746/7/GPL/openjdk-16.0.2_windows-x64_bin.zip.sha256")
            },
            "17": {
                "17": (
                "https://download.java.net/java/GA/jdk17/0d483333a00540d886896bac774ff48b/35/GPL/openjdk-17_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk17/0d483333a00540d886896bac774ff48b/35/GPL/openjdk-17_windows-x64_bin.zip.sha256"),
                "17.0.1": (
                "https://download.java.net/java/GA/jdk17.0.1/2a2082e5a09d4267845be086888add4f/12/GPL/openjdk-17.0.1_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk17.0.1/2a2082e5a09d4267845be086888add4f/12/GPL/openjdk-17.0.1_windows-x64_bin.zip.sha256"),
                "17.0.2": (
                "https://download.java.net/java/GA/jdk17.0.2/dfd4a8d0985749f896bed50d7138ee7f/8/GPL/openjdk-17.0.2_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk17.0.2/dfd4a8d0985749f896bed50d7138ee7f/8/GPL/openjdk-17.0.2_windows-x64_bin.zip.sha256")
            },
            "18": {
                "18": (
                "https://download.java.net/java/GA/jdk18/43f95e8614114aeaa8e8a5fcf20a682d/36/GPL/openjdk-18_windows-x64_bin.zip",
                "https://download.java.net/java/GA/jdk18/43f95e8614114aeaa8e8a5fcf20a682d/36/GPL/openjdk-18_windows-x64_bin.zip.sha256")
            }
        }

    def __extaer_prefijo_jdk(self, command_jdk):
        return command_jdk.removeprefix("jdk=").removeprefix("jdk@").removeprefix("jdk")

    def detect_jdk(self, jdk):
        jdk = self.__extaer_prefijo_jdk(jdk)
        for key1, value1 in self.__jdk_versions_urls.items():
            if key1 in jdk:
                for key2, value2 in value1.items():
                    if key2.__eq__(jdk):
                        if ".tar.gz" in value2[0]:
                            exctention = ".tar.gz"
                        elif ".zip" in value2[0]:
                            exctention = ".zip"
                        # 0 = JDK-versions, 1 = url, 2 = jdk-name, 3 = extencion of file to download and descompress.
                        return (key2, value2, "jdk-" + key2, exctention)
        print("Error, JDK version not found")

    def jdk_list(self):
        print("JDK list available to download and install")
        for value in self.__jdk_versions_urls.values():
            for key in value.keys():
                print("jdk-" + key)
        print("")
