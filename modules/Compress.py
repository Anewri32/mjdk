import zipfile
import tarfile


def extract_tar(file, path):
    z = tarfile.open(file)
    try:
        z.extractall(path)
        z.close()
        return True
    except Exception as e:
        print("Error", e)
        z.close()
        return False


def extract_zip(file, path):
    z = zipfile.ZipFile(file, "r")
    try:
        z.extractall(pwd=None, path=path)
        z.close()
        return True
    except Exception as e:
        print("Error", e)
        z.close()
        return False
