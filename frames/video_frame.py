import tkinter as tk
from tkinter import ttk

class VideoFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #Frames
        video_frame = ttk.Frame(self)
        video_frame.grid()

        #Labels
        video_display_label = ttk.Label(video_frame, text="Video Display")
        video_display_label.grid(row=0, column=0, sticky="NSEW")