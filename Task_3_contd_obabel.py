import subprocess
import os
import tempfile

# Define paths and filenames
project_dir = "/mnt/c/Work/AMI/SBDD_project"
experimental_ligand_file = os.path.join(project_dir, "experimental_ligand_redocked.pdbqt")
ligands_dir = os.path.join(project_dir, "ligands")

# Function to calculate RMSD and save aligned ligand to temporary file
def calculate_rmsd(predicted, experimental):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdbqt") as temp_aligned:
            command = f'obabel -ipdbqt "{predicted}" -ipdbqt "{experimental}" --align --rmsd --quiet -opdbqt -O {temp_aligned.name}'
            subprocess.run(command, shell=True, check=True)

            # Calculate RMSD using the aligned ligand
            rmsd_command = f'obabel -ipdbqt {temp_aligned.name} -ormsd'
            result = subprocess.run(rmsd_command, shell=True, capture_output=True, text=True, check=True)
            rmsd_value = float(result.stdout.strip())

            # Return RMSD value and aligned ligand filename (temp_aligned.name)
            return rmsd_value, temp_aligned.name
    except subprocess.CalledProcessError as e:
        print(f"Error calculating RMSD for {predicted} and {experimental}:\n{e.stdout}\n{e.stderr}")
        return None, None

# Get all PDBQT files in the ligands directory
ligand_files = [os.path.join(ligands_dir, f) for f in os.listdir(ligands_dir) if f.startswith('results_') and f.endswith('.pdbqt')]

# Calculate RMSD for each ligand in the ligands directory
rmsd_results = []
for ligand in ligand_files:
    rmsd_value, aligned_ligand = calculate_rmsd(ligand, experimental_ligand_file)
    if rmsd_value is not None:
        rmsd_results.append((ligand, rmsd_value, aligned_ligand))

# Sort the results by RMSD
rmsd_results.sort(key=lambda x: x[1])  # Sort by RMSD value

# Print the results
for ligand, rmsd, aligned_ligand in rmsd_results:
    print(f"Ligand: {os.path.basename(ligand)}, RMSD: {rmsd:.3f} Å, Aligned Ligand: {os.path.basename(aligned_ligand)}")
