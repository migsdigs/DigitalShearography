The Digital Shearography GUI Application is an application to be used for Digital Shearography inspection devices utilizing the FLIR Integrated Imaging Solutions Chameleon3 CCD Camera. This application provides functions and operations needed to manage the Shearographic inspection process and display the fringe patterns that result from real-time subtraction of images using Digital Shearography.

Prior to using the application on a new PC, the PyCapture2 python extension, that is required for the operation of the Chameleon3 camera, needs to be installed. For instructions on how to extract the PyCapture2 package on Windows, please refer to the README_PyCapture2.txt file, which is provided by FLIR Integrated Imaging Solutions.

This Python Application also requires the installation of the OpenCV, Pillow and configparser libraries. This is done by:
1. Click on the Windows start button in the bottom left of the screen and search for 'command prompt'. Click on the Windows command prompt and wait for a black window to open.

2. Type "pip install configparser" and click the enter button to install the configparser library.

3. Type "pip install Pillow" and click the enter button to install the Pillow library.

4. Type "pip install opencv-python" and click the enter button to install the OpenCV library.


Once the Required Python Libraries are installed, the application may be used. Prior to opening the application, the Chameleon3 USB 3.0 camera must be connected to the PC. The application is opened by running the app.py file. Upon opening, the application the display window displays the camera view. Instructions for use of the application for a Non-destructive testing process are given below.

1. Prior to beginning the inspection process, the inspection setup on the right side of the application needs to be configured. Depending on the inspection device being used, the inspection mode should be set to normal or 4f mode.

2. Next, the desired inspection parameters (inspection time limit, frame capture interval, reference image delay) should be set. These can be set manually under the inspection setup or pre-set in the config.ini file and then imported using the Import Config File. The latter is recommended when running many NDT inspections with the same required inspection parameters and camera variable values.

3. The desired camera variables should be set (under Camera Variable Control). Setting a value greater than 1.0 increases the image enhancement (brightness, contrast), while applying a value between 0.0 and 1.0 decreases the image enhancement. The original image can be reverted to by using the Reset buttons.

4. If it is desired that the images to be saved are saved to a custom folder or location, the directory of this location, e.g. C:\Users\pc\Desktop\Final_Year_Project_App\test_inspection , should be pasted into the Image Save Location entry at the top of the application, afterwhich the Set Folder button should be pressed. If no save location is set, the images will save to the location of the applications install.

5. The inspection can begin by hitting the START INSPECTION button.

6. Once the reference image has been taken (immediately after pressing the START INSPECTION button or at the time set in the inspection setup), the camera display can be changed to display the real-time subtraction of the reference image from the current camera image by pressing the Fringe Pattern Mode button. One can revert back to displaying the real-time camera view by pressing the Video Mode Button.

7. The display can be paused or stopped using the Video Controls in the top panel.

8. Images that are displayed in the display window can be randomly saved by pressing the Snapshot Frame button in the top left of the application window.

9. Once the inspection is completed, a new inspection may be configured by pressing the New Inspection button in the top left of the application window.

For more information go to: https://github.com/migsdigs/Final_Year_Project
