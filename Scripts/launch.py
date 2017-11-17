import os
import datetime
import time
import requests
import os.path
import sys


def KML_ScriptGeneration(Iterations):
        i = 0
        script_kml = open("generated_script.kml","w")
        script_kml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?> \n")
        script_kml.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\"> \n")
        script_kml.write("<Folder> \n")
        script_kml.write("<name>Temperature and wind informations at time "+ str(i) +" </name> \n")
        script_kml.write("<description>Ground overlay on France of temps and wind streams at time : "+str(i)+" </description> \n")
        while i<NbrPrevisions+1 :

            script_kml.write("<GroundOverlay> \n")
            script_kml.write("<TimeSpan>")
            script_kml.write("<begin>2017-11-"+str(16+i)+"</begin>\n")
            script_kml.write("<end>2017-11-"+str(16+i+1)+"</end>\n")
            script_kml.write("</TimeSpan> \n")
            script_kml.write("<name>Temperatures at time "+str(i)+"</name> \n")
            script_kml.write("<Icon> \n")
            script_kml.write("<href><![CDATA[../Images/MesDonnees_"+str(i)+".nc_temp.png]]></href> \n")
            script_kml.write("</Icon> \n")
            script_kml.write("<LatLonBox> \n")
            script_kml.write("<north>55.4</north> \n")
            script_kml.write("<south>37.5</south> \n")
            script_kml.write("<east>16</east> \n")
            script_kml.write("<west>-12</west> \n")
            script_kml.write("<rotation>0</rotation> \n")
            script_kml.write("</LatLonBox> \n")
            script_kml.write("</GroundOverlay> \n")

            script_kml.write("<GroundOverlay> \n")
            script_kml.write("<TimeSpan>\n")
            script_kml.write("<begin>2017-11-"+str(16+i)+"</begin>\n")
            script_kml.write("<end>2017-11-"+str(16+i+1)+"</end>\n")
            script_kml.write("</TimeSpan> \n")
            script_kml.write("<name>Isovalues of temperatures at time "+str(i)+" </name> \n")
            script_kml.write("<Icon> \n")
            script_kml.write("<href><![CDATA[../Images/MesDonnees_"+str(i)+".nc_isovaleurs.png]]></href> \n")
            script_kml.write("</Icon> \n")
            script_kml.write("<LatLonBox> \n")
            script_kml.write("<north>55.4</north> \n")
            script_kml.write("<south>37.5</south> \n")
            script_kml.write("<east>16</east> \n")
            script_kml.write("<west>-12</west> \n")
            script_kml.write("<rotation>0</rotation> \n")
            script_kml.write("</LatLonBox> \n")
            script_kml.write("</GroundOverlay> \n")

            script_kml.write("<GroundOverlay> \n")
            script_kml.write("<TimeSpan> \n")
            script_kml.write("<begin>2017-11-"+str(16+i)+"</begin>\n")
            script_kml.write("<end>2017-11-"+str(16+i+1)+"</end>\n")
            script_kml.write("</TimeSpan> \n")
            script_kml.write("<name>Wind streams at time "+str(i)+"</name> \n")
            script_kml.write("<Icon> \n")
            script_kml.write("<href><![CDATA[../Images/MesDonnees_"+str(i)+".nc_courants.png]]></href> \n")
            script_kml.write("</Icon> \n")
            script_kml.write("<LatLonBox> \n")
            script_kml.write("<north>55.4</north> \n")
            script_kml.write("<south>37.5</south> \n")
            script_kml.write("<east>16</east> \n")
            script_kml.write("<west>-12</west> \n")
            script_kml.write("<rotation>0</rotation> \n")
            script_kml.write("</LatLonBox> \n")
            script_kml.write("</GroundOverlay> \n")
            i+=1
        script_kml.write("</Folder> \n")
        script_kml.write("</kml> \n")
        script_kml.close()


#=================================================================================#
if __name__ == "__main__":
    os.system('echo ')
    os.system('echo SCRIPT DE GENERATION AUTOMATIQUE DE DONNES METEOS ')
    os.system('echo ')

    #  Lancement du script avec arguments
    if (len(sys.argv) == 2 ):
        os.system('echo .        ===  Recuperation et traitement des donnees de meteo France ===')
        os.system('echo ')
        NbrPrevisions = int(sys.argv[1])
        i=0
        #Importation des donnees
        while i<NbrPrevisions+1 :
                os.system('echo .        == Traitement de la donnee ' + str(i) + ' ==')
                os.system('python RequeteAromeHD.py ' + str(i) + ' SP1')
                os.system('echo ')
                os.system('mv *.grib2 ../Donnees')
                # Exportation au format nc
                os.system('../wgrib2 ../Donnees/*.grib2 -netcdf ../Donnees/MesDonnees_' + str(i) + '.nc')
                #Suppression de la donnee grib2 parasite :
                os.system('rm ../Donnees/*.grib2')
                os.system('echo ')

                #Traitement sur Paraview
                os.system('echo     1. Generation des temperatures')
                os.system('pvpython temperatures.py ../Donnees/MesDonnees_'+str(i)+'.nc')
                os.system('echo     2. Generation des isovaleurs')
                os.system('pvpython isovaleurs.py ../Donnees/MesDonnees_'+str(i)+'.nc')
                os.system('echo     3. Generation des lignes de courant')
                os.system('pvpython lignes_courant.py ../Donnees/MesDonnees_'+str(i)+'.nc')

                os.system('mv ../Donnees/*.png ../Images')
                os.system('echo ')
                i+=1
        os.system('')
        os.system('echo .         === FIN DU SCRIPT ===')
        KML_ScriptGeneration(NbrPrevisions)
        os.system('mv generated_script.kml ../KML')
        sys.exit(1)
        #Exportation au format nc


    if(len(sys.argv)==3):
            NbrPrevisions = int(sys.argv[1])
            os.system('echo         ===  Recuperation de la donnee '+str(NbrPrevisions)+' de meteo France ===')
            os.system('python RequeteAromeHD.py '+str(NbrPrevisions)+' SP1')
            os.system('mv *.grib2 ../Donnees')
            os.system('echo ')
            # Exportation au format nc
            os.system('echo         === Exportation de la donnee au format nc ===')
            os.system('echo ')
            os.system('../wgrib2 ../Donnees/*.grib2 -netcdf ../Donnees/MesDonnees_'+str(NbrPrevisions)+'.nc')
            os.system('echo ')
            #Suppression des donnees grib2 parasites
            os.system('rm ../Donnees/*.grib2')

            # Traitement sur Paraview
            # permet d'avoir des .png
            os.system('echo ')
            os.system('echo         === Generation de l\'image dans le dossier Images ===')
            os.system('echo ')
            os.system('echo 1. Generation des temperatures')
            os.system('pvpython temperatures.py ../Donnees/MesDonnees_'+str(NbrPrevisions)+'.nc')
            os.system('echo 2. Generation des isovaleurs')
            os.system('pvpython isovaleurs.py ../Donnees/MesDonnees_'+str(NbrPrevisions)+'.nc')
            os.system('echo 3. Generation des lignes de courant')
            os.system('pvpython lignes_courant.py ../Donnees/MesDonnees_'+str(NbrPrevisions)+'.nc')
            os.system('mv ../Donnees/*.png ../Images')

            os.system('echo ')
            os.system('echo             === Fin du script ===')
            sys.exit(1)
    #Lancement du script sans arguments : affichage de base
    if (len(sys.argv) == 1):
            #Importation des donnees
            os.system('echo         ===  Recuperation des donnees de meteo France ===')
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
            sys.exit(1)
