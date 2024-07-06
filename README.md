DOCKING INSTRUCTIONS:

This is done using the target 1a4g

- Create an environment with conda and Python 3.10
- Install AutoDock Vina, openbabel and meeko in the environment
- Download AutoDockTools (https://ccsb.scripps.edu/mgltools/downloads/)
- Download pdb of receptor
- Extract sdf of ligands and decoys
- Download the python script for batch docking
- Put the sdf and pdb files in the folder with your python code
- Use OpenBabel to prepare the pdb receptor file by adding hydrogens and partial charges using this command in the console:

(sbdd24) <receptor folder>obabel 1a4g.pdb -O 1a4g_prepared.pdb -p --addtotors --partialcharge

- Convert receptor to PDBQT with this command:

obabel 1a4g_prepared.pdb -O 1a4g.pdbqt --addtotors

- Another option (which I used) open the AutoDockTools app and follow these steps: load receptor pbd, delete Waters, add polar hydrogens, add charges, select the receptor in grid, download the pbdqt file. See first part of YouTube video (https://www.youtube.com/watch?v=BLbXkhqbebs). This video shows how to do the docking in general with vina.

- Split the na-ligands.sdf file into individual files and convert them, repeat with decoys:

obabel na-ligands.sdf -O ligand.pdbqt -m

- Put these ligands.pdbqt in a folder called Ligands, and decoys in a folder called Decoys

- To get the data for the center and size of the docking box of the python script, execute the AutoDockTools file. Open 1a4g.pdb file, then click on grid -> macromolecule -> open, and choose the 1a4g.pdbqt file. Then, click grid -> grid box. This will give you the data you need to put on the python script.

- Apply the Python script using the command: Python Batch_Docking.py. This is how it looks in my cdm:
(D:\Python\SBDD\Final_Project\sbdd24) D:\Python\SBDD\Final_Project\sbdd24\Batch_Docking>python Batch_Docking.py

Batch_Docking is the folder where I have the Python script, the 1a4g pbd and pdbtq files, the sdf files for the ligands and the decoys, and the folders of Ligands and Decoys, which contain the pdbqt files for ligands and decoys.


# addtotors is used to ensure that rotatable bonds are correctly identified and marked in the receptor, and then correctly identified in the file conversion.
