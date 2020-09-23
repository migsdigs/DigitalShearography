#File to link the video display with the controls


class Controller():
    def __init__(self):
        self.video_frame = None
        self.controls_frame = None

        self.inspection_time_limit_flag = False
        self.reference_image_delay_flag = False
        self.frame_capture_interval_flag = False

        self.save_count = 0
    
    ######################## METHODS FOR SETTING FRAMES TO CONTROL ########################
    
    def set_video_frame(self, frame):   #assign the video_frame class from the DS_GUI class to the video_frame object of the controller (allows for methods from video_frame class to be called in controller)
        self.video_frame = frame

    def set_controls_frame(self, frame):
        self.controls_frame = frame
    
    def set_setup_frame(self, frame):
        self.setup_frame = frame


    ######################## METHODS FOR VIDEO CONTROL ########################

    def pause(self):    #method for pausing video
        self.video_frame.pause_video()  #executes the pause_video() method from thee video frame class when pause() method is called
        self.controls_frame.pause_button["state"] = "disabled"
        self.controls_frame.play_button["state"] = "enabled"
        self.controls_frame.stop_button["state"] = "enabled"
        #print("video paused")
    
    def play(self):     #method to play cideo
        self.video_frame.play_video()
        self.controls_frame.play_button["state"] = "disabled"
        self.controls_frame.pause_button["state"] = "enabled"
        self.controls_frame.stop_button["state"] = "disabled"
        #print("video played")
    
    def stop(self):     #method to stop video/inspection
        self.video_frame.stop_video()
        self.controls_frame.play_button["state"] = "disabled"
        self.controls_frame.pause_button["state"] = "disabled"
        self.controls_frame.stop_button["state"] = "disabled"
        #print("video stopped")

    
    def display_fringes(self):  #display fringes when fringe display button is pressed
        self.video_frame.display_fringes_flag = True
        self.controls_frame.fringe_pattern_button["state"] = "disabled"
        self.controls_frame.real_time_video_button["state"] = "enabled"
    

    def display_video(self):    #display real time video when video button is pressed
        self.video_frame.display_fringes_flag = False
        self.controls_frame.fringe_pattern_button["state"] = "enabled"
        self.controls_frame.real_time_video_button["state"] = "disabled"

  
    def save_snapshot(self):    #method to save images when snapshot button is hit
        snapshot_name = "snapshot"+str(self.save_count)+".jpeg"
        self.video_frame.img.save(snapshot_name)
        self.save_count = self.save_count+1

    def frame_capture(self):    #method to save images at set intervals
        honk = 0


    ######################## METHODS FOR START INSPECTION ########################

    def start(self):
        self.controls_frame.pause_button["state"] = "enabled"

        self.setup_frame.inspection_time_limit_check_button["state"] = "disabled"
        self.setup_frame.inspection_time_limit_set_button["state"] = "disabled"

        self.setup_frame.frame_capture_interval_check_button["state"] = "disabled"
        self.setup_frame.frame_capture_interval_check_button["state"] = "disabled"

        self.setup_frame.reference_image_delay_check_button["state"] = "disabled"
        self.setup_frame.reference_image_delay_set_button["state"] = "disabled"

        self.setup_frame.start_inspection_button["state"] = "disabled"

        self.controls_frame.snapshot_button["state"] = "enabled"

        if not self.reference_image_delay_flag:
            self.video_frame.capture_reference_image()
            #print(self.video_frame.ref_image)
            self.controls_frame.fringe_pattern_button["state"] = "enabled"


    
    ######################## METHODS FOR INSPECTION SETUP ########################
    def inspection_time_limit_command(self):                    
        if self.setup_frame.inspection_time_limit_option.get():
            self.setup_frame.inspection_time_limit_entry["state"] = "enabled"                                      
            self.setup_frame.inspection_time_limit_set_button["state"] = "enabled"

            self.inspection_time_limit_flag = True                                          #inspection time limit flag (used in start method later)
        elif self.setup_frame.inspection_time_limit_option.get()==False:
            self.setup_frame.inspection_time_limit_entry["state"] = "disabled"
            self.setup_frame.inspection_time_limit_set_button["state"] = "disabled"

            self.inspection_time_limit_flag = False  
        


    def frame_capture_interval_command(self):               
        if self.setup_frame.frame_capture_interval_option.get():
            self.setup_frame.frame_capture_interval_entry["state"] = "enabled"
            self.setup_frame.frame_capture_interval_set_button["state"] = "enabled"

            self.frame_capture_interval_flag = True                                         #inspection time limit flag (used in start method later)
        elif self.setup_frame.frame_capture_interval_option.get()==False:
            self.setup_frame.frame_capture_interval_entry["state"] = "disabled"
            self.setup_frame.frame_capture_interval_set_button["state"] = "disabled"

            self.frame_capture_interval_flag = False 


    def reference_image_delay_command(self):               
        if self.setup_frame.reference_image_delay_option.get():
            self.setup_frame.reference_image_delay_entry["state"] = "enabled"
            self.setup_frame.reference_image_delay_set_button["state"] = "enabled"

            self.reference_image_delay_flag = True
        elif self.setup_frame.reference_image_delay_option.get()==False:
            self.setup_frame.reference_image_delay_entry["state"] = "disabled"
            self.setup_frame.reference_image_delay_set_button["state"] = "disabled"

            self.reference_image_delay_flag = True

    
    def inspection_time_limit_set(self):
        try:
            self.inspection_time_limit = self.setup_frame.inspection_time_limit_mins.get()
            
            print(self.inspection_time_limit)
        except:
            print("error")

    
    def frame_capture_interval_set(self):
        try:
            self.frame_capture_interval = self.setup_frame.frame_capture_interval_seconds.get()
            
            print(self.frame_capture_interval)
        except:
            print("error")

    
    def reference_image_delay_set(self):
        try:
            self.reference_image_delay = self.setup_frame.reference_image_delay_seconds.get()
            
            print(self.reference_image_delay)
        except:
            print("error")
    

    ######################## METHODS FOR CAMERA VARIABLES ########################
