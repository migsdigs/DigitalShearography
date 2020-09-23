#File to control basic GUI functions e.g. video pause/play

import tkinter as tk
from tkinter import ttk

class ControlsFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        #Configure self


        #Main Control Frame
        main_control_frame = ttk.Frame(self)
        main_control_frame.grid(row=0, column=0)

        #Inside Main Control Frame
            #Snapshot and New window frame & widgets
        snapshot_frame = ttk.Frame(main_control_frame, padding=15)
        snapshot_frame.grid(row=0, column=0)

        new_window_button = ttk.Button(snapshot_frame, text="New Inspection", state="disabled")   #set command
        new_window_button.grid(row=0, column=0)

        snapshot__button = ttk.Button(snapshot_frame, text="Snapshot Frame", state="disabled")
        snapshot__button.grid(row=0, column=1)


            #Video Controls Frame and Buttons
        video_controls_frame = ttk.Frame(main_control_frame, padding=15)
        video_controls_frame.grid(row=0, column=1)

        self.play_button = ttk.Button(video_controls_frame, text="Play", command=controller.play, state="disabled")   
        self.play_button.grid(row=0, column=0)

        self.pause_button = ttk.Button(video_controls_frame, text="Pause", command=controller.pause, state="disabled")  
        self.pause_button.grid(row=0, column=1)

        self.stop_button = ttk.Button(video_controls_frame, text="Stop", command = controller.stop, state="disabled")    
        self.stop_button.grid(row=0, column=2)


            #Real Time Video/Fringe Pattern Frame and Buttons
        video_mode_frame = ttk.Frame(main_control_frame, padding=20)
        video_mode_frame.grid(row=0, column=2)

        real_time_video_button = ttk.Button(video_mode_frame, text="Video Mode", state="disabled")
        real_time_video_button.grid(row=0, column=0)

        fringe_pattern_button = ttk.Button(video_mode_frame, text="Fringe Pattern Mode", state="disabled")
        fringe_pattern_button.grid(row=0, column=1)


            #Initialisation File Import
        initialisation_frame = ttk.Frame(main_control_frame, padding = 20)
        initialisation_frame.grid(row=0, column=3)

        import_file_path_label = ttk.Label(initialisation_frame, text="Initialisation file path", padding=10)
        import_file_path_label.grid(row=0, column=0)

        file_path = tk.StringVar()
        import_entry = ttk.Entry(initialisation_frame, width=20, textvariable=file_path, text="file path")
        import_entry.grid(row=0, column=1)

        import_button = ttk.Button(initialisation_frame, text="Import Initialisation Folder")    #set command
        import_button.grid(row=0, column=2)




