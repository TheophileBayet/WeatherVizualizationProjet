import os

# Importation des donnees
os.system('RequeteAromeHD.py 0 SP1')
os.system('mv *.grib2 Donnees')

# Exportation au format nc
os.system('./wgrib2 *.grib2 -netcdf MesDonnees.nc')

# Traitement sur Paraview
# permet d'avoir des .png


# Exportation au format KML
