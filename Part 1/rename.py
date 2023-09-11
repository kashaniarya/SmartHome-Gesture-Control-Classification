import os

def rename_videos(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"): # or filename.endswith(".avi") or filename.endswith(".mkv"):
            new_filename = filename.split(".")[0] + "_KASHANI." + filename.split(".")[1]
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))


folder_path = "C:/Users/Arya Kashani/Documents/ASU/CSE535-MobileApplications/Kashani_Arya_Gestures"
rename_videos(folder_path)
