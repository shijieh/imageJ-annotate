# imageJ-annotate

This repository contains code used to (1)automate the ImageJ cell counter (auto_run.ijm) and (2) visualize the cell counter results with manual clicking (annotate.py)

## Automate ImageJ with auto_run.ijm
The file auto_run.ijm is a macro that contains a series of ImageJ commands. These commands automate the cell counting process using ImageJ. To execute the commands, first load the raw image file (e.g., the raw_picture.jpg file included in the repository as a demonstration). Then, go to Plugins -> Macros -> Run, and select the auto_run_ijm file as the macro file. Fiji will then automatically conduct a cell counting and save the results into the Fiji_data.csv file. 

## Visualization with annotate.ipynb
The annotate.ipynb file is a python script that takes the Fiji cell counting results (Fiji_data.csv) and the manual clicking results (manual_clicking_data.csv) as input. It then overlays the cell locations from both method on the raw image file (raw_picture.jpg). 
