import tkinter as tk
from tkinter import ttk

class SetupFrame(ttk.Frame):            #create a class of type ttk.Frame
    def __init__(self, parent, controller): #initialise the class
        super().__init__(parent)        #call the constructor of the ttk.Frame
                                        #class to inherit its and the parent's
                                        #properties

        self.columnconfigure(0, weight=1)   

        #inspection setup frame
        inspection_setup_frame = ttk.Frame(self)
        inspection_setup_frame.grid(row=0, column=0)

        #Inside inspection setup frame
            #Inspection Setup Label and Start Button
        inspection_setup_label = ttk.Label(inspection_setup_frame, text="INSPECTION SETUP")
        inspection_setup_label.grid(row=0, column=0, pady = 5)

        self.start_inspection_button = ttk.Button(inspection_setup_frame, text = "START INSPECTION", command = controller.start)     #set command
        self.start_inspection_button.grid(row=1, column=0, pady=5, ipadx=40, ipady=15)

            #Inspection Mode
        inspection_mode_frame = ttk.Frame(inspection_setup_frame)
        inspection_mode_frame.grid(row=2, column=0, pady=5)

        inspection_mode_label = ttk.Label(inspection_mode_frame, text="Inspection Mode")
        inspection_mode_label.grid(row=0, column=0, columnspan=2)

        self.normal_mode_button = ttk.Button(inspection_mode_frame, text="Normal", state = "disabled", command = controller.set_normal_mode)   
        self.normal_mode_button.grid(row=1, column=0)

        self.four_f_mode_button = ttk.Button(inspection_mode_frame, text="4f", command = controller.set_four_f_mode)       
        self.four_f_mode_button.grid(row=1, column=1)


            #Inspection Time Limit Frame, Label, check button, entry field
        inspection_time_limit_Frame = ttk.Frame(inspection_setup_frame)
        inspection_time_limit_Frame.grid(row=3, column=0, pady=5)

        inspection_time_limit_label = ttk.Label(inspection_time_limit_Frame, text="Inspection Time Limit (minutes)", padding = 10)
        inspection_time_limit_label.grid(row=0, column=0, columnspan=3, sticky="EW")

        self.inspection_time_limit_option = tk.BooleanVar()

        self.inspection_time_limit_check_button = ttk.Checkbutton(inspection_time_limit_Frame, 
        text="Enable", 
        variable=self.inspection_time_limit_option, 
        command = controller.inspection_time_limit_command, 
        onvalue=True, offvalue=False)
        self.inspection_time_limit_check_button.grid(row=1, column=0, columnspan=3)


        self.inspection_time_limit_mins = tk.DoubleVar()
        self.inspection_time_limit_entry = ttk.Entry(inspection_time_limit_Frame, width=6, textvariable=self.inspection_time_limit_mins, state="disabled")
        self.inspection_time_limit_entry.grid(row=2, column=0)

        self.inspection_time_limit_set_button = ttk.Button(inspection_time_limit_Frame, text="Set", state="disabled", command = controller.inspection_time_limit_set)  
        self.inspection_time_limit_set_button.grid(row=2, column=1)

        self.inspection_time_limit_value_label = ttk.Label(inspection_time_limit_Frame, text="None")
        self.inspection_time_limit_value_label.grid(row=2, column=2)


            #Frame Capture Interval
        Frame_capture_interval_frame = ttk.Frame(inspection_setup_frame)
        Frame_capture_interval_frame.grid(row=4, column=0, pady=5)

        Frame_capture_interval_label = ttk.Label(Frame_capture_interval_frame, text="Frame Capture Interval (seconds)", padding = 10)
        Frame_capture_interval_label.grid(row=0, column=0, columnspan=3, sticky="EW")

        self.frame_capture_interval_option = tk.BooleanVar()


        self.frame_capture_interval_check_button = ttk.Checkbutton(Frame_capture_interval_frame, 
        text="Enable", 
        variable=self.frame_capture_interval_option, 
        command = controller.frame_capture_interval_command, 
        onvalue=True, offvalue=False)
        self.frame_capture_interval_check_button.grid(row=1, column=0, columnspan=3)


        self.frame_capture_interval_seconds = tk.IntVar()
        self.frame_capture_interval_entry = ttk.Entry(Frame_capture_interval_frame, width=6, textvariable=self.frame_capture_interval_seconds, state="disabled")
        self.frame_capture_interval_entry.grid(row=2, column=0)

        self.frame_capture_interval_set_button = ttk.Button(Frame_capture_interval_frame, text="Set", state="disabled", command = controller.frame_capture_interval_set)  
        self.frame_capture_interval_set_button.grid(row=2, column=1)

        self.frame_capture_interval_value_label = ttk.Label(Frame_capture_interval_frame, text="None")
        self.frame_capture_interval_value_label.grid(row=2, column=2)


            #Reference Image Delay
        reference_image_delay_frame = ttk.Frame(inspection_setup_frame)
        reference_image_delay_frame.grid(row=5, column=0, pady=5)

        reference_image_delay_label = ttk.Label(reference_image_delay_frame, text="Reference Image Delay (seconds)", padding = 10)
        reference_image_delay_label.grid(row=0, column=0, columnspan=3, sticky="EW")

        self.reference_image_delay_option = tk.BooleanVar()


        self.reference_image_delay_check_button = ttk.Checkbutton(reference_image_delay_frame, 
        text="Enable", 
        variable=self.reference_image_delay_option, 
        command = controller.reference_image_delay_command, 
        onvalue=True, offvalue=False)
        self.reference_image_delay_check_button.grid(row=1, column=0, columnspan=3)


        self.reference_image_delay_seconds = tk.IntVar()
        self.reference_image_delay_entry = ttk.Entry(reference_image_delay_frame, width=6, textvariable=self.reference_image_delay_seconds, state="disabled")
        self.reference_image_delay_entry.grid(row=2, column=0)

        self.reference_image_delay_set_button = ttk.Button(reference_image_delay_frame, text="Set", state="disabled", command = controller.reference_image_delay_set)  
        self.reference_image_delay_set_button.grid(row=2, column=1)

        self.reference_image_delay_value_label = ttk.Label(reference_image_delay_frame, text="None")
        self.reference_image_delay_value_label.grid(row=2, column=2)


        ####################### CAMERA VARIABLES #######################
        #Camera Variables Frame
        camera_variables_frame = ttk.Frame(self)
        camera_variables_frame.grid(row=1, column=0, pady=15)

        #Inside Camera Variables Frame
            #Camera Variable Label
        camera_variable_label = ttk.Label(camera_variables_frame, text="Camera Variable Control", padding = 5)
        camera_variable_label.grid(row=0, column=0, columnspan=3)

            #Brightness Frame, Label and Entry
        brightness_frame = ttk.Frame(camera_variables_frame)
        brightness_frame.grid(row=1, column=0)
        
        brightness_label = ttk.Label(brightness_frame, text="Brightness", padding =5)
        brightness_label.grid(row=0, column=0)

        self.brightness_value_label = ttk.Label(brightness_frame, text="1.0", padding = 5)
        self.brightness_value_label.grid(row=0, column=1)

        self.brightness = tk.DoubleVar()
        self.brightness_entry = ttk.Entry(brightness_frame, width=6, textvariable=self.brightness)
        self.brightness_entry.grid(row=1, column=0)
        self.brightness_entry.delete(0, 'end')

        brightness_set_button = ttk.Button(brightness_frame, text="Set", command = controller.set_brightness)        #set command
        brightness_set_button.grid(row=1, column=1)

        brightness_reset_button = ttk.Button(brightness_frame, text="Reset", command = controller.reset_brightness)    
        brightness_reset_button.grid(row=1, column=2, sticky="EW")


            #Contrast Label and Entry
        contrast_frame = ttk.Frame(camera_variables_frame)
        contrast_frame.grid(row=2, column=0)

        contrast_label = ttk.Label(contrast_frame, text=" Contrast ", padding = 5)
        contrast_label.grid(row=0, column=0)

        self.contrast_value_label = ttk.Label(contrast_frame, text="1.0", padding = 5)
        self.contrast_value_label.grid(row=0, column=1)

        self.contrast = tk.DoubleVar()
        self.contrast_entry = ttk.Entry(contrast_frame, width=6, textvariable=self.contrast)
        self.contrast_entry.grid(row=1, column=0)
        self.contrast_entry.delete(0, 'end')

        contrast_set_button = ttk.Button(contrast_frame, text="Set", command = controller.set_contrast)           
        contrast_set_button.grid(row=1, column=1)

        contrast_reset_button = ttk.Button(contrast_frame, text="Reset", command = controller.reset_contrast)      
        contrast_reset_button.grid(row=1, column=2, sticky="EW")




    

        

        



