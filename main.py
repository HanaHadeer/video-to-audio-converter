import os

import moviepy.editor
from tkinter.filedialog import *
import tkinter as tk
from tkinter import font, filedialog, ttk, messagebox
import re  # to convert one slash to double slash


def convert_to_audio():
    video = askopenfilename()
    if video:
        video = moviepy.editor.VideoFileClip(video)

        audio = video.audio
        audio_name = entry.get() + '.mp3'
        audio.write_audiofile(audio_name)
        # audio.write_audiofile('audio.mp3')
        folder_selected = filedialog.askdirectory()

        if folder_selected:
            # print(folder_selected)
            fol_sel = re.sub('/', '//', folder_selected)
            # print(fol_sel)
            source = audio_name
            save_dir = fol_sel + '//' + audio_name
            os.replace(source, save_dir)
            messagebox.showinfo("Success", f"Audio successfully saved at:\n{save_dir}")
        else:
            messagebox.showwarning("Warning", "No folder selected. Audio not saved.")
    else:
        messagebox.showwarning("Warning", "No video selected. Conversion cancelled.")


# UI Window
window = tk.Tk()
window.title('Video to Audio Converter')
window.geometry("500x300")
window.resizable(False, False)

# Style
style = ttk.Style(window)
style.configure('TLabel', font=('Arial', 15))
style.configure('TButton', font=('Helvetica', 12, 'bold'), padding=10)
style.configure('TEntry', font=('Helvetica', 12))

# Title
title_label = ttk.Label(window, text="Video to Audio Converter", font=("Arial", 25, "bold"), foreground="blue")
title_label.pack(pady=20)

# Audio Name Entry
entry_label = ttk.Label(window, text="Enter Audio File Name (without extension):")
entry_label.pack(pady=5)

entry = ttk.Entry(window)
entry.insert(0, 'audio_1')
entry.pack(pady=5)

# Convert Button
convert_button = ttk.Button(window, text="Select Video and Convert", command=convert_to_audio)
convert_button.pack(pady=20)

# Status Label
status_label = ttk.Label(window, text="", font=("Arial", 12))
status_label.pack(pady=5)

window.mainloop()
