from zipfile import ZipFile, ZIP_DEFLATED
import os


def zip_files_in_dir(dir_name, zip_obj):
    for folder, sub_folder, filenames in os.walk(dir_name):
        for filename in filenames:
            file_name = str(os.path.join(folder, filename))
            zip_obj.write(
                file_name, os.path.relpath(file_name, os.path.join(dir_name, ".."))
            )


def zip_file(file_name, zip_obj):
    zip_obj.write(file_name)


def main():
    with ZipFile("python-exercise.zip", "w", ZIP_DEFLATED) as zipObj:
        zip_file("main.py", zipObj)
        zip_file("requirements.txt", zipObj)
        zip_files_in_dir("app", zipObj)


if __name__ == "__main__":
    main()
