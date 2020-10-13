#Imports
import tkinter as tk
from tkinter import ttk
from frames import VideoFrame, ControlsFrame, SetupFrame

from controller import Controller
import PyCapture2


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
        super().__init__(*args, **kwargs)  
        
        self.controller = None                                                                 #use inheritance of tk.Tk class
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        #Configurations of the Root
        self.title("Digital Shearography - Project 55")                                                     #title of application
        self.geometry("{}x{}+0+0".format(screen_width, screen_height))              #set the size of the window to fullscreen by default

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        #Themes and Styling
        style = ttk.Style(self)
        #style.theme_use("clam")

        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure("TimerText.TLabel", background=COLOUR_LIGHT_BACKGROUND, foreground=COLOUR_DARK_TEXT, font="Courier 38")


        #Main Container to Hold the Class Frames (video, control and setup)
        main_container = ttk.Frame(self)
        main_container.grid(row=0, column=0)
        main_container.columnconfigure(0, weight=2)
        main_container.columnconfigure(1, weight=1)

        main_container.rowconfigure(0, weight=1)        #play around this
        main_container.rowconfigure(1, weight=7)


        #Frames inside main container
        self.controls_frame = ControlsFrame(main_container, controller)
        self.controls_frame.grid(row=0, column=0, columnspan=2, pady=(10), sticky="NSEW")

        self.video_frame = VideoFrame(main_container, screen_width, screen_height, c, 33)   #pass in parent frame, screen height & width, camera object and delay between refreshing video
        self.video_frame.grid(row=1, column=0, pady=(30), padx=(30), sticky="NSEW")
        self.video_frame.display_video()


        self.setup_frame = SetupFrame(main_container, controller)
        self.setup_frame.grid(row=1, column=1, pady=(30), padx=(30), sticky="NSEW")

    def set_controller(self, controller):   #pass in Controller class as the controller 
        self.controller = controller
        controller.set_video_frame(self.video_frame)
        controller.set_controls_frame(self.controls_frame)
        controller.set_setup_frame(self.setup_frame)
    

    
###################################################################################################################     
###################################################################################################################

######################### CAMERA SETUP #########################

bus = PyCapture2.BusManager()
num_cams = bus.getNumOfCameras()
print('Number of cameras detected:', num_cams)
if not num_cams:
    print('Insufficient number of cameras. Exiting...')
    exit()

# Select camera on 0th index
c = PyCapture2.Camera()             #Assign Camera object to C
uid = bus.getCameraFromIndex(0)     #select camera on 0th index
c.connect(uid)                      #connect camera object to physical camera

# Disable On-board Image Processing
c.setProperty(type = PyCapture2.PROPERTY_TYPE.AUTO_EXPOSURE, onOff = False)  #Disable/Enable Auto Exposure


print('Starting image capture...')
c.startCapture()

###################################################################################################################     
###################################################################################################################

controller = Controller()           #create object controller of the Controller() class
app = DS_GUI()
app.set_controller(controller)
app.mainloop()

try:
    c.stopCapture()
    print("stopping capture")
    c.disconnect()
    print("camera disconnected")

except:
    exit()
