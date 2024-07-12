import subprocess
import os

# Define paths and filenames
project_dir = "/mnt/c/Work/AMI/SBDD_project"
receptor_file = os.path.join(project_dir, "1a4g.pdbqt")
ligand_file = os.path.join(project_dir, "zanamivir_prepared")
output_file = os.path.join(project_dir, "experimental_ligand_redocked.pdbqt")
vina_path = "/home/yahya/AutoDock-Vina/build/linux/release"

# Define Vina docking parameters
center_x = 7.578
center_y = 40.179
center_z = -14.709
size_x = 40
size_y = 40
size_z = 40

# Change the working directory to where Vina executable is located
os.chdir(vina_path)

# Prepare the Vina command
command = [
    "./vina",  # Assuming 'vina' is the executable name in the vina_path directory
    "--receptor", receptor_file,
    "--ligand", ligand_file,
    "--center_x", str(center_x),
    "--center_y", str(center_y),
    "--center_z", str(center_z),
    "--size_x", str(size_x),
    "--size_y", str(size_y),
    "--size_z", str(size_z),
    "--out", output_file
]

# Print the command for debugging
print(f"Running command: {' '.join(command)}")

# Run the command and capture output
try:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    print(f"Docking completed successfully.\nOutput:\n{result.stdout}")
    print(f"Errors (if any):\n{result.stderr}")
except subprocess.CalledProcessError as e:
    print(f"Error running Vina:\n{e.stdout}\n{e.stderr}")
