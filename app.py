#Imports
import tkinter as tk
from tkinter import ttk
from frames import VideoFrame, ControlsFrame, SetupFrame

from controller import Controller
import PyCapture2

#Set DPI awareness (needed for some newer screens)
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


#Class for Root of application
class DS_GUI(tk.Tk):                        #create a class of type Tk class
    def __init__(self, *args, **kwargs):    #initialise the class
        super().__init__(*args, **kwargs)   #call the constructor of the Tk 
                                            #class to inherit properties
        
        self.controller = None                                              
        screen_width = self.winfo_screenwidth()         #get the width of the screen                         
        screen_height = self.winfo_screenheight()       #get the height of the screen
        
        #Configurations of the Root
        self.title("Digital Shearography - Project 55")
        # Above: title of application                     
        self.geometry("{}x{}+0+0".format(screen_width, screen_height))
        # Above: Set the size of the window to fullscreen by default      
        
        self.columnconfigure(0, weight=1)   #configure weights of the columns and rows
        self.rowconfigure(0, weight=1)
        

        #Main Container to Hold the Class Frames (video, control and setup)
        main_container = ttk.Frame(self)
        main_container.grid(row=0, column=0)
        main_container.columnconfigure(0, weight=2)
        main_container.columnconfigure(1, weight=1)

        main_container.rowconfigure(0, weight=1)        
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
        # Below: create copies of the frame classes 
        # so that they can be accessed in the controller
        controller.set_video_frame(self.video_frame)
        controller.set_controls_frame(self.controls_frame)
        controller.set_setup_frame(self.setup_frame)
    

    
###################################################################################################################     
###################################################################################################################

######################### CAMERA SETUP #########################

bus = PyCapture2.BusManager()                   #identify the Globally Unique Identifier (GUID) of the camera
num_cams = bus.getNumOfCameras()                #determine the number of cameras connected to the PC
print('Number of cameras detected:', num_cams)  #print the number of cameras detected
if not num_cams:                                #if no cameras are detected exit the application
    print('Insufficient number of cameras. Exiting...')
    exit()

# Select camera on 0th index
c = PyCapture2.Camera()             #Assign Camera object to C
uid = bus.getCameraFromIndex(0)     #select camera on 0th index
c.connect(uid)                      #connect camera object to physical camera

# Disable On-board Image Processing
c.setProperty(type = PyCapture2.PROPERTY_TYPE.AUTO_EXPOSURE, onOff = False)  #Disable Auto Exposure

print('Starting image capture...')
c.startCapture()                    #start capturing data from the camera to the image buffers

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
