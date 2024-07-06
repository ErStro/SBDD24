import os

# Paths for creating the ranking list
vslist_directory = "D:\\Python\\SBDD\\Final_Project\\sbdd24\\Batch_Docking"
ligands_directory = "D:\\Python\\SBDD\\Final_Project\\sbdd24\\Batch_Docking\\Ligands_V1"
decoys_directory = "D:\\Python\\SBDD\\Final_Project\\sbdd24\\Batch_Docking\\Decoys_V1"

# Merge the results of the dockings into a ranked list regarding affinity
vslist = []

# Function to extract affinities from log files in a directory
def extract_affinities(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".log"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    if line.startswith("   1"):  # Look for the line with mode 1
                        parts = line.split()
                        affinity = float(parts[1])  # Extract the affinity value
                        ligand_name = os.path.splitext(filename)[0]
                        # Remove "results_" prefix if it exists
                        if ligand_name.startswith("results_"):
                            ligand_name = ligand_name[len("results_"):]
                        vslist.append((ligand_name, affinity))
                        break  # Exit the loop after finding mode 1

# Extract affinities from both Ligands and Decoys directories
extract_affinities(ligands_directory)
extract_affinities(decoys_directory)

# Sort results by affinity value (ascending order)
vslist.sort(key=lambda x: x[1])

# Write the sorted results to a new file in the output directory
with open(os.path.join(vslist_directory, "final_ranking.txt"), 'w') as output_file:
    for ligand_name, affinity in vslist:
        output_file.write(f"{ligand_name} -> {affinity} (kcal/mol)\n")
