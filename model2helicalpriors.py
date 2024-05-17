# Python script for generating helical prior used in relion helical reconstruction. See inital steps below.

# Step 1: Within the desired PEET alignment directory, run createAlignedModel to generate updated particle coordinates.
# For example: createAlignedModel "peet_alignment_base_name.prm"

# Step 2: Run imodinfo with the "-l" option, and pass the output to a text file.
# For example: imodinfo -l model_name.mod > model_information.txt

# Step 3: Run this python script, providing the model_information.txt as input.
# This script reads contour and point information in the input text file and will output a star file containing helical prior information.
# This script is intended to be used alongside toRelionCoords, which generates a star file from the output of createAlignedModel.
# Helical priors should be appended to the toRelionCoords star file before subtomogram export in Warp.


subvolume coordinates (XYZ) 
def extract_contour_data(input_file):
    contour_data = {}

    with open(input_file, 'r') as file:
        for line in file:
            tokens = line.split()
            if len(tokens) == 4 and tokens[1].isdigit() and tokens[2].isdigit():
                contour_num = int(tokens[1])
                num_points = int(tokens[2])
                length = float(tokens[3])
                if contour_num not in contour_data:
                    contour_data[contour_num] = {'num_points': num_points, 'lengths': []}
                contour_data[contour_num]['lengths'].append(length)

    return contour_data

def generate_star_file(input_file, output_star_file, spacing):
    contour_data = extract_contour_data(input_file)

    with open(output_star_file, 'w') as star_file:
        star_file.write("# version 30001\n")
        star_file.write("\ndata\n\n")
        star_file.write("loop_\n")
        star_file.write("_rlnHelicalTubeID #1\n")
        star_file.write("_rlnHelicalTrackLength #2\n")
        star_file.write("_rlnAngleTiltPrior #3\n")
        star_file.write("_rlnAnglePsiPrior #4\n")
        star_file.write("_rlnAnglePsiFlipRatio #5\n")

        for contour_num, data in contour_data.items():
            cumulative_length = 0
            for i in range(data['num_points']):
                star_file.write(f"{contour_num} {cumulative_length:.2f} 0 0 0.5\n")
                cumulative_length += spacing

if __name__ == "__main__":
    input_file = "model_information.txt"  # Replace with your model information
    output_star_file = "relion_helical_priors.star"  # Replace with your desired output star file name
    spacing_between_contours = 1.0  # Replace with the spacing between contours in voxels. This information is used to assign the correct helical track length (in Angstroms) for relion processing. 

    generate_star_file(input_file, output_star_file, spacing_between_contours)
