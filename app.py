#Imports
import tkinter as tk
from tkinter import ttk
from frames import VideoFrame, ControlsFrame, SetupFrame

#GLOBALS

#Colours
COLOUR_PRIMARY = "#2e3f4f"          #looks at Tkinter resources for colour codes
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


#Class for Root of application
class DS_GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)                                                                   #use inheritance of tk.Tk class

        #Configurations of the Root
        self.title("Digital Shearography - Project 55")                                                     #title of application
        self.geometry("{}x{}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))              #set the size of the window to fullscreen by default

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        #Themes and Styling
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure("TimerText.TLabel", background=COLOUR_LIGHT_BACKGROUND, foreground=COLOUR_DARK_TEXT, font="Courier 38")


        #Main Container to Hold the Main Frames (video, control and setup)
        main_container = ttk.Frame(self)
        main_container.grid(row=0, column=0)
        main_container.columnconfigure(0, weight=2)
        main_container.columnconfigure(1, weight=1)



        #Frames inside main container
        controls_frame = ControlsFrame(main_container)
        controls_frame.grid(row=0, column=0, columnspan=2, pady=(10), sticky="NSEW")

        video_frame = VideoFrame(main_container)
        video_frame.grid(row=1, column=0, pady=(30), padx=(30), sticky="NSEW")

        setup_frame = SetupFrame(main_container)
        setup_frame.grid(row=1, column=1, pady=(30), padx=(30), sticky="NSEW")



app = DS_GUI()
app.mainloop()
