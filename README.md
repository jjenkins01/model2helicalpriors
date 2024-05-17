model2helicalpriors is a python script for generating helical priors that can be used in relion helical reconstruction. 

See inital steps below.

Step 1: Within the desired PEET alignment directory, run createAlignedModel to generate updated particle coordinates.
For example: createAlignedModel "peet_alignment_base_name.prm"

Step 2: Run imodinfo with the "-l" option, and pass the output to a text file.
For example: imodinfo -l model_name.mod > model_information.txt

Step 3: Run this python script, providing the model_information.txt as input.
This script reads contour and point information in the input text file and will output a star file containing helical prior information.
This script is intended to be used alongside toRelionCoords, which generates a star file from the output of createAlignedModel.
Helical priors should be appended to the toRelionCoords star file before subtomogram export in Warp.
