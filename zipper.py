import zipfile
import pathlib


# Function to zip files. 
def archiveCreate(filepaths, destination_folder):

    destination_path = pathlib.Path(destination_folder, "Compressed_files")
    with zipfile.ZipFile(destination_folder, "w") as zip_file:
        for fp in filepaths:
            filepath = pathlib.Path(filepath)
            zip_file.write(fp, archive_name=filepath.name)


