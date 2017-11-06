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
mesDonneesnc = NetCDFReader(FileName=[sys.argv[1]])
mesDonneesnc.Dimensions = '(latitude, longitude)'
mesDonneesnc.SphericalCoordinates = 0
mesDonneesnc.ReplaceFillValueWithNan = 1
mesDonneesnc.OutputType = 'Image'

# create a new 'Threshold'
threshold1 = Threshold(Input=mesDonneesnc)
threshold1.Scalars = ['POINTS', 'TMP_2maboveground']
threshold1.ThresholdRange = [254.0, 300.0]

# create a new 'Calculator'
calculator1 = Calculator(Input=threshold1)
calculator1.ResultArrayName = 'DegreConversion'
calculator1.Function = 'TMP_2maboveground-273.15'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'DegreConversion'
degreConversionLUT = GetColorTransferFunction('DegreConversion')
degreConversionLUT.RGBPoints = [-18.636618041992165, 0.231373, 0.298039, 0.752941, 1.879975891113304, 0.865003, 0.865003, 0.865003, 22.396569824218773, 0.705882, 0.0156863, 0.14902]
degreConversionLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'DegreConversion'
degreConversionPWF = GetOpacityTransferFunction('DegreConversion')
degreConversionPWF.Points = [-18.636618041992165, 0.0, 0.5, 0.0, 22.396569824218773, 1.0, 0.5, 0.0]
degreConversionPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calculator1
calculator1Display = Show(calculator1, renderView1)

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(threshold1)
# ----------------------------------------------------------------


# SAUVE UNE COPIE D ECRAN DANS UN FICHIER PNG
WriteImage(sys.argv[1]+"_temp.png")

# REALISE LE ROGNAGE DES PARTIES EXTERNES PAR L UTILITAIRE convert D IMAGEMAGICK, QUI DOIT ETRE INSTALLE SUR L OS
# os.system('convert -trim -define png:color-type=6' + sys.argv[1]+".png " + sys.argv[1]+".png")
