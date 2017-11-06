import os

# Importation des donnees
os.system('RequeteAromeHD.py 0 SP1')
os.system('mv *.grib2 Donnees')

# Exportation au format nc
os.system('./wgrib2 Donnees/*.grib2 -netcdf Donnees/MesDonnees.nc')

# Traitement sur Paraview
# permet d'avoir des .png
os.system('visuAvecTemperature.py Donnees/MesDonnees.nc')

# Exportation au format KML
