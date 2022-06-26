import os
import subprocess


def setx_var(var_name, var_value):
    filename = "setxVar.bat"
    file = open(filename, "w")
    file.write('setx ' + var_name + ' "' + var_value + '"')
    file.close()
    subprocess.run(filename)
    os.remove(filename)


def setx_add_path(path_value):
    filename = "setxAddPath.bat"
    file = open(filename, "w")
    file.write('setx PATH "%PATH%";"' + path_value + '"')
    file.close()
    subprocess.run(filename)
    os.remove(filename)
