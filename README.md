DOCKING INSTRUCTIONS:

This is done using the target 1a4g

- Create an environment with conda and Python 3.10
- Install AutoDock Vina, openbabel and meeko in the environment
- Download AutoDockTools (https://ccsb.scripps.edu/mgltools/downloads/)
- Download pdb of receptor
- Extract sdf of ligands and decoys
- Download the python script for batch docking and vs ranking
- Put the sdf and pdb files in the folder with your python code
- Use OpenBabel to prepare the pdb receptor file by adding hydrogens and partial charges using this command in the console:

(sbdd24) <receptor folder>obabel 1a4g.pdb -O 1a4g_prepared.pdb -p --addtotors --partialcharge

Note: the ligand and decoys files are pepared using built-in openbabel command in the batch-docking script.

- Another option (which I used) open the AutoDockTools app and follow these steps: load receptor pbd, delete Waters, add polar hydrogens, add charges, select the receptor in grid, download the pbdqt file. See first part of YouTube video (https://www.youtube.com/watch?v=BLbXkhqbebs). This video shows how to do the docking in general with vina.

- To get the data for the center and size of the docking box of the python script, execute the AutoDockTools file. Open 1a4g.pdb file, then click on grid -> macromolecule -> open, and choose the 1a4g.pdbqt file. Then, click grid -> grid box. This will give you the data you need to put on the python script.

- Apply the Python script for batch docking using the command: Python Batch_Docking.py. This is how it looks in my cdm:
(D:\Python\SBDD\Final_Project\sbdd24) D:\Python\SBDD\Final_Project\sbdd24\Batch_Docking>python Batch_Docking.py

Batch_Docking is the folder where I have the Python scripts, the 1a4g pbd and pdbtq files, the sdf files for the ligands and the decoys, and the folders of Ligands and Decoys. The python script does not do the docking of both ligands and decoys at the same time, one must change the file and folder names from ligands to decoys. The result of this script is the prepared ligand and decoys pdbqt files, docking results in pdbqt, and docking results in .log files in each of the folders.

- Apply the Python script VS_Ranking using the command: Python VS_Ranking.py. This is how it looks in my cdm:
(D:\Python\SBDD\Final_Project\sbdd24) D:\Python\SBDD\Final_Project\sbdd24\Batch_Docking>python VS_Ranking.py

This will give a .txt file called final_ranking with the dockings of both ligands and decoys ranked from best to worst. To apply this, the batch docking script must first be applied for ligands and decoys so their folders contain the necessary results for ranking.

Note: the python code must be modified to adjust to the folders and directories of the user, as well as adjusting the parameters of vina depending on the target (center and size)
Note: addtotors is used to ensure that rotatable bonds are correctly identified and marked in the receptor, and then correctly identified in the file conversion.
