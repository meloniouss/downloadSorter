import os
import shutil

path = "C:/Users/fireh/Downloads/"
files = os.listdir(path)
for file in files:
    if ".pdf" in file and not os.path.exists(path + "PDFs/" + file):
        shutil.move(path + file, path + "PDFs/" + file)
    elif ".jpg" in file and not os.path.exists(path + "Images/" + file):
        shutil.move(path + file, path + "Images/" + file)
    elif ".png" in file and not os.path.exists(path + "Images/" + file):
        shutil.move(path + file, path + "Images/" + file)
    elif ".docx" in file and not os.path.exists(path + "Docs/" + file):
        shutil.move(path + file, path + "Docs/" + file)
    elif ".txt" in file and not os.path.exists(path + "Docs/" + file):
        shutil.move(path + file, path + "Docs/" + file)
    elif ".csv" in file and not os.path.exists(path + "Excels/" + file):
        shutil.move(path + file, path + "Excels/" + file)
    elif ".exe" in file and not os.path.exists(path + "Executables/" + file):
        shutil.move(path + file, path + "Executables/" + file)
    elif ".mov" in file and not os.path.exists(path + "Videos/" + file):
        shutil.move(path+file, path + "Videos/" + file)
    elif ".mp4" in file and not os.path.exists(path + "Videos/" + file):
        shutil.move(path+file, path + "Videos/" + file)
    elif ".wmv" in file and not os.path.exists(path + "Videos/" + file):
        shutil.move(path+file, path + "Videos/" + file)
    elif ".avi" in file and not os.path.exists(path + "Videos/" + file):
        shutil.move(path+file, path + "Videos/" + file)
    elif ".zip" in file and not os.path.exists(path + "Zips/" + file):
        shutil.move(path+file, path + "Zips/" + file)
    elif ".rar" in file and not os.path.exists(path + "Zips/" + file):
        shutil.move(path + file, path + "Zips/" + file)
    elif ".webp" in file and not os.path.exists(path + "random webpages i downloaded on accident/" + file):
        shutil.move(path + file, path + "random webpages i downloaded on accident/" + file)
    elif ".html" in file and not os.path.exists(path + "random webpages i downloaded on accident/" + file):
        shutil.move(path + file, path + "random webpages i downloaded on accident/" + file)
