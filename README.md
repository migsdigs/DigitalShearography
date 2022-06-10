# Refinement of an Existing Digital Shearography Device and Development of a GUI for camera interaction

Authors : [Miguel Garcia Naude](https://github.com/migsdigs)

## Abstract

Digital Shearography is an optical non-destructive testing technique that is used to inspect objects for defects. The benefits of Non-destructive testing and in particular, Digital Shearography, has resulted in it being useful in maintenance and quality conformance in automotive and aeronautical industries. Most Digital Shearography devices make use of Michelson Interferometers as their shearing device,however devices making use of this shearing device are limited to having a small angular field of view. By incorporating a 4f system into a Michelson Interferometer based inspection device, the angular field of view of the system is no longer limited by the Michelson Interferometer, thus maximising the camera field of view. By developing a user-friendly GUI to interact with the developed inspection device, the Shearographic Inspection process is managed and fringe patterns resulting from real-time subtraction of images using Digital Shearography are displayed. This enables non-destructive tests to be effectively carried out in order to gather object defect information. 

## Products
|   |   |
|:-:|:-:|
| ![device](/products/device.png) <br> Assembled Prototype| ![device2](/products/device2.png) <br> Internal Components of Assembled Prototype displaying 4f system |

|   |
|:-:|
| ![GUI](/products/gui.png) <br> Developed Graphical User Interface|

The above shows the developed products for this project. The first two images display the designed and assembled Digital Shearography system incorporating a 4f System (notice how the camera lens is separated from the camera). The third image is a screenshot of the developed GUI. Key features include the live camera display and the parameter tuning options on the right of the screen.

## Excerpt of Results
|   |
|:-:|
| ![original_fov](/results/original_fov.png) <br> Field of View of Existing Prototype| 
| ![4f_fov](/results/obtained_fov_with_4f.png) <br> Field of View of Revised Prototype with a 4f system incorporated|
|![defect_detection](/results/comparrison.png) <br> Defect detection (formation of fringe patterns) using the revised prototype (left) and the existing prototype (right)|


An excerpt of the results shown above shows the improved field of view obtained by using the revised design. However, as can be seen by the figure in which the prototypes are used for defect detection, the revised design is unable to produce the same level of image quality as the existing one. This is likely due to the limitations with regards to the available machining capabilities. Incorporating a 4f system introduces many more opportunities for errors to arise as even the slight misplacement of a lens, mirror or camera sensor will result in loss of image quality. Making use of more precise machining would thus likely give rise to a highly capable prototype for conducting digital shearography.

## Running the code for the GUI

The GUI was developed to interface with the camera and provide some additional functionality, such as tuning of camera parameters. For further documentation regarding the execution of this GUI for this project please see [the Technical README](README_technical.txt) and [the PyCapture2 README](README_PyCapture2.txt).
