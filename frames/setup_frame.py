import tkinter as tk
from tkinter import ttk

class SetupFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)

        #inspection setup frame
        inspection_setup_frame = ttk.Frame(self)
        inspection_setup_frame.grid()

        #Inside inspection setup frame
            #Inspection Setup Label and Start Button
        inspection_setup_label = ttk.Label(inspection_setup_frame, text="INSPECTION SETUP")
        inspection_setup_label.grid(row=0, column=0, pady = 5)

        start_inspection_button = ttk.Button(inspection_setup_frame, text = "START INSPECTION")
        start_inspection_button.grid(row=1, column=0, pady=5)

            #Inspection Time Limit Frame, Label, check button, entry field
        inspection_time_limit_Frame = ttk.Frame(inspection_setup_frame)
        inspection_time_limit_Frame.grid(row=2, column=0, pady=15)

        inspection_time_limit_label = ttk.Label(inspection_time_limit_Frame, text="Inspection Time Limit", padding = 10)
        inspection_time_limit_label.grid(row=0, column=0, sticky="EW")





