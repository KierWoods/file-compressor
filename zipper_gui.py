import PySimpleGUI as gui
from zipper import archiveCreate


label = gui.Text("Choose File to compress:  ")
input_one = gui.Input()
upload_button_one = gui.FilesBrowse("Select", key="file")


label2 = gui.Text("Choose Destination Folder:")
input_two = gui.Input()
upload_button_two = gui.FolderBrowse("Select", key="folder")

exe_button = gui.Button("Execute")
complete_label = gui.Text(key="complete")


window = gui.Window("File compression App",
layout=[[label,input_one, upload_button_one],
[label2,input_two, upload_button_two],[exe_button], [complete_label]])


while True:
    event, values = window.read()
    print(event, values)

    filepaths = values["file"].split(";")
    folder = values["folder"]

    # Call function from zipper. 
    archiveCreate(filepaths, folder)
    window["complete"].update(value="Files Compressed!")
window.close()
