import tkinter as tk
from tkinter import ttk

class ControlsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #Configure self


        #Main Control Frame
        main_control_frame = ttk.Frame(self)
        main_control_frame.grid(row=0, column=0)

        #Inside Main Control Frame
            #Snapshot and New window frame & widgets
        snapshot_frame = ttk.Frame(main_control_frame, padding=15)
        snapshot_frame.grid(row=0, column=0)

        new_window_button = ttk.Button(snapshot_frame, text="New Inspection")   #set command
        new_window_button.grid(row=0, column=0)

        snapshot__button = ttk.Button(snapshot_frame, text="Snapshot Frame")
        snapshot__button.grid(row=0, column=1)


            #Video Controls Frame and Buttons
        video_controls_frame = ttk.Frame(main_control_frame, padding=15)
        video_controls_frame.grid(row=0, column=1)

        play_button = ttk.Button(video_controls_frame, text="Play")   #set command
        play_button.grid(row=0, column=0)

        pause__button = ttk.Button(video_controls_frame, text="Pause")  #set command
        pause__button.grid(row=0, column=1)

        stop__button = ttk.Button(video_controls_frame, text="Stop")    #set command
        stop__button.grid(row=0, column=2)


            #Initialisation File Import
        initialisation_frame = ttk.Frame(main_control_frame, padding = 30)
        initialisation_frame.grid(row=0, column=2)

        import_file_path_label = ttk.Label(initialisation_frame, text="Initialisation file path", padding=10)
        import_file_path_label.grid(row=0, column=0)

        file_path = tk.StringVar()
        import_entry = ttk.Entry(initialisation_frame, width=20, textvariable=file_path, text="file path")
        import_entry.grid(row=0, column=1)

        import_button = ttk.Button(initialisation_frame, text="Import Initialisation Folder")    #set command
        import_button.grid(row=0, column=2)




