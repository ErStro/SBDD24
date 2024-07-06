import subprocess
import os

# Define Autodock Vina variables
receptor = "D:\\Python\\SBDD\\Final_Project\\sbdd24\\Batch_Docking\\1a4g.pdbqt"
center_x = 7.578
center_y = 40.179
center_z = -14.709
size_x = 40
size_y = 40
size_z = 40

# Get the directory where the ligands are stored
working_directory = "D:\\Python\\SBDD\\Final_Project\\sbdd24\\Batch_Docking\\Ligands"

# Get all .pdbqt files in the ligand directory
ligand_files = [f for f in os.listdir(working_directory) if f.endswith('.pdbqt')]

# Path to Autodock Vina executable
vina_path = "D:\\Python\\SBDD\\Final_Project\\sbdd24\\Library\\bin\\vina.exe"

# Run Vina for each ligand
for ligand in ligand_files:
    ligand_path = os.path.join(working_directory, ligand)
    output_file = os.path.join(working_directory, f"results_{ligand.split('.')[0]}.pdbqt")
    log_file = os.path.join(working_directory, f"results_{ligand.split('.')[0]}.log")

    # Run Vina docking
    command = [
        vina_path, "--receptor", receptor, "--ligand", ligand_path,
        "--center_x", str(center_x), "--center_y", str(center_y), "--center_z", str(center_z),
        "--size_x", str(size_x), "--size_y", str(size_y), "--size_z", str(size_z),
        "--out", output_file, "--log", log_file
    ]

    # Print the command for debugging
    print("Running command:", " ".join(command))

    # Run the command
    subprocess.run(command, shell=True, check=True)