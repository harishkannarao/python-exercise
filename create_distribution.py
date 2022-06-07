from zipfile import ZipFile, ZIP_DEFLATED
import os


def zip_files_in_dir(dir_name, zip_obj):
    for folder, sub_folder, filenames in os.walk(dir_name):
        for filename in filenames:
            zip_obj.write(os.path.join(folder, filename),
                          os.path.relpath(os.path.join(folder, filename), os.path.join(dir_name, '..')))


def zip_file(file_name, zip_obj):
    zip_obj.write(file_name)


with ZipFile('python-exercise.zip', 'w', ZIP_DEFLATED) as zipObj:
    zip_file('main.py', zipObj)
    zip_file('requirements.txt', zipObj)
    zip_files_in_dir('my_module', zipObj)
