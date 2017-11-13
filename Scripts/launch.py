import os

# Importation des donnees
os.system('echo SCRIPT DE GENERATION AUTOMATIQUE DE DONNES METEOS ')
os.system('echo ')
os.system('echo         ===  recuperation des donnees de meteo France ===')
os.system('python RequeteAromeHD.py 0 SP1')
os.system('mv *.grib2 ../Donnees')
os.system('echo ')
# Exportation au format nc
os.system('echo         === Exportation des donnees au format nc ===')
os.system('echo ')
os.system('../wgrib2 ../Donnees/*.grib2 -netcdf ../Donnees/MesDonnees.nc')
os.system('echo ')
#Suppression des donnees grib2 parasites
os.system('rm ../Donnees/*.grib2')

# Traitement sur Paraview
# permet d'avoir des .png
os.system('echo ')
os.system('echo         === Generation des images dans le dossier Images ===')
os.system('echo ')
os.system('echo 1. Generation des temperatures')
os.system('pvpython temperatures.py ../Donnees/MesDonnees.nc')
os.system('echo 2. Generation des isovaleurs')
os.system('pvpython isovaleurs.py ../Donnees/MesDonnees.nc')
os.system('echo 3. Generation des lignes de courant')
os.system('pvpython lignes_courant.py ../Donnees/MesDonnees.nc')
os.system('mv ../Donnees/*.png ../Images')

os.system('echo ')
os.system('echo             === Fin du script ===')
