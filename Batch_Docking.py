import subprocess
import os

# Define Autodock Vina variables
center_x = 7.578
center_y = 40.179
center_z = -14.709
size_x = 40
size_y = 40
size_z = 40

# Define paths
receptor = "D:\\Python\\SBDD\\Final_Project\\sbdd24\\Batch_Docking\\1a4g.pdbqt"
sdf_file = "D:\\Python\\SBDD\\Final_Project\\sbdd24\\Batch_Docking\\na-ligands.sdf"
output_folder = "D:\\Python\\SBDD\\Final_Project\\sbdd24\\Batch_Docking\\Ligands"
vina_path = "D:\\Python\\SBDD\\Final_Project\\sbdd24\\Library\\bin\\vina.exe"
vslist_directory = "D:\\Python\\SBDD\\Final_Project\\sbdd24\\Batch_Docking"

# Split the multi-ligand SDF file into individual ligand files
split_command = f'obabel {sdf_file} -O {output_folder}\\ligand_.sdf -m'
subprocess.run(split_command, shell=True, check=True)

# Get all split ligand SDF files
ligand_sdf_files = [f for f in os.listdir(output_folder) if f.startswith('ligand_') and f.endswith('.sdf')]

# Convert each SDF ligand file to PDBQT with hydrogens and partial charges using Open Babel
for ligand_sdf in ligand_sdf_files:
    ligand_sdf_path = os.path.join(output_folder, ligand_sdf)
    ligand_pdbqt = ligand_sdf.replace('.sdf', '.pdbqt')
    ligand_pdbqt_path = os.path.join(output_folder, ligand_pdbqt)
    obabel_command = f'obabel {ligand_sdf_path} -O {ligand_pdbqt_path} -p --partialcharge'
    subprocess.run(obabel_command, shell=True, check=True)

# Get all converted PDBQT ligand files
ligand_files = [f for f in os.listdir(output_folder) if f.endswith('.pdbqt') and f.startswith('ligand_')]

# Run Vina for each ligand
for ligand in ligand_files:
    ligand_path = os.path.join(output_folder, ligand)
    output_file = os.path.join(output_folder, f"results_{ligand.split('.')[0]}.pdbqt")
    log_file = os.path.join(output_folder, f"results_{ligand.split('.')[0]}.log")

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