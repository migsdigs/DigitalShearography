# Refinement of an Existing Digital Shearography Device and Development of a GUI for camera interaction

Authors : [Miguel Garcia Naude](https://github.com/migsdigs)

## Abstract

Digital Shearography is an optical non-destructive testing technique that is used to inspect objects for defects. The benefits of Non-destructive testing and in particular, Digital Shearography, has resulted in it being useful in maintenance and quality conformance in automotive and aeronautical industries. Most Digital Shearography devices make use of Michelson Interferometers as their shearing device,however devices making use of this shearing device are limited to having a small angular field of view. By incorporating a 4f system into a Michelson Interferometer based inspection device, the angular field of view of the system is no longer limited by the Michelson Interferometer, thus maximising the camera field of view. By developing a user-friendly GUI to interact with the developed inspection device, the Shearographic Inspection process is managed and fringe patterns resulting from real-time subtraction of images using Digital Shearography are displayed. This enables non-destructive tests to be effectively carried out in order to gather object defect information. 

## Excerpt of Results
|   |   |
|---|---|
| ![car_Static](/simulation_results/gifs/car_static.gif) <br> Static target|  ![car_dynamic](/simulation_results/gifs/car_dynamic.gif) <br> Adaptive target |
|![freethrow](/simulation_results/gifs/freethrow.gif) <br> Simple object tracking|  ![surveillance](/simulation_results/gifs/surveillance.gif) <br> Adaptive lighting confitions|

An excerpt of the results shown above allude to the advantages of dynamic colour targets for objects with slowly changing color distributions. Other results highlight the filters general ability to track, as well as highlighting the shortfalls of tracking under extremely dynamic lighting conditions.

## Running the code

Further documentation regarding the execution of the simulations produced for this project can be found in the ```examples``` folder of this repository.
