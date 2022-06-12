import wget


def file(file_to_download, path_to_file):
    print("Downloading " + file_to_download)
    wget.download(file_to_download, path_to_file)
    print("Downloaded file")
