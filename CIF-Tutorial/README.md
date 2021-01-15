# How to create your own CIF files

***This tutorial is largely based on Stefaan Cottenier's course: [Computational Materials Physics](https://compmatphys.epotentia.com/), and can be treated as my personal lecture notes of the course.***

- Use the following template making the necessary adjustments:
```
#===============================================================================
# General-purpose P1 CIF
#===============================================================================

data_global
_chemical_name                     'Lead Oxide'
_cell_length_a                     3.99
_cell_length_b                     3.99
_cell_length_c                     5.01
_cell_angle_alpha                  90.
_cell_angle_beta                   90.
_cell_angle_gamma                  90.
_symmetry_space_group_name_H-M     'P 1'
_symmetry_Int_Tables_number        1

loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_symmetry_multiplicity
_atom_site_Wyckoff_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
O1  O  1 a  0.0  0.0  0.0
O2  O  1 a  0.5  0.5  0.5
Pb1 Pb 1 a  0.5  0.0  0.77
Pb2 Pb 1 a  0.0  0.5  0.23
```
- The problem with this file is that it does not include the symmetery information of the crystal, which is necessary for your DFT calculation. The crystal is defined using the P1 space group, which is the space group of least symmetry.

- To overcome this problem you need to use the [FINDSYM](https://stokes.byu.edu/iso/findsym.php) tool. In principle, it takes a P1 CIF file and return a CIF file with the "highest symmetry" of the crystal. However, FINDSYM is quite picky when it comes to CIF files. If you upload this template, it returns an error. To circumvent this difficulty, upload the template to the [Bilbao Crystallographic Server](https://www.cryst.ehu.es/).

- From the Bilbao Crystallographic Server home page, choose `Structure Utilities`, and then choose `VISUALIZE`.
- Upload your template, and click `Show`. The crystal will be viewed using `Jmol`.
- Scroll down and download the CIF file. It will look like this:
```
data_generated_by_bilbao_crystallographic_server

_cell_length_a                   3.99 
_cell_length_b                   3.99 
_cell_length_c                   5.01 
_cell_angle_alpha                90. 
_cell_angle_beta                 90. 
_cell_angle_gamma                90.        
_symmetry_space_group_name_H-M   'P1' 
_symmetry_Int_Tables_number      1 

loop_
_symmetry_equiv_pos_site_id
_symmetry_equiv_pos_as_xyz
1    'x,y,z'

loop_
_atom_site_label 
_atom_site_type_symbol 
_atom_site_symmetry_multiplicity 
_atom_site_Wyckoff_symbol 
_atom_site_fract_x 
_atom_site_fract_y 
_atom_site_fract_z 
O1     O ? 1a     0.00000  0.00000  0.00000
O2     O ? 1a     0.50000  0.50000  0.50000
Pb1   Pb ? 1a     0.50000  0.00000  0.77000
Pb2   Pb ? 1a     0.00000  0.50000  0.23000
```
A bit different than your previous file, but readable by `FINDSYM`.
- Go back to [FINDSYM](https://stokes.byu.edu/iso/findsym.php), upload the new CIF file, scroll down and clik `OK` to submit data.
- The new CIF file will show up. Scroll down and download it. Change the file's extension from `.txt` to `.cif`. It looks like this:
```
# CIF file created by FINDSYM, version 7.1

data_findsym-output
_audit_creation_method FINDSYM

_cell_length_a    3.9900000000
_cell_length_b    3.9900000000
_cell_length_c    5.0100000000
_cell_angle_alpha 90.0000000000
_cell_angle_beta  90.0000000000
_cell_angle_gamma 90.0000000000
_cell_volume      79.7597010000

_symmetry_space_group_name_H-M "P -4 m 2"
_symmetry_Int_Tables_number 115
_space_group.reference_setting '115:P -4 -2'
_space_group.transform_Pp_abc a,b,c;0,0,0

loop_
_space_group_symop_id
_space_group_symop_operation_xyz
1 x,y,z
2 -x,-y,z
3 -y,-x,-z
4 y,x,-z
5 -x,y,z
6 x,-y,z
7 y,-x,-z
8 -y,x,-z

loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_symmetry_multiplicity
_atom_site_Wyckoff_label
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_occupancy
_atom_site_fract_symmform
O1  O    1 a 0.00000 0.00000 0.00000 1.00000 0,0,0  
O2  O    1 c 0.50000 0.50000 0.50000 1.00000 0,0,0  
Pb1 Pb   2 g 0.00000 0.50000 0.23000 1.00000 0,0,Dz 

# end of cif
```
Notice that the space group has changed to `P -4 m 2`.
# Using the CIF file with CIF2Cell
- If you used this last CIF file with `cif2cell`:
```
$ cif2cell TiPt1.cif -p quantum-espresso -o TiPt.in
```
it will return an error:
```
Traceback (most recent call last):
  File "/usr/local/bin/cif2cell", line 1574, in <module>
    docstring = StandardDocstring()
  File "/usr/local/bin/cif2cell", line 1021, in StandardDocstring
    tmpstring2 += ". Reference number : "+ref.databasecode
TypeError: must be str, not NoneType
```
- To tackle this last problem, change the following lines in the CIF file:
```
data_findsym-output
_audit_creation_method FINDSYM
```
to:
```
data_findsym-output
_audit_creation_method FINDSYM
_cod_database_code None
```
- Also, change the following lines:
```
_symmetry_space_group_name_H-M "P -4 m 2"
_symmetry_Int_Tables_number 115
_space_group.reference_setting '115:P -4 -2'
_space_group.transform_Pp_abc a,b,c;0,0,0
```
to:
```
_space_group_name_Hall		'-P 2a 2a'
_symmetry_Int_Tables_number	51
```
- Notice that it is `_space_group_name_Hall` not `_symmetry_space_group_name_Hall`. The latter is supended in recent CIF file formats and shouldn't be used.
- To be able to change the last four lines related to the space group, you need to know the name of the space group `P -4 m 2` in the Hall notation.
- Go to [http://cci.lbl.gov/sginfo/hall_symbols.html](http://cci.lbl.gov/sginfo/hall_symbols.html).
- Search the space group by its number in the **Internation Tables for Crystallography, Vol. A**, which is 51 in our case.
- Scroll down to find the following:
```
51        P m m a       -P 2a 2a
51:ba-c   P m m b       -P 2b 2
51:cab    P b m m       -P 2 2b
51:-cba   P c m m       -P 2c 2c
51:bca    P m c m       -P 2c 2
51:a-cb   P m a m       -P 2 2a
```
- There are 6 possibilities to the 51st space group. To know which one to choose, look at the line: `_space_group.transform_Pp_abc a,b,c;0,0,0`.
- The letter combiniation is `a,b,c` which is not present in the 6 possibilities because it is the default choice. That is, `51` is equivalent to `51:abc`.
- Thus, the correct space group to choose is `-P 2a 2a`. Yo may use either single or double quotes in the CIF file.

Congratulations, you have created a *working* CIF file without knowing much about crystallography.
