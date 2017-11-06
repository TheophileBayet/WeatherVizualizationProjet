import sys
import os

# state file generated using paraview version 5.1.2

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.UseOffscreenRendering = True
renderView1.UseOffscreenRenderingForScreenshots = True
MonEchelle = 0.5
renderView1.ViewSize = [(int) (2801*MonEchelle),(int) (1791*MonEchelle)]
renderView1.InteractionMode = '2D'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [2., 46.45, 0.0]
renderView1.CameraPosition = [2., 46.45, 60.]
renderView1.CameraFocalPoint = [2., 46.45, 0.0]
renderView1.CameraParallelScale = 9.
renderView1.CameraParallelProjection = 1
renderView1.Background = [1.0, 1.0, 1.0]
renderView1.UseGradientBackground = 1

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
lecteurNC = NetCDFReader(FileName=[sys.argv[1]])
lecteurNC.Dimensions = '(latitude, longitude)'
lecteurNC.SphericalCoordinates = 0
lecteurNC.OutputType = 'Image'

# create a new 'Calculator'
conversionKelvinCelsius = Calculator(Input=lecteurNC)
conversionKelvinCelsius.ResultArrayName = 'TMPC_2maboveground'
conversionKelvinCelsius.Function = 'TMP_2maboveground-273.15'

# create a new 'Threshold'
seuillage = Threshold(Input=conversionKelvinCelsius)
seuillage.Scalars = ['POINTS', 'TMPC_2maboveground']
seuillage.ThresholdRange = [-100., 100.0]

# create a new 'Contour'
contour1 = Contour(Input=calculator1)
contour1.ContourBy = ['POINTS', 'CelsiusKelvinConversion']
contour1.Isosurfaces = [-18.6366, -12.774714285714289, -6.912828571428574, -1.050942857142859, 4.810942857142854, 10.672828571428571, 16.534714285714283, 22.3966]
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'TMP2maboveground'
tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
tMP2mabovegroundLUT.RGBPoints = [254.5133819580078, 0.231373, 0.298039, 0.752941, 275.0299758911133, 0.865003, 0.865003, 0.865003, 295.54656982421875, 0.705882, 0.0156863, 0.14902]
tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TMP2maboveground'
tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
tMP2mabovegroundPWF.Points = [254.5133819580078, 0.0, 0.5, 0.0, 295.54656982421875, 1.0, 0.5, 0.0]
tMP2mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contour1
contour1Display = Show(contour1, renderView1)

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(seuillage)
# ----------------------------------------------------------------


# SAUVE UNE COPIE D ECRAN DANS UN FICHIER PNG
WriteImage(sys.argv[1]+"_isovaleurs.png")

# REALISE LE ROGNAGE DES PARTIES EXTERNES PAR L UTILITAIRE convert D IMAGEMAGICK, QUI DOIT ETRE INSTALLE SUR L OS
# os.system('convert -trim -define png:color-type=6' + sys.argv[1]+".png " + sys.argv[1]+".png")
