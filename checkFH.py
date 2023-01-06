"""
Copy ảnh qua file chạy của FH để test lỗi dựa vào máy ngoại quan
"""

import os
import shutil
import glob
# import PySimleGUI as sg
import PySimpleGUI as sg
import os.path

# First the window layout in 2 columns

# file_list_column = [
#     [
#         sg.Text("Image Folder"),
#         sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
#         sg.FolderBrowse(),
#     ],
# ]

# # For now will only show the name of the file that was chosen
# image_viewer_column = [
#     [sg.Text("Choose an image from list on left:")],
#     [sg.Text(size=(40, 1), key="-TOUT-")],
#     [sg.Image(key="-IMAGE-")],
# ]

# # ----- Full layout -----
# layout = [
#     [
#         sg.Column(file_list_column),
#         sg.VSeperator(),
#     ]
# ]

# window = sg.Window("Image Viewer", layout)

# # Run the Event Loop
# while True:
#     event, values = window.read()
#     if event == "Exit" or event == sg.WIN_CLOSED:
#         break
#     # Folder name was filled in, make a list of files in the folder
#     if event == "-FOLDER-":
#         folder = values["-FOLDER-"]
#             # Get list of files in folder
#         file_list = os.listdir(folder)


# window.close()

check_path = "C:\\Users\\vnmuser\\Desktop\\DUYLOC\\lib\\yolov5\\runs\\detect\\CHECK-LOI-OKK-CAM_1-A93\\me\\images"
original_path = "C:\\Users\\vnmuser\\Desktop\\DUYLOC\\Report\\images\\A93\\NG\\CAM_1\\OKK"
save_path = "C:\\Users\\vnmuser\\Documents\\OMRON FZ\\RAMDisk\\checkFH\\"

for file in glob.glob(save_path + "*.bmp"):
    os.remove(file)

for i in os.listdir(check_path):
    shutil.copy(os.path.join(original_path,i),os.path.join(save_path,i))


