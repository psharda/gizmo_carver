"""
   inputs_gizmo_carver.py

   Purpose:
        Input file for RadMC carving routines. This is the only file you should
        edit. Follow the comments below to see what each variable represents.

   Author:
        Sean Feng, feng.sean01@utexas.edu
        Spring 2022

        Modified from:
        inputs_CarveOut.py, written by
        Aaron T. Lee, aaron.t.lee@utexas.edu
        Spring 2018

        Written/Tested with Python 3.9, yt 4.0.2
        Further modified by Piyush Sharda (2023)
"""

from yt.units import *
import numpy as np

# Constants for calculating derived fields
dust_to_gas = 0.01
mol_hydrogen_ratio = 2.0
#microturbulence_speed = 1.77264e5 # cgs: based on the relation linewidth = 0.72 * (L/1pc)**0.56 km/s, where L is the size of the regridded cell. 
gamma = 5.0/3.0 # Note gamma is not constant and this function is an approximation.
helium_mass_fraction = 0.284 # Default mass fraction in Gizmo

# number fraction of target species
# molecular_abundance = 10**-4 # abundance of CO relative to H2

# ratio of 13C to 12C isotopes
c13_over_c12 = 1./50.
o18_over_o16 = 1./500 #TIMES paper: https://ui.adsabs.harvard.edu/abs/2021ApJS..256...16Y/abstract

# Mask abundance based on accreted particles
mask_abundance = False

# Units of the below box values ('pc','cm','AU','ly' accepted)
box_units = 'pc'

# x, y, z coordinates for the center of the carved domain (e.g., location of a star core)
# The values should match the unit given by box_units
#box_center = [15.95957649, 15.54566532, 15.19446488] #M2e3, center = 15
box_center = [48.55052441, 47.38566334, 49.65661156] #[49.52588194, 49.16974805, 49.712277] #[55.8,44.8, 57.2] # Core 1, 330  #M2e4 center = 50

# Routine will generate input files for a square area centered at box_center 
# extending to box_center += box_size on each side
# Use same units as box_units
box_size = 5.0 # pc (=L/2)

# Resolution of the resulting image (give as a complex number, e.g. for 
# box_dim = 64j, the resulting image will be 64x64)
box_dim = 256j

# Snapshot number
snap = '2000'

# Name tag for output file directory
tag = 'sn'+snap+'_'+ str(int(np.imag(box_dim)))+'_'

# Filepath of the HDF5 file name to read in
# If the HDF5 file is located in the same directory as the script files, 
# you can just put the file name
hdf5_dir = '/g/data/jh2/ps3459/starforge_data/32/'

# unit base to use for calculations
unit_base = {'UnitMagneticField_in_gauss':  1e+4,
             'UnitLength_in_cm'         : 3.08568e+18,
             'UnitMass_in_g'            :   1.989e+33,
             'UnitVelocity_in_cm_per_s' :      100}

# Filepath for directory containing input files that are not generated by the carver routine.
# These files are still necessary for running RADMC-3D. The files are:
# camera_wavelength_micron.inp
# dustkappa_silicate.inp
# dustopac.inp
# lines.inp
# molecule_nh3.inp (Or data file for other target species)
# radmc3d.inp
# wavelength_micron.inp
existing_filepath = '/g/data/jh2/ps3459/gizmo_carver/default_files/'

# Filepath for storing output files. Routine will make a working directory within this
# output directory for each run.
output_filepath = '/g/data/jh2/ps3459/gizmo_carver/output_files/'

# Write a new line file rather than use defaults file
write_line_file = True
# velocity max/min for the wavelength file
vmax = 20 # km/s
# number of wavelengths in output file
nwav = 256
# Line rest frequency, see molecule_x.inp file
restfreq_CO_J10 = 115.2712018e9
restfreq_CO_J21 = 230.5380000e9
restfreq_CO_J32 = 345.7959899e9
restfreq_CO_J43 = 461.0407682e9
restfreq_CO_J54 = 576.2679305e9
restfreq_CO_J65 = 691.4730763e9
restfreq_CO_J76 = 806.6518060e9
restfreq_CO_J87 = 921.7997000e9
restfreq_CO_J98 = 1036.9123930e9
restfreq_CO_J109 = 1151.9854520e9

restfreq_13CO_J10 = 110.2013542798e9
restfreq_13CO_J21 = 220.3986841281e9
restfreq_13CO_J32 = 330.5879652218e9
restfreq_13CO_J43 = 440.7651734547e9
restfreq_13CO_J54 = 550.9262850456e9
restfreq_13CO_J65 = 661.0672766472e9
restfreq_13CO_J76 = 771.1841254539e9
restfreq_13CO_J87 = 881.2728093107e9
restfreq_13CO_J98 = 991.3293068214e9
restfreq_13CO_J109 = 1101.3495974571e9

restfreq_C18O_J10 = 109.7821734e9
restfreq_C18O_J21 = 219.5603541e9
restfreq_C18O_J32 = 329.3305525e9
restfreq_C18O_J43 = 439.0887658e9
restfreq_C18O_J54 = 548.8310055e9
restfreq_C18O_J65 = 658.5532782e9
restfreq_C18O_J76 = 768.2515933e9
restfreq_C18O_J87 = 877.9219553e9
restfreq_C18O_J98 = 987.5603822e9
restfreq_C18O_J109 = 1097.1628753e9

restfreq_HCOp_J10 = 89.18852470e9
restfreq_HCOp_J21 = 178.37505630e9
restfreq_HCOp_J32 = 267.55762590e9
restfreq_HCOp_J43 = 356.73422300e9
restfreq_HCOp_J54 = 445.90287210e9
restfreq_HCOp_J65 = 535.06158100e9
restfreq_HCOp_J76 = 624.20836060e9
restfreq_HCOp_J87 = 713.34122780e9
restfreq_HCOp_J98 = 802.45819950e9
restfreq_HCOp_J109 = 891.55729030e9

restfreq_H13COp_J10 = 86.7542884e9
restfreq_H13COp_J21 = 173.5067003e9
restfreq_H13COp_J32 = 260.2553390e9
restfreq_H13COp_J43 = 346.9983440e9
restfreq_H13COp_J54 = 433.7338327e9
restfreq_H13COp_J65 = 520.4598843e9
restfreq_H13COp_J76 = 607.1746456e9
restfreq_H13COp_J87 = 693.8762612e9
restfreq_H13COp_J98 = 780.5628120e9
restfreq_H13COp_J109 = 867.2324263e9

restfreq_HCN_J10 = 88.63160220e9
restfreq_HCN_J21 = 177.26111120e9
restfreq_HCN_J32 = 265.88643390e9
restfreq_HCN_J43 = 354.50547730e9
restfreq_HCN_J54 = 443.11614850e9
restfreq_HCN_J65 = 531.71634790e9
restfreq_HCN_J76 = 620.30400220e9
restfreq_HCN_J87 = 708.87700510e9
restfreq_HCN_J98 = 797.43326230e9
restfreq_HCN_J109 = 885.97069490e9

restfreq_HNC_J10 = 90.66356800e9
restfreq_HNC_J21 = 181.32475800e9
restfreq_HNC_J32 = 271.98114200e9
restfreq_HNC_J43 = 362.63030300e9
restfreq_HNC_J54 = 453.26992200e9
restfreq_HNC_J65 = 543.89755400e9
restfreq_HNC_J76 = 634.51082600e9
restfreq_HNC_J87 = 725.10734100e9
restfreq_HNC_J98 = 815.68467600e9
restfreq_HNC_J109 = 906.24045900e9

# Output file names for use in RADMC3D
out_afname = "amr_grid.inp"       # output file name for amr grid
#out_codefaultname = "numberdens_CO_default.inp" # output file name for target species above
out_codespname = "numberdens_CO_despotic.inp" # output file name for target species (with despotic chemistry) above
out_couclname = "numberdens_CO_uclchem.inp" # output file name for target species (with UCLCHEM chemistry) above
out_13codespname = "numberdens_13CO_despotic.inp"
out_c18odespname = "numberdens_C18O_despotic.inp"
out_13couclname = "numberdens_13CO_uclchem.inp"
out_c18ouclname = "numberdens_C18O_uclchem.inp"

out_hcopdespname = "numberdens_HCOp_despotic.inp"
out_hcopuclname = "numberdens_HCOp_uclchem.inp"
out_h13copdespname = "numberdens_H13COp_despotic.inp"
out_h13copuclname = "numberdens_H13COp_uclchem.inp"

out_hcnuclname = "numberdens_HCN_uclchem.inp"
out_hncuclname = "numberdens_HNC_uclchem.inp"

out_nhname = "numberdens_h2.inp" # output file name for h2 number density
out_vfname = "gas_velocity.inp"   # output file name for velocity

out_tfname_CO = "gas_temperature_CO.inp"    # output file name for temperature
out_tfname_HCOp = "gas_temperature_HCOp.inp"
out_tfname_HCN = "gas_temperature_HCN.inp"
out_tfname_HCN = "gas_temperature_HNC.inp"

out_ddfname = "dust_density.inp" # output file name for dust density
out_dtfname = "dust_temperature.dat" # output for dust temperature (requires .dat)
out_mtfname = "microturbulence.inp" # output for microturbulence

# Names of existing files
out_molname_CO = 'molecule_co.inp' # (Or data file for other target species)
out_molname_13CO = 'molecule_13co.inp'
out_molname_C18O = 'molecule_c18o.inp'
out_molname_HCOp = 'molecule_hcop.inp'
out_molname_H13COp = 'molecule_h13cop.inp'
out_molname_HCN = 'molecule_hcn.inp'
out_molname_HNC = 'molecule_hnc.inp'

# Names of lines.inp files
out_linesname_CO = 'lines_co.inp'
out_linesname_13CO = 'lines_13co.inp'
out_linesname_C18O = 'lines_c18o.inp'
out_linesname_HCOp = 'lines_hcop.inp'
out_linesname_H13COp = 'lines_h13cop.inp'
out_linesname_HCN = 'lines_hcn.inp'
out_linesname_HNC = 'lines_hnc.inp'

out_wlmname = 'wavelength_micron.inp' #wavelength file for continuum radiative transfer: https://www.ita.uni-heidelberg.de/~dullemond/software/radmc-3d/manual_radmc3d/inputoutputfiles.html#sec-wavelengths

out_cwlname_CO_J10 = 'camera_wavelength_micron_COJ10.inp' #narrowly spaced wavelengths around restfreq for line radiative transfer
out_cwlname_CO_J21 = 'camera_wavelength_micron_COJ21.inp'
out_cwlname_CO_J32 = 'camera_wavelength_micron_COJ32.inp'
out_cwlname_CO_J43 = 'camera_wavelength_micron_COJ43.inp'
out_cwlname_CO_J54 = 'camera_wavelength_micron_COJ54.inp'
out_cwlname_CO_J65 = 'camera_wavelength_micron_COJ65.inp'
out_cwlname_CO_J76 = 'camera_wavelength_micron_COJ76.inp'
out_cwlname_CO_J87 = 'camera_wavelength_micron_COJ87.inp'
out_cwlname_CO_J98 = 'camera_wavelength_micron_COJ98.inp'
out_cwlname_CO_J109 = 'camera_wavelength_micron_COJ109.inp'

out_cwlname_13CO_J10 = 'camera_wavelength_micron_13COJ10.inp' #narrowly spaced wavelengths around restfreq for line radiative transfer
out_cwlname_13CO_J21 = 'camera_wavelength_micron_13COJ21.inp'
out_cwlname_13CO_J32 = 'camera_wavelength_micron_13COJ32.inp'
out_cwlname_13CO_J43 = 'camera_wavelength_micron_13COJ43.inp'
out_cwlname_13CO_J54 = 'camera_wavelength_micron_13COJ54.inp'
out_cwlname_13CO_J65 = 'camera_wavelength_micron_13COJ65.inp'
out_cwlname_13CO_J76 = 'camera_wavelength_micron_13COJ76.inp'
out_cwlname_13CO_J87 = 'camera_wavelength_micron_13COJ87.inp'
out_cwlname_13CO_J98 = 'camera_wavelength_micron_13COJ98.inp'
out_cwlname_13CO_J109 = 'camera_wavelength_micron_13COJ109.inp'

out_cwlname_C18O_J10 = 'camera_wavelength_micron_C18OJ10.inp' #narrowly spaced wavelengths around restfreq for line radiative transfer
out_cwlname_C18O_J21 = 'camera_wavelength_micron_C18OJ21.inp'
out_cwlname_C18O_J32 = 'camera_wavelength_micron_C18OJ32.inp'
out_cwlname_C18O_J43 = 'camera_wavelength_micron_C18OJ43.inp'
out_cwlname_C18O_J54 = 'camera_wavelength_micron_C18OJ54.inp'
out_cwlname_C18O_J65 = 'camera_wavelength_micron_C18OJ65.inp'
out_cwlname_C18O_J76 = 'camera_wavelength_micron_C18OJ76.inp'
out_cwlname_C18O_J87 = 'camera_wavelength_micron_C18OJ87.inp'
out_cwlname_C18O_J98 = 'camera_wavelength_micron_C18OJ98.inp'
out_cwlname_C18O_J109 = 'camera_wavelength_micron_C18OJ109.inp'

out_cwlname_HCOp_J10 = 'camera_wavelength_micron_HCOpJ10.inp' #narrowly spaced wavelengths around restfreq for line radiative transfer
out_cwlname_HCOp_J21 = 'camera_wavelength_micron_HCOpJ21.inp'
out_cwlname_HCOp_J32 = 'camera_wavelength_micron_HCOpJ32.inp'
out_cwlname_HCOp_J43 = 'camera_wavelength_micron_HCOpJ43.inp'
out_cwlname_HCOp_J54 = 'camera_wavelength_micron_HCOpJ54.inp'
out_cwlname_HCOp_J65 = 'camera_wavelength_micron_HCOpJ65.inp'
out_cwlname_HCOp_J76 = 'camera_wavelength_micron_HCOpJ76.inp'
out_cwlname_HCOp_J87 = 'camera_wavelength_micron_HCOpJ87.inp'
out_cwlname_HCOp_J98 = 'camera_wavelength_micron_HCOpJ98.inp'
out_cwlname_HCOp_J109 = 'camera_wavelength_micron_HCOpJ109.inp'

out_cwlname_H13COp_J10 = 'camera_wavelength_micron_H13COpJ10.inp' #narrowly spaced wavelengths around restfreq for line radiative transfer
out_cwlname_H13COp_J21 = 'camera_wavelength_micron_H13COpJ21.inp'
out_cwlname_H13COp_J32 = 'camera_wavelength_micron_H13COpJ32.inp'
out_cwlname_H13COp_J43 = 'camera_wavelength_micron_H13COpJ43.inp'
out_cwlname_H13COp_J54 = 'camera_wavelength_micron_H13COpJ54.inp'
out_cwlname_H13COp_J65 = 'camera_wavelength_micron_H13COpJ65.inp'
out_cwlname_H13COp_J76 = 'camera_wavelength_micron_H13COpJ76.inp'
out_cwlname_H13COp_J87 = 'camera_wavelength_micron_H13COpJ87.inp'
out_cwlname_H13COp_J98 = 'camera_wavelength_micron_H13COpJ98.inp'
out_cwlname_H13COp_J109 = 'camera_wavelength_micron_H13COpJ109.inp'

out_cwlname_HCN_J10 = 'camera_wavelength_micron_HCNJ10.inp' #narrowly spaced wavelengths around restfreq for line radiative transfer
out_cwlname_HCN_J21 = 'camera_wavelength_micron_HCNJ21.inp'
out_cwlname_HCN_J32 = 'camera_wavelength_micron_HCNJ32.inp'
out_cwlname_HCN_J43 = 'camera_wavelength_micron_HCNJ43.inp'
out_cwlname_HCN_J54 = 'camera_wavelength_micron_HCNJ54.inp'
out_cwlname_HCN_J65 = 'camera_wavelength_micron_HCNJ65.inp'
out_cwlname_HCN_J76 = 'camera_wavelength_micron_HCNJ76.inp'
out_cwlname_HCN_J87 = 'camera_wavelength_micron_HCNJ87.inp'
out_cwlname_HCN_J98 = 'camera_wavelength_micron_HCNJ98.inp'
out_cwlname_HCN_J109 = 'camera_wavelength_micron_HCNJ109.inp'

out_cwlname_HNC_J10 = 'camera_wavelength_micron_HNCJ10.inp' #narrowly spaced wavelengths around restfreq for line radiative transfer
out_cwlname_HNC_J21 = 'camera_wavelength_micron_HNCJ21.inp'
out_cwlname_HNC_J32 = 'camera_wavelength_micron_HNCJ32.inp'
out_cwlname_HNC_J43 = 'camera_wavelength_micron_HNCJ43.inp'
out_cwlname_HNC_J54 = 'camera_wavelength_micron_HNCJ54.inp'
out_cwlname_HNC_J65 = 'camera_wavelength_micron_HNCJ65.inp'
out_cwlname_HNC_J76 = 'camera_wavelength_micron_HNCJ76.inp'
out_cwlname_HNC_J87 = 'camera_wavelength_micron_HNCJ87.inp'
out_cwlname_HNC_J98 = 'camera_wavelength_micron_HNCJ98.inp'
out_cwlname_HNC_J109 = 'camera_wavelength_micron_HNCJ109.inp'


out_dksname = 'dustkappa_silicate.inp'
out_dtpname = 'dustopac.inp'
out_rmcname = 'radmc3d.inp'
out_execute = 'radmc3d'

out_jobscript_CO = 'job_co.sh'
out_jobscript_13CO = 'job_13co.sh'
out_jobscript_C18O = 'job_c18o.sh'
out_jobscript_HCOp = 'job_hcop.sh'
out_jobscript_H13COp = 'job_h13cop.sh'
out_jobscript_HCN = 'job_hcn.sh'
out_jobscript_HNC = 'job_hnc.sh'

out_makeinput = 'input_info.txt' # Save the setup parameters and output
out_extra1 = 'radmc_moments.py'
out_extra2 = 'recreate_cube.py'
out_extra3 = 'check_radmc_input.py'
out_extra4 = 'radmc_image_processing.py'
out_extra5 = 'get_coldens_from_pytreegrav.py' #file to get the column densities from pytreegrav RT
