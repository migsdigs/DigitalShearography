PyCapture2 is a wrapper for FLIR Integrated Imaging Solutions' FlyCapture 2 library.

FLIR Integrated Imaging Solutions' website is located at https://www.ptgrey.com

The PyCapture2 python extension provides a common software interface to control and acquire images from FLIR USB 3.0,
GigE, FireWire, and USB 2.0 cameras using the same API under 32- or 64-bit Windows.

--------------------------------------------------------------------------------------------------------------
Instructions on how to extract the PyCapture2 package and run the examples on Windows

Windows
=========================================================================
1. Ensure that python is installed on the system before installing PyCapture2 using the instructions below.
Note that the default install links on the official python website https://www.python.org/downloads/
is for 32-bit windows. To download the 64 bit version, click into the specific Python release version
to download the x64 installer.

PyCapture2 versions after 2.11.3.361 will require NumPy; run "pip install setuptools cython numpy" to install the required modules.

Example:
C:\Python27\python.exe -m pip install setuptools cython numpy

2. To ensure the prerequisites such as drivers and visual studio redistributables are installed on the system,
run the FlyCapture2 SDK installer that corresponds with the PyCapture2 version number. For example, if installing
PyCapture2 2.11.1, install the Flycapture2 SDK 2.11.1

If there is ever the need to reinstall drivers, they can also be installed using the Windows device manager
with the driver files located in the folder(s):
<Python Install path>\PyCapture2\driver64\
<Python Install path>\PyCapture2\driver\

3. Run the .msi installer to install the PyCapture2 python module into an existing python installation directory.
For example C:\Python27\


4. Choose the correct PyCapture2 .msi depending on the version of Python installed on your system.

	- PyCapture2-2.11.X.win-amd64-py3.5.msi is for Python version 3.5
	- PyCapture2-2.11.X.win-amd64-py2.7.msi is for Python version 2.7

5. Once installed, the PyCapture2 examples can be ran directly from the command prompt.

For example if PyCapture2 is installed for Python3.5 and the python install directory is in C:\Python35\, enter the following commmand:
"cd C:\Python35"
"python PyCapture2\examples\AsyncTriggerEx.py"


*** GENERAL NOTES ***

- If both versions of python 2.7 and 3.5 are installed on the system and you have installed both PyCapture2-py.2.7.msi and PyCapture2-py.3.5.msi, ensure to cd into the correct python directory before running the examples.

For example, to run with Python 2.7 and if it is installed in the directory C:\Python27\
"cd C:\Python27"
"python PyCapture2\examples\AsyncTriggerEx.py"

- The pgr_events_table.dat is required in order to run the EventsEx.py example. Ensure that the pgr_events_table.dat file is in the same directory as the directory where the examples are ran.

For example if the command prompt current directory is C:\Python27\PyCapture2\examples\
"cd C:\Python27\PyCapture2\examples\"
"C:\Python27\python EventsEx.py"
the pgr_events_table.dat needs to be in C:\Python27\PyCapture2\examples\pgr_events_table.dat

For example if the command prompt current directory is C:\Python27\
"cd C:\Python27\"
"C:\Python27\python PyCapture2\examples\EventsEx.py"
the pgr_events_table.dat needs to be in C:\Python27\pgr_events_table.dat
