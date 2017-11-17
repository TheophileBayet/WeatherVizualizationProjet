Projet de Visualisation scientifique réalisé par : 
-Jandin Wendy
-Bayet Théophile

Utilisation : 
	    Dossiers : 
	    	     /Scripts : Les scripts pythons utilisés pour gérer les données (téléchargement, traitement, stockage).
		     /KML : Les scripts KML utilisés pour visualiser les données sur google earth.
		     /Images : Les images générées par les scripts pythons.
		     /Donnees : Les données qui ne sont pas supprimées.

	    Lancement : 
	    	      cd /Scripts 

		      Le script launch.py peut prendre 0, 1 ou 2 arguments : 
		      -python launch.py génère 3 images dans le dossier /Images, correspondant au traitement des dernières données de météoFrance ( requeteHD 0 SP1 ). Ces images peuvent être affichées via le script KML affichage_carte.kml.
 
		      -python launch.py X génère 3*X images dans le dossier /IMages, ainsi qu'un script generated_script dans /KML, ce dernier permettant d'afficher via une animation l'évolution prévue par les données météoFrance sur le laps de temps X. ( exemple : python launch.py 3 )
 
		      -python launch.py X Y génère juste les 3 images correspondant au traitement de la donnée X dans les prévisions de météofrance, et les place dans le dossier /Images. 'Y' peut être n'importe quoi, cela importe peu. ( exemple : python launch.py 6 bis  // python launch.py 5 youplaboum ) 


            Affichage sur Google Earth : 
	    	      Lancer le script launch.py comme décrit précédemment afin d'obtenir les données que vous souhaitez. 
		      Ouvrir le script affichage_carte.kml pour afficher les données uniquement pour les dernières en dates.
		      Ouvrir le script generated_script.kml pour afficher une animation des prévisions de météoFrance sur le temps que vous avez choisi en lançant le script python.

Bonne utilisation.
Questions : 
wendy.jandin@grenoble-inp.org
theophile.bayet@grenoble-inp.org
