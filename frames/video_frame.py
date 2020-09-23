import tkinter as tk
from tkinter import ttk
import PIL as pl
from PIL import Image, ImageTk
import cv2
import numpy as np

class VideoFrame(ttk.Frame):
    def __init__(self, parent, screen_width, screen_height):
        super().__init__(parent)

        self.screen_width = screen_width
        self.screen_height = screen_height

        #Frames
        video_frame = ttk.Frame(self)
        video_frame.grid()

        #fetch image
        #video_image = Image.open("./frames/download.png").resize((1288,800))
        #video_photo = ImageTk.PhotoImage(video_image)

        #Video Label
        self.video_display_label = ttk.Label(video_frame)
        #video_display_label.image = video_photo
        self.video_display_label.grid(row=0, column=0)

        self.video_pause = False
    
    def capture_reference_image(self):
        honk = 0
    
    def display_video(self, c, delay):
        self.c = c
        self.delay = delay
        image = self.c.retrieveBuffer()
        cv_image1 = np.array(image.getData(), dtype="uint8").reshape( (image.getRows(), image.getCols()) )
        #cv_image2 = np.array(image.getData(), dtype="uint8").reshape( (image.getRows(), image.getCols()) )

        #difference = cv2.absdiff(cv_image1,ref)
        #print(result)
        #cv2.imshow('frame',result)
        #cv2.waitKey(1)
        img = pl.Image.fromarray(cv_image1)
        image = img.resize((self.screen_width-700,self.screen_height-300))

        photo = ImageTk.PhotoImage(image)
        self.video_display_label.config(image=photo)
        self.video_display_label.image = photo

        if not self.video_pause:
            self.video_display_label.after(delay, lambda: self.display_video(self.c, self.delay))


    def pause_video(self):
        self.video_pause = True

    def play_video(self):
        self.video_pause = False
        self.display_video(self.c, self.delay)
    
    def stop_video(self):
        self.stop_image = Image.open("./Assets/stop.JPG").resize((self.screen_width-700,self.screen_height-300))
        self.stop_photo = ImageTk.PhotoImage(self.stop_image)
        
        self.video_display_label.config(image=self.stop_photo)
        self.video_display_label.image = self.stop_photo

    

        

