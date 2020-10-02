import tkinter as tk
from tkinter import ttk
import PIL as pl
from PIL import Image, ImageTk
import cv2
import numpy as np

class VideoFrame(ttk.Frame):
    def __init__(self, parent, screen_width, screen_height, cam, delay):
        super().__init__(parent)

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.cam = cam      #camera object that is passed into the VideoFrame class
        self.delay = delay  #the delay between frame updates of the video display

        self.video_pause = False            #A flag used to determine if video must be paused or playing
        self.display_fringes_flag = False   #A flag to be used to determine if fringes or real time video must be displayed
        self.ref_image = None
        self.img = None
        

        #Frames
        video_frame = ttk.Frame(self)
        video_frame.grid()


        #Video Label
        self.video_display_label = ttk.Label(video_frame)
        self.video_display_label.grid(row=0, column=0)

        
    
    def capture_reference_image(self):      #only to be called once
        ref_buffer = self.cam.retrieveBuffer()
        self.ref_image = np.array(ref_buffer.getData(), dtype="uint8").reshape( (ref_buffer.getRows(), ref_buffer.getCols()) )  #convert ref_buffer to numpy array to be used in subtraction of images
        self.ref_img = pl.Image.fromarray(self.ref_image)

    def display_video(self):
        image = self.cam.retrieveBuffer()
        cv_image1 = np.array(image.getData(), dtype="uint8").reshape( (image.getRows(), image.getCols()) )                      #convert image to numpy array
        #cv_image2 = np.array(image.getData(), dtype="uint8").reshape( (image.getRows(), image.getCols()) )
    
            
        #print(result)  
        #cv2.imshow('frame',result)
        #cv2.waitKey(1)

    #Display real time video or fringe patterns depending on the state of the flag
        if not self.display_fringes_flag:
            self.img = pl.Image.fromarray(cv_image1)
            photo = self.img.resize((self.screen_width-700,self.screen_height-300))

            display_image = ImageTk.PhotoImage(photo)
            self.video_display_label.config(image=display_image)
            self.video_display_label.image = display_image
        
        elif self.display_fringes_flag==True:
            self.difference = cv2.absdiff(cv_image1,self.ref_image)    #subtract the current image from the reference image

            self.img = pl.Image.fromarray(self.difference)
            photo = self.img.resize((self.screen_width-700,self.screen_height-300))

            display_image = ImageTk.PhotoImage(photo)
            self.video_display_label.config(image=display_image)
            self.video_display_label.image = display_image

    
        if not self.video_pause:
            self.video_display_label.after(self.delay, lambda: self.display_video())


    def pause_video(self):
        self.video_pause = True

    def play_video(self):
        self.video_pause = False
        self.display_video()
    
    def stop_video(self):
        self.stop_image = Image.open("./Assets/stop.JPG").resize((self.screen_width-700,self.screen_height-300))
        self.stop_photo = ImageTk.PhotoImage(self.stop_image)
        
        self.video_display_label.config(image=self.stop_photo)
        self.video_display_label.image = self.stop_photo

        self.cam.stopCapture()
        print("stopping capture")
        self.cam.disconnect()
        print("camera disconnected")

    

        

