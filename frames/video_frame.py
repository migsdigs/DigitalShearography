# Imports
import tkinter as tk
from tkinter import ttk
import PIL as pl
from PIL import Image, ImageTk, ImageEnhance
import cv2
import numpy as np

class VideoFrame(ttk.Frame):    # create a class of type ttk.Frame
    def __init__(self, parent, screen_width, screen_height, cam, delay):    
                                    # initialise the class
        super().__init__(parent)    # call the constructor of the ttk.Frame
                                    # class to inherit its and the parent's 
                                    # properties

        self.screen_width = screen_width    # integers passed in from app.py
        self.screen_height = screen_height  # integers passed in from app.py

        self.cam = cam      # camera object that is passed into the VideoFrame class
        self.delay = delay  # the delay between frame updates of the video display

        self.video_pause = False            # A flag used to determine if video must be paused or playing
        self.display_fringes_flag = False   # A flag to be used to determine if fringes or real time video 
                                            # must be displayed
        self.mode_flag = False              # A flag used to alter the inspection mode from regular to 4f mode 
        self.ref_image = None               # An object to store the reference image once it is taken
        self.img = None                     # An object to store the current camera image

        # Camera Variable Default Values
        self.brightness_value = 1.0         # brightness value used in image enhancement
        self.contrast_value = 1.0           # contrast value used in image enhancement

        # Frames
        video_frame = ttk.Frame(self)       # create the video_frame frame
        video_frame.grid()


        # Video Label
        self.video_display_label = ttk.Label(video_frame)
        self.video_display_label.grid(row=0, column=0)

    
    def capture_reference_image(self):          # method to capture and save reference image (only to be called once)
        ref_buffer = self.cam.retrieveBuffer()  # retrieve data from the camera buffer
        self.ref_image=np.array(ref_buffer.getData(),dtype="uint8").reshape((ref_buffer.getRows(),ref_buffer.getCols()))  
        # Above: convert ref_buffer to numpy array to be used in subtraction of images
        
        if self.mode_flag == True:  # If 4f inspection mode is enabled, rotate numpy image 180 degrees
            self.ref_image = np.flip(self.ref_image, axis=0)
            self.ref_image = np.flip(self.ref_image, axis=1)

        self.ref_img = pl.Image.fromarray(self.ref_image)
        # Above: convert numpy image array to image object

    def display_video(self):    #method to display real-time video or fringe patterns to display
        image = self.cam.retrieveBuffer()   # retrieve data from the camera buffer
        cv_image1 = np.array(image.getData(),dtype="uint8").reshape((image.getRows(),image.getCols()))                      
        # Above: convert image to numpy array
        
        if self.mode_flag == True:  # If 4f inspection mode is enabled, rotate numpy image 180 degrees
            cv_image1 = np.flip(cv_image1, axis=0)
            cv_image1= np.flip(cv_image1, axis=1)

    #Display real time video or fringe patterns depending on the state of the flag
        if not self.display_fringes_flag:   # if fringe pattern display mode is disabled
            self.img = pl.Image.fromarray(cv_image1)
            # Above: convert numpy image array to image object    

            contrastImg = ImageEnhance.Contrast(self.img)
            contrastedImage = contrastImg.enhance(self.contrast_value)
            # Above: adjusting image to desired contrast  
            
            brightnessImg = ImageEnhance.Brightness(contrastedImage)
            Enhanced_img = brightnessImg.enhance(self.brightness_value)
            # Above: adjusting image to desired brightness

            self.photo = Enhanced_img.resize((self.screen_width-700,self.screen_height-300))
            # Above: resize image

            display_image = ImageTk.PhotoImage(self.photo)
            # Above: convert image to tkinter compatible photo image

            self.video_display_label.config(image=display_image)
            self.video_display_label.image = display_image
            # Above: display image on tkinter label
        
        elif self.display_fringes_flag==True:   #if fringe pattern display mode is enabled
            self.difference = cv2.absdiff(cv_image1,self.ref_image)    
            #Above: subtract the current image from the reference image

            self.img = pl.Image.fromarray(self.difference)
            # Above: convert numpy image array to image object

            contrastImg = ImageEnhance.Contrast(self.img)
            contrastedImage = contrastImg.enhance(self.contrast_value)     
            # Above: adjusting image to desired contrast

            brightnessImg = ImageEnhance.Brightness(contrastedImage)
            Enhanced_img = brightnessImg.enhance(self.brightness_value)
            # Above: adjusting image to desired brightness

            self.photo = Enhanced_img.resize((self.screen_width-700,self.screen_height-300))
            # Above: resize image

            display_image = ImageTk.PhotoImage(self.photo)
            # Above: convert image to tkinter compatible photo image

            self.video_display_label.config(image=display_image)
            self.video_display_label.image = display_image
            # Above: display image on tkinter label

        if not self.video_pause:    #if the display is not paused (note below)
            self.video_display_label.after(self.delay, lambda: self.display_video())
            # Above: call the display_video() method after delay number of milliseconds to refresh display
            

    def pause_video(self):  # method to pause video display
        self.video_pause = True

    def play_video(self):   # method to resume video display
        self.video_pause = False
        self.display_video()
    
    def stop_video(self):   # method to stop video display and inspection process
        # Set the video display to a black image:
        self.stop_image = Image.open("./Assets/stop.JPG").resize((self.screen_width-700,self.screen_height-300))    
        self.stop_photo = ImageTk.PhotoImage(self.stop_image)
        
        # Set video_display_label to black image when inspection is stopped
        self.video_display_label.config(image=self.stop_photo)
        self.video_display_label.image = self.stop_photo
        

        

    

        

