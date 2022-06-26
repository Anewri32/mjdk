import os

import wget
import hashlib

def download_file(file_to_download, path_to_file):
    if os.path.exists(path_to_file):
        os.remove(path_to_file)
    print("Downloading " + file_to_download)
    wget.download(file_to_download, path_to_file)
    print("Downloaded file")

def SHA256_Checksum(ruta):
    h = hashlib.sha256()
    with open(ruta, 'rb', buffering=0) as f:
        for b in iter(lambda : f.read(128*1024), b''):
            h.update(b)
    return h.hexdigest()

def Check_SHA256_With_File(file, sha256):
    if sha256.__contains__("http"):
        url = sha256
        temp_file_name = "sha256Temp.sha256"
        download_file(url, temp_file_name)

    temp_file = open(temp_file_name, "r")
    sha256 = temp_file.read()
    temp_file.close()
    os.remove(temp_file_name)

    file_sha256 = SHA256_Checksum(file)
    if file_sha256.__eq__(sha256):
        return True
    else:
        return False
