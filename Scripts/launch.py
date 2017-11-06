import os

# Importation des donnees
os.system('python RequeteAromeHD.py 0 SP1')
os.system('mv *.grib2 ../Donnees')

# Exportation au format nc
os.system('../wgrib2 ../Donnees/*.grib2 -netcdf ../Donnees/MesDonnees.nc')

#Suppression des donnees grib2 parasites
os.system('rm ../Donnees/*.grib2')

# Traitement sur Paraview
# permet d'avoir des .png
os.system('pvpython temperatures.py ../Donnees/MesDonnees.nc')
#os.system('pvpython isovaleurs.py ../Donnees/MesDonnees.nc')
os.system('pvpython lignes_courant.py ../Donnees/MesDonnees.nc')
