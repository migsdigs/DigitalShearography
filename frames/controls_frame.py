# Imports
import tkinter as tk
from tkinter import ttk

class ControlsFrame(ttk.Frame):     #create a class of type ttk.Frame
    def __init__(self, parent, controller): #initialise the class
        super().__init__(parent)    #call the constructor of the ttk.Frame
                                    #class to inherit its and the parent's
                                    #properties

        # Main Control Frame
        main_control_frame = ttk.Frame(self)
        main_control_frame.grid(row=0, column=0)

        # Inside Main Control Frame
            #Snapshot and New window frame & widgets
        snapshot_frame = ttk.Frame(main_control_frame, padding=15)
        snapshot_frame.grid(row=0, column=0)

        # New Inspection button
        self.new_inspection_button = ttk.Button(snapshot_frame, text="New Inspection", state="disabled", command=controller.reset)   
        self.new_inspection_button.grid(row=0, column=0)

        # Snapshot Frame button
        self.snapshot_button = ttk.Button(snapshot_frame, text="Snapshot Frame", state="enabled", command=controller.save_snapshot)
        self.snapshot_button.grid(row=0, column=1)


            #V ideo Controls Frame and Buttons
        video_controls_frame = ttk.Frame(main_control_frame, padding=15)
        video_controls_frame.grid(row=0, column=1)

        # Play button
        self.play_button = ttk.Button(video_controls_frame, text="Play", command=controller.play, state="disabled")   
        self.play_button.grid(row=0, column=0)

        # Pause button
        self.pause_button = ttk.Button(video_controls_frame, text="Pause", command=controller.pause, state="disabled")  
        self.pause_button.grid(row=0, column=1)

        # Stop button
        self.stop_button = ttk.Button(video_controls_frame, text="Stop", command = controller.stop, state="disabled")    
        self.stop_button.grid(row=0, column=2)


            # Real Time Video/Fringe Pattern Frame and Buttons
        video_mode_frame = ttk.Frame(main_control_frame, padding=20)
        video_mode_frame.grid(row=0, column=2)

        # Video Mode button
        self.real_time_video_button = ttk.Button(video_mode_frame, text="Video Mode", state="disabled", command = controller.display_video)
        self.real_time_video_button.grid(row=0, column=0)

        # Fringe Pattern Mode button
        self.fringe_pattern_button = ttk.Button(video_mode_frame, text="Fringe Pattern Mode", state="disabled", command = controller.display_fringes)
        self.fringe_pattern_button.grid(row=0, column=1)


            # Images folder (enter directory location for saved images)
        image_folder_frame = ttk.Frame(main_control_frame, padding=20)
        image_folder_frame.grid(row=0, column=3)

        # Image Folder label
        image_folder_label = ttk.Label(image_folder_frame, text="Image Save Location")
        image_folder_label.grid(row=0, column=0)

        # Image Folder Entry
        self.folder_directory = tk.StringVar()
        self.folder_entry = ttk.Entry(image_folder_frame, width=20, textvariable = self.folder_directory)
        self.folder_entry.grid(row=1, column=0)

        # Set Folder button
        self.folder_set_button = ttk.Button(image_folder_frame, text="Set Folder", command = controller.get_save_location)    
        self.folder_set_button.grid(row=1, column=1)


            # Initialisation File Import
        initialisation_frame = ttk.Frame(main_control_frame, padding = 20)
        initialisation_frame.grid(row=0, column=4)

        # Initialisation File label
        import_config_file_label = ttk.Label(initialisation_frame, text="Initialisation file")
        import_config_file_label.grid(row=0, column=0)

        # Import config button
        self.config_button = ttk.Button(initialisation_frame, text="Import Config File", command=controller.set_config)    
        self.config_button.grid(row=1, column=0)




