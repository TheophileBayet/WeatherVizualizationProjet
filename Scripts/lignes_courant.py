import sys
import os

# state file generated using paraview version 4.4.0

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

# create a new 'Threshold' ( supprimer les NaN)
threshold1 = Threshold(Input=mesDonneesnc)
threshold1.Scalars = ['POINTS', 'TMP_2maboveground']
threshold1.ThresholdRange = [254.0, 300.0]

# create a new 'Calculator'( Conversion en Degres)
calculator1 = Calculator(Input=threshold1)
calculator1.ResultArrayName = 'DegreConversion'
calculator1.Function = 'TMP_2maboveground-273.15'

# create a new 'Calculator' ( Pour calculer les lignes de courant du vent)
calculator3 = Calculator(Input=calculator1)
calculator3.ResultArrayName = 'LignesCourant'
calculator3.Function = 'UGRD_10maboveground*iHat+VGRD_10maboveground*jHat'

# create a new 'Stream Tracer' ( tracage des lignes de courant )
streamTracer2 = StreamTracer(Input=calculator3,
    SeedType='High Resolution Line Source')
streamTracer2.Vectors = ['POINTS', 'LignesCourant']
streamTracer2.MaximumStreamlineLength = 28.0

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer2.SeedType.Point1 = [-13.501214132117621, 42.60412804920032, -6.328271240363392e-15]
streamTracer2.SeedType.Point2 = [14.498785867882379, 60.504129575079226, -6.328271240363392e-15]

# create a new 'Stream Tracer' ( tracage des lignes de courant bis )
streamTracer1 = StreamTracer(Input=calculator3,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['POINTS', 'LignesCourant']
streamTracer1.MaximumSteps = 5000
streamTracer1.MaximumStreamlineLength = 28.0

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-12.0, 37.5, 0.0]
streamTracer1.SeedType.Point2 = [16.0, 55.400001525878906, 0.0]
streamTracer1.SeedType.Resolution = 128

# create a new 'Stream Tracer' ( tracage des lignes de courant ter)
streamTracer3 = StreamTracer(Input=calculator3,
    SeedType='High Resolution Line Source')
streamTracer3.Vectors = ['POINTS', 'LignesCourant']
streamTracer3.MaximumStreamlineLength = 28.0

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer3.SeedType.Point1 = [-6.775774820230788, 34.52759601840739, -2.886579864025407e-15]
streamTracer3.SeedType.Point2 = [21.224225179769213, 52.42759754428629, -2.886579864025407e-15]


# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'DegreConversion'
degreConversionLUT = GetColorTransferFunction('DegreConversion')
degreConversionLUT.RGBPoints = [-17.620947265625, 0.235229, 0.42745, 0.756862, -7.0, 0.258823, 0.439215, 0.760784, 8.0, 0.865003, 0.865003, 0.865003, 20.0, 0.7254901960784313, 0.29411764705882354, 0.29411764705882354, 23.817529296875, 0.7254901960784313, 0.0, 0.0]
degreConversionLUT.ColorSpace = 'Lab'
degreConversionLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'DegreConversion'
degreConversionPWF = GetOpacityTransferFunction('DegreConversion')
degreConversionPWF.Points = [-17.620947265625, 0.0, 0.5, 0.0, 23.817529296875, 1.0, 0.5, 0.0]
degreConversionPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

## show data from calculator1
#calculator1Display = Show(calculator1, renderView1)

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1)
# show data from streamTracer2
streamTracer2Display = Show(streamTracer2, renderView1)
# show data from streamTracer3
streamTracer3Display = Show(streamTracer3, renderView1)

SetActiveSource(streamTracer1)


# SAUVE UNE COPIE D ECRAN DANS UN FICHIER PNG
WriteImage(sys.argv[1]+"_courants.png")

# REALISE LE ROGNAGE DES PARTIES EXTERNES PAR L UTILITAIRE convert D IMAGEMAGICK, QUI DOIT ETRE INSTALLE SUR L OS
# os.system('convert -trim -define png:color-type=6' + sys.argv[1]+".png " + sys.argv[1]+".png")
