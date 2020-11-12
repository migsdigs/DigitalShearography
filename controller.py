

#Configuration File Setup
from configparser import ConfigParser
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)

class Controller():                 # create the Controller class
    def __init__(self):             # initialise the class
        self.video_frame = None     # video_frame object to which VideoFrame class is assigned
        self.controls_frame = None  # controls_frame object to which ControlsFrame class is assigned
        self.setup_frame = None     # setup_frame object to which SetupFrame class is assigned

        self.inspection_time_limit_flag = False     
        # Above: flag state determines if inspection time limit is going to be used or not
        self.reference_image_delay_flag = False     
        # Above: flag state determines if reference image delay is going to be used or not
        self.frame_capture_interval_flag = False    
        # Above: flag state determines if frames saving at a set interval is going to be used or not

        self.save_count = 0             # Object to store the image save count
        self.interval_save_count = 0    # Object to store count of images saved at set intervals

        # set the reference image delay, frame capture interval & inspection time limit to 0 default
        # (used as a check condition later)
        self.reference_image_delay = 0
        self.frame_capture_interval = 0
        self.inspection_time_limit = 0

        self.save_location = str()      # Object to store desired save location of images
        self.save_location_flag = False # Flag state determines if custom save location is used or not

    
    ######################## METHODS FOR SETTING FRAMES TO CONTROL ########################
    # assign the frame classes in the DS_GUI class to the 
    # objects of the controller (allows for attributes 
    # of the frame classes to be accessed in the controller class)
    
    def set_video_frame(self, frame):   
        self.video_frame = frame

    def set_controls_frame(self, frame):
        self.controls_frame = frame
    
    def set_setup_frame(self, frame):
        self.setup_frame = frame

    
    ######################## METHODS INSPECTION MODE ########################
    # methods to set the inspection mode
    # if 4f mode is activated, the resultant image is flipped 180 degrees before
    # being displayed, as is required for a 4f system

    def set_normal_mode(self):
        self.setup_frame.normal_mode_button["state"] = "disabled"
        self.setup_frame.four_f_mode_button["state"] = "enabled"
        self.video_frame.mode_flag = False
    
    def set_four_f_mode(self):
        self.setup_frame.normal_mode_button["state"] = "enabled"
        self.setup_frame.four_f_mode_button["state"] = "disabled"
        self.video_frame.mode_flag = True

    ######################## METHODS FOR VIDEO CONTROL ########################
    # methods for controlling the video display
    # allow for the display to be paused, resumed or stopped

    def pause(self):    #method for pausing video
        self.video_frame.pause_video()  #executes the pause_video() method from thee video frame class when pause() method is called
        self.controls_frame.pause_button["state"] = "disabled"
        self.controls_frame.play_button["state"] = "enabled"
        self.controls_frame.stop_button["state"] = "enabled"
        
    
    def play(self):     #method to play video
        self.video_frame.play_video()
        self.controls_frame.play_button["state"] = "disabled"
        self.controls_frame.pause_button["state"] = "enabled"
        self.controls_frame.stop_button["state"] = "disabled"
        
    
    def stop(self):     #method to stop video/inspection
        self.video_frame.stop_video()
        self.controls_frame.play_button["state"] = "disabled"
        self.controls_frame.pause_button["state"] = "disabled"
        self.controls_frame.stop_button["state"] = "disabled"

        self.controls_frame.snapshot_button["state"] = "disabled"
        self.controls_frame.real_time_video_button["state"] = "disabled"
        self.controls_frame.fringe_pattern_button["state"] = "disabled"
        
        self.frame_capture_interval = 0     #if frames are set to be captured at set intervals, stop capturing frames


    # methods to control what is displayed
    def display_fringes(self):  # display fringes when fringe display button is pressed
                                # results in real-time subtraction of reference image from current image
        self.video_frame.display_fringes_flag = True
        self.controls_frame.fringe_pattern_button["state"] = "disabled"
        self.controls_frame.real_time_video_button["state"] = "enabled"
    

    def display_video(self):    #display real time video when video button is pressed
        self.video_frame.display_fringes_flag = False
        self.controls_frame.fringe_pattern_button["state"] = "enabled"
        self.controls_frame.real_time_video_button["state"] = "disabled"


    ######################## METHODS FOR IMAGES & SAVING ########################
  
    def save_snapshot(self):    #method to save images when snapshot button is hit
        if self.save_location_flag:     #if a custom save location has been provided
            try:                        #try save the image to the provided location
                snapshot_name = self.save_location+"\\snapshot"+str(self.save_count)+".jpeg"
                self.video_frame.photo.save(snapshot_name)

            except:                     #if an error occurs, save the image to the default save location
                snapshot_name = "snapshot"+str(self.save_count)+".jpeg"
                self.video_frame.photo.save(snapshot_name)

        else:                           #else, save the image to the default save location
            snapshot_name = "snapshot"+str(self.save_count)+".jpeg"
            self.video_frame.photo.save(snapshot_name)
        self.save_count = self.save_count+1     #increment the save count by 1


    def save_ref_image(self):   #method to save the reference image once it is taken
        if self.save_location_flag:
            try:
                self.video_frame.ref_img.save(self.save_location + "\\reference_image.jpeg")
            except:
                self.video_frame.ref_img.save("reference_image.jpeg")
        
        else:
            self.video_frame.ref_img.save("reference_image.jpeg")


    def frame_capture_save(self):    #method to save images at set intervals
        frame_capture_interval_milliseconds = int(self.frame_capture_interval*1000)

        if self.frame_capture_interval_flag: # if frame capture interval Checkbutton is checked
            if self.frame_capture_interval > 0: # checking that the interval (seconds) set is valid
                if self.save_location_flag: # save frames to desired save location
                    try:
                        frame_capture_name = self.save_location + "\\interval_capture"+str(self.interval_save_count)+".jpeg"
                        self.video_frame.photo.save(frame_capture_name)
                
                    except:
                        frame_capture_name = "interval_capture"+str(self.interval_save_count)+".jpeg"
                        self.video_frame.photo.save(frame_capture_name)
                        
                else:   # save frames to default save location
                    frame_capture_name = "interval_capture"+str(self.interval_save_count)+".jpeg"
                    self.video_frame.photo.save(frame_capture_name)

                self.interval_save_count = self.interval_save_count+1
                self.setup_frame.start_inspection_button.after(frame_capture_interval_milliseconds, lambda: self.frame_capture_save())            


    def get_save_location(self): # method to retrieve desired save location from entry
        self.save_location = self.controls_frame.folder_directory.get()
        self.save_location_flag = True  # set the save_location_flag to true 
        

    ######################## METHOD FOR RESETTING INSPECTION ########################
    # resets button states and set inspection parameters so that new inspection can be configured
    def reset(self):    
        self.setup_frame.start_inspection_button["state"] = "enabled"

        self.controls_frame.play_button["state"] = "disabled"
        self.controls_frame.pause_button["state"] = "disabled"
        self.controls_frame.stop_button["state"] = "disabled"

        self.controls_frame.snapshot_button["state"] = "enabled"
        self.controls_frame.new_inspection_button["state"] = "disabled"

        self.controls_frame.folder_set_button["state"] = "enabled"
        self.controls_frame.config_button["state"] = "enabled"

        self.video_frame.ref_image = None   # reset reference image variable to None
        self.video_frame.display_fringes_flag = False           #change display mode back to real time video display
        self.controls_frame.real_time_video_button["state"] = "disabled"
        self.controls_frame.fringe_pattern_button["state"] = "disabled"
        
        self.video_frame.mode_flag = False                      #change inspection made back to normal inspection
        self.setup_frame.four_f_mode_button["state"] = "enabled"
        self.setup_frame.normal_mode_button["state"] = "disabled"

        self.setup_frame.inspection_time_limit_check_button["state"] = "enabled"
        self.setup_frame.frame_capture_interval_check_button["state"] = "enabled"
        self.setup_frame.reference_image_delay_check_button["state"] = "enabled"

        self.inspection_time_limit = 0                          #reset inspection time limit
        self.setup_frame.inspection_time_limit_value_label["text"] = "None"     

        self.frame_capture_interval = 0                         #reset frame capture interval
        self.setup_frame.frame_capture_interval_value_label["text"] = "None"

        self.reference_image_delay = 0                          #reset reference image delay
        self.setup_frame.reference_image_delay_value_label["text"] = "None"

        if self.video_frame.video_pause:    #if the display has been paused and stopped, display real time video again 
            self.video_frame.play_video()

        
    ######################## METHODS FOR START INSPECTION ########################
    # starts the inspection procedure
    # starts the time count for relevant inspection parameters that have been set
    # disables widgets that should not be used during the inspection
    def start(self):
        self.controls_frame.pause_button["state"] = "enabled"   #enable pause button

        # disabled buttons, Checkbuttons and entries of inspection parameters
        self.setup_frame.inspection_time_limit_check_button["state"] = "disabled"
        self.setup_frame.inspection_time_limit_set_button["state"] = "disabled"
        self.setup_frame.inspection_time_limit_entry["state"] = "disabled"

        self.setup_frame.frame_capture_interval_check_button["state"] = "disabled"
        self.setup_frame.frame_capture_interval_check_button["state"] = "disabled"
        self.setup_frame.frame_capture_interval_entry["state"] = "disabled"

        self.setup_frame.reference_image_delay_check_button["state"] = "disabled"
        self.setup_frame.reference_image_delay_set_button["state"] = "disabled"
        self.setup_frame.reference_image_delay_entry["state"] = "disabled"

        self.setup_frame.start_inspection_button["state"] = "disabled"

        self.controls_frame.new_inspection_button["state"] = "enabled"

        self.controls_frame.folder_entry["state"] = "disabled"
        self.controls_frame.folder_set_button["state"] = "disabled"

        self.controls_frame.config_button["state"] = "disabled"

        self.setup_frame.normal_mode_button["state"] = "disabled"
        self.setup_frame.four_f_mode_button["state"] = "disabled"

        # call inspection 
        self.reference_image()      #call take_reference_image method
        self.frame_capture_save()   #call frame_capture_save
        self.inspection_limit()     #call inspection_limit method

        
    def reference_image(self):     
        # determines when reference image will be taken 
        # then takes reference image using take_reference_image() method
        if not self.reference_image_delay_flag:     
            # if reference image delay flag is False, a reference image will be taken immediately after start
            self.take_reference_image()

        elif self.reference_image_delay_flag:       
            #if reference image delay flag is true, reference image will only be taken after the set seconds    
            if self.reference_image_delay > 0:
                reference_image_delay_milliseconds = int(self.reference_image_delay*1000)
                self.setup_frame.start_inspection_button.after(reference_image_delay_milliseconds, lambda: self.take_reference_image())    
                # Above: after set seconds take reference image
            
            else:
                self.take_reference_image()         
                # Above: if a delay is not properly inputted, it will default to no delay


    def take_reference_image(self): 
        # takes reference image by calling capture_reference_image 
        # from video_frame and enables fringe pattern button
        self.video_frame.capture_reference_image()
        self.controls_frame.fringe_pattern_button["state"] = "enabled"
        self.save_ref_image()   #once reference image is taken, save the image


    def inspection_limit(self):
        if self.inspection_time_limit_flag: # if inspection time limit checkbutton is checked
            if self.inspection_time_limit > 0:  #checking that the time limit set is valid
                inspection_time_limit_milliseconds = int(self.inspection_time_limit*1000*60)
                self.setup_frame.start_inspection_button.after(inspection_time_limit_milliseconds, lambda: self.inspection_limit_set())    
                # Above: after set minutes stop inspection by called inspection_time_limit_set() method


    def inspection_limit_set(self):
        self.pause()
        self.video_frame.video_display_label.after(500, lambda: self.stop())    
        # Above: after 500 ms stop inspection and disconnect camera
        
    


    ######################## METHODS FOR INSPECTION SETUP ########################

    def inspection_time_limit_command(self):    
        # Sets flags to true or false and enables/disables 
        # buttons & entry based on checkbuttons status                   
        if self.setup_frame.inspection_time_limit_option.get():
            self.setup_frame.inspection_time_limit_entry["state"] = "enabled"                                      
            self.setup_frame.inspection_time_limit_set_button["state"] = "enabled"

            self.inspection_time_limit_flag = True  #inspection time limit flag (used in start() method)
        
        elif self.setup_frame.inspection_time_limit_option.get()==False:
            self.setup_frame.inspection_time_limit_entry["state"] = "disabled"
            self.setup_frame.inspection_time_limit_set_button["state"] = "disabled"

            self.inspection_time_limit_flag = False

            self.setup_frame.inspection_time_limit_value_label["text"] = "None"     #sets the text of the label to none  
            self.inspection_time_limit = 0      #set inspection time limit to 0 if disabled

    def frame_capture_interval_command(self):   
        # Sets flags to true or false and enables/disables 
        # buttons & entry based on checkbuttons status            
        if self.setup_frame.frame_capture_interval_option.get():
            self.setup_frame.frame_capture_interval_entry["state"] = "enabled"
            self.setup_frame.frame_capture_interval_set_button["state"] = "enabled"

            self.frame_capture_interval_flag = True                                         
            # Above: inspection time limit flag (used in start method later)
        
        elif self.setup_frame.frame_capture_interval_option.get()==False:
            self.setup_frame.frame_capture_interval_entry["state"] = "disabled"
            self.setup_frame.frame_capture_interval_set_button["state"] = "disabled"

            self.frame_capture_interval_flag = False 

            self.setup_frame.frame_capture_interval_value_label["text"] = "None"
            self.frame_capture_interval = 0     #set frame capture interval to 0 if disabled


    def reference_image_delay_command(self):    
        # Sets flags to true or false and enables/disables 
        # buttons & entry based on checkbuttons status             
        if self.setup_frame.reference_image_delay_option.get():
            self.setup_frame.reference_image_delay_entry["state"] = "enabled"
            self.setup_frame.reference_image_delay_set_button["state"] = "enabled"

            self.reference_image_delay_flag = True
            # Above: inspection time limit flag (used in start method later)
        
        elif self.setup_frame.reference_image_delay_option.get()==False:
            self.setup_frame.reference_image_delay_entry["state"] = "disabled"
            self.setup_frame.reference_image_delay_set_button["state"] = "disabled"

            self.reference_image_delay_flag = False

            self.setup_frame.reference_image_delay_value_label["text"] = "None"
            self.reference_image_delay = 0     #set reference image delay to 0 if disabled

    
    def inspection_time_limit_set(self):    
        # sets the inspection time limit time when set button is pressed
        try:    # try set inspection time limit to value in entry
            self.inspection_time_limit = self.setup_frame.inspection_time_limit_mins.get()
            self.setup_frame.inspection_time_limit_value_label["text"] = str(self.inspection_time_limit)
            
        except: # if an error occurs, disabled inspection time limit
            self.inspection_time_limit = 0
            self.setup_frame.inspection_time_limit_value_label["text"] = "None"

    
    def frame_capture_interval_set(self):   
        # sets the frame capture interval time when set button is pressed
        try:    # try set frame capture interval to value in entry
            self.frame_capture_interval = self.setup_frame.frame_capture_interval_seconds.get()
            self.setup_frame.frame_capture_interval_value_label["text"] = str(self.frame_capture_interval)

        except: # if an error occurs, disabled frame capture interval
            self.frame_capture_interval = 0
            self.setup_frame.frame_capture_interval_value_label["text"] = "None"
    
    def reference_image_delay_set(self):    
        # sets the reference image delay time when set button is pressed
        try:    # try set reference image delay to value in entry
            self.reference_image_delay = self.setup_frame.reference_image_delay_seconds.get()
            self.setup_frame.reference_image_delay_value_label["text"] = str(self.reference_image_delay)

        except: # if an error occurs, disabled reference image delay
            self.reference_image_delay = 0   #if this remains 0, there will be no reference image delay
            self.setup_frame.reference_image_delay_value_label["text"] = "None"   

    ######################## METHODS FOR CAMERA VARIABLES ########################

    def set_brightness(self):   # method to set image brightness 
        try:    # try set brightness value to value in entry
            self.video_frame.brightness_value = self.setup_frame.brightness.get()
            self.setup_frame.brightness_value_label["text"] = str(self.video_frame.brightness_value)
        
        except: # if an error occurs, reset the image brightness
            self.video_frame.brightness_value = 1.0
            self.setup_frame.brightness_value_label["text"] = str(self.video_frame.brightness_value)


    def reset_brightness(self): # method to reset the image brightness
        self.video_frame.brightness_value = 1.0
        self.setup_frame.brightness_entry.delete(0, "end")
        self.setup_frame.brightness_value_label["text"] = str(self.video_frame.brightness_value)

    
    def set_contrast(self): # method to set image contrast 
        try:    # try set contrast value to value in entry
            self.video_frame.contrast_value = self.setup_frame.contrast.get()
            self.setup_frame.contrast_value_label["text"] = str(self.video_frame.contrast_value)
        
        except: # if an error occurs, reset the image contrast
            self.video_frame.contrast_value = 1.0
            self.setup_frame.contrast_value_label["text"] = str(self.video_frame.contrast_value)

    
    def reset_contrast(self):   # method to reset the image contrast
        self.video_frame.contrast_value = 1.0
        self.setup_frame.contrast_entry.delete(0, "end")
        self.setup_frame.contrast_value_label["text"] = str(self.video_frame.contrast_value)


    ######################## METHOD FOR CONFIG FILE ########################

    def set_config(self):   
        # method to configure inspection parameters and camera variables
        # to values given in the file config.ini, when the Import Config File
        # button is pressed

        #configure contrast
        try:    # try set contrast value to value in config file
            self.video_frame.contrast_value = float(config['cameraVariables']['CONTRAST'])

        except: # if an error occurs, set image contrast to default
            self.video_frame.contrast_value = 1.0


        #configure brightness
        try:    # try set brightness value to value in config file
            self.video_frame.brightness_value = float(config['cameraVariables']['BRIGHTNESS'])

        except: # if an error occurs, set image brightness to default
            self.video_frame.brightness_value = 1.0

        
        #configure inspection time limit
        try:    # try set inspection time limit value to value in config file
            self.inspection_time_limit = float(config['inspectionSetup']['INSPECTION_TIME_LIMIT'])
            self.setup_frame.inspection_time_limit_value_label["text"] = str(self.inspection_time_limit)
            self.inspection_time_limit_flag = True

        except: # if an error occurs, disable inspection time limit
            self.inspection_time_limit = 0
            self.setup_frame.inspection_time_limit_value_label["text"] = "None"

        
        #configure frame capture interval
        try:    # try set frame capture interval value to value in config file
            self.frame_capture_interval = float(config['inspectionSetup']['FRAME_CAPTURE_INTERVAL'])
            self.setup_frame.frame_capture_interval_value_label["text"] = str(self.frame_capture_interval)
            self.frame_capture_interval_flag = True
        
        except: # if an error occurs, disable frame capture interval
            self.frame_capture_interval = 0
            self.setup_frame.frame_capture_interval_value_label["text"] = "None"

        
        #configure reference image delay
        try:    # try reference image delay value to value in config file
            self.reference_image_delay = float(config['inspectionSetup']['REFERENCE_IMAGE_DELAY'])
            self.setup_frame.reference_image_delay_value_label["text"] = str(self.reference_image_delay)
            self.reference_image_delay_flag = True
        
        except: # if an error occurs, disable reference image delay
            self.reference_image_delay = 0
            self.setup_frame.reference_image_delay_value_label["text"] = "None"


        self.controls_frame.config_button['state'] = 'disabled' 
        # Above: disable the config_button after importing config file