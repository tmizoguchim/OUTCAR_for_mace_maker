# OUTCAR_for_mace_maker

This program is for modify OUTCAR using POSCAR.
For making train.xyz for MACE, OUTCAR should be include the compositional information in "POSCAR = " line. However, the compositional information would be missing in some methodology. In such case, this program can read the compositional information from the POSCAR in the same folder as OUTCAR, and replace the "POSCAR = " line with the composition.  
And the modified OUTCAR will be copied to the selected folder.

# Usage

```% python OUTCAR_for_mace_maker.py ````

You have to specify the source folder for searching and target folder for saving. 
```
input_folder = "/home/***/*** your current folder "
output_folder = "/home/+++/+++/OUTCAR-collection your saving folder "
```
Futheremore, you should specify the name of the folders for searching.
```
    if os.path.isdir(subdir_path) and '****' in subdir:

```

