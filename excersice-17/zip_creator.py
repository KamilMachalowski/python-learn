import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    with zipfile.ZipFile(pathlib.Path(dest_dir, "compressed.zip"), "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


# test for only to check if the function works - when this file is execute alone
if __name__ == "__main__":
    make_archive(filepaths=["compores_files.py"], dest_dir="compressed")