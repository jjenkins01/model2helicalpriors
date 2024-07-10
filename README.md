![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
[![DOI](https://img.shields.io/badge/DOI-10.1038%2Fs41586--024--07680--x-blue)](https://doi.org/10.1038/s41586-024-07680-x)
![IMOD](https://img.shields.io/badge/software-IMOD-ff69b4?logo=appveyor)
![PEET](https://img.shields.io/badge/software-PEET-4EAA25?logo=appveyor)


model2helicalpriors is a python script for generating helical priors that can be used in relion helical reconstruction. 

The following helical priors will be written to a star file:

1. rlnHelicalTubeID #This corresponds to the contour number in the input file
2. rlnHelicalTrackLength #This is the associated, cumulative length (in voxels) for each model
3. rlnAngleTiltPrior #set to zero
4. rlnAnglePsiPrior #set to zero
5. rlnAnglePsiFlipRatio #prior orientation knowledge, set to 0.5 to allow relion to refine.

Before running the script we need to perform some initial steps using commands in PEET and IMOD.

[https://bio3d.colorado.edu/PEET/]

[https://bio3d.colorado.edu/imod/]

[https://bio3d.colorado.edu/ftp/PEET/man/html/man1/createAlignedModel.1.html]

Step 1: Within the desired PEET alignment directory, run createAlignedModel to generate updated particle coordinates.

For example: 

```createAlignedModel "peet_alignment_base_name.prm"```

Step 2: Run imodinfo with the "-l" option, and pass the output to a text file.

For example: 

```imodinfo -l model_name.mod > model_information.txt```

Step 3: Now we can run this python script, providing the model_information.txt as input. Note that python 3.6+ is required.

For example:

```python model2helicalpriors.py```

This script reads contour and point information in the input text file and will output a star file containing the helical prior information.
This script is intended to be used alongside toRelionCoords, which generates a star file from the output of createAlignedModel.
Helical priors should be appended to the toRelionCoords star file before subtomogram export in Warp.
