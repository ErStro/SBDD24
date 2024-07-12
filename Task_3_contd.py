import os
import numpy as np

# Define paths
project_dir = "/mnt/c/Work/AMI/SBDD_project"
experimental_ligand_file = os.path.join(project_dir, "experimental_ligand_redocked.pdbqt")
ligands_dir = os.path.join(project_dir, "ligands")


def read_pdbqt_coordinates(pdbqt_file):
    coordinates = []
    with open(pdbqt_file, 'r') as f:
        for line in f:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                coordinates.append([x, y, z])
    return np.array(coordinates)


def calculate_rmsd(experimental_coords, predicted_coords):
    # Check if the number of atoms match (not necessary for direct comparison)
    N = min(len(experimental_coords), len(predicted_coords))

    # Calculate RMSD
    rmsd = np.sqrt(np.sum(np.square(experimental_coords[:N] - predicted_coords[:N])) / N)

    return rmsd


# Read experimental ligand coordinates
experimental_coords = read_pdbqt_coordinates(experimental_ligand_file)

# Get all predicted ligand files
predicted_files = [f for f in os.listdir(ligands_dir) if f.startswith("results_ligand_") and f.endswith(".pdbqt")]

# Calculate RMSD for each predicted ligand
rmsd_results = []
for predicted_file in predicted_files:
    predicted_file_path = os.path.join(ligands_dir, predicted_file)
    predicted_coords = read_pdbqt_coordinates(predicted_file_path)

    try:
        rmsd_value = calculate_rmsd(experimental_coords, predicted_coords)
        rmsd_results.append((predicted_file, rmsd_value))
    except Exception as e:
        print(f"Error calculating RMSD for {predicted_file}: {e}")

# Sort the results by RMSD value
rmsd_results.sort(key=lambda x: x[1])

# Print the results
print("\nRMSD Results:")
for ligand, rmsd in rmsd_results:
    print(f"Ligand: {ligand}, RMSD: {rmsd:.3f} Å")
