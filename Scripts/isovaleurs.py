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

# create a new 'Contour'
contour1 = Contour(Input=calculator1)
contour1.ContourBy = ['POINTS', 'DegreConversion']
contour1.Isosurfaces = [-18, -6, 6, 14, 22]
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ESSAI 1
# # get color transfer function/color map for 'DegreConversion'
# degreConversionLUT = GetColorTransferFunction('DegreConversion')
# degreConversionLUT.RGBPoints = [-17.620947265625, 0.235229, 0.42745, 0.756862, -7.0, 0.258823, 0.439215, 0.760784, 8.0, 0.865003, 0.865003, 0.865003, 20.0, 0.7254901960784313, 0.29411764705882354, 0.29411764705882354, 23.817529296875, 0.7254901960784313, 0.0, 0.0]
# degreConversionLUT.ColorSpace = 'Lab'
# degreConversionLUT.ScalarRangeInitialized = 1.0
#
# # get opacity transfer function/opacity map for 'DegreConversion'
# degreConversionPWF = GetOpacityTransferFunction('DegreConversion')
# degreConversionPWF.Points = [-17.620947265625, 0.0, 0.5, 0.0, 23.817529296875, 1.0, 0.5, 0.0]
# degreConversionPWF.ScalarRangeInitialized = 1

# ESSAI 2
# # get color transfer function/color map for 'DegreConversion'
# degreConversionLUT = GetColorTransferFunction('DegreConversion')
# degreConversionLUT.RGBPoints = [-17.620947265625, 0.235229, 0.42745, 0.756862, -6.999999999999984, 0.258823, 0.439215, 0.760784, 8.000000000000025, 0.865003, 0.865003, 0.865003, 20.00000000000001, 0.725490196078431, 0.294117647058824, 0.294117647058824, 23.81752929687502, 0.725490196078431, 0.0, 0.0]
# degreConversionLUT.ColorSpace = 'Lab'
# degreConversionLUT.ScalarRangeInitialized = 1.0
#
# # get opacity transfer function/opacity map for 'DegreConversion'
# degreConversionPWF = GetOpacityTransferFunction('DegreConversion')
# degreConversionPWF.Points = [-17.620947265625, 0.0, 0.5, 0.0, 23.817529296875023, 1.0, 0.5, 0.0]
# degreConversionPWF.ScalarRangeInitialized = 1
#
# # get color transfer function/color map for 'TMP2maboveground'
# tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
# tMP2mabovegroundLUT.RGBPoints = [255.529052734375, 0.235229, 0.42745, 0.756862, 266.15, 0.258823, 0.439215, 0.760784, 281.15, 0.865003, 0.865003, 0.865003, 293.15, 0.725490196078431, 0.294117647058824, 0.294117647058824, 296.967529296875, 0.725490196078431, 0.0, 0.0]
# tMP2mabovegroundLUT.ColorSpace = 'Lab'
# tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0
#
# # get opacity transfer function/opacity map for 'TMP2maboveground'
# tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
# tMP2mabovegroundPWF.Points = [-17.620947265625, 0.0, 0.5, 0.0, 296.9674987792969, 1.0, 0.5, 0.0]
# tMP2mabovegroundPWF.ScalarRangeInitialized = 1

# # ESSAI 3
# # get color transfer function/color map for 'TMP2maboveground'
# tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
# tMP2mabovegroundLUT.RGBPoints = [255.529052734375, 0.235229, 0.42745, 0.756862, 266.15, 0.258823, 0.439215, 0.760784, 281.15, 0.865003, 0.865003, 0.865003, 293.15, 0.725490196078431, 0.294117647058824, 0.294117647058824, 296.967529296875, 0.725490196078431, 0.0, 0.0]
# tMP2mabovegroundLUT.ColorSpace = 'Lab'
# tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0
#
# # get opacity transfer function/opacity map for 'TMP2maboveground'
# tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
# tMP2mabovegroundPWF.Points = [-17.620947265625, 0.0, 0.5, 0.0, 296.9674987792969, 1.0, 0.5, 0.0]
# tMP2mabovegroundPWF.ScalarRangeInitialized = 1

# ESSAI 4
# get color transfer function/color map for 'TMP2maboveground'
tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
tMP2mabovegroundLUT.InterpretValuesAsCategories = 1
tMP2mabovegroundLUT.RGBPoints = [255.14999389648438, 0.231373, 0.298039, 0.752941, 276.0587615966797, 0.865003, 0.865003, 0.865003, 296.967529296875, 0.705882, 0.0156863, 0.14902]
tMP2mabovegroundLUT.ColorSpace = 'Lab'
tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0
tMP2mabovegroundLUT.Annotations = ['255.15', '255.15', '267.15', '267.15', '279.15', '279.15', '287.15', '287.15', '295.15', '295.15']
tMP2mabovegroundLUT.IndexedColors = [0.23529411764705882, 0.42745098039215684, 0.7568627450980392, 0.25882352941176473, 0.4392156862745098, 0.7607843137254902, 0.8666666666666667, 0.8666666666666667, 0.9058823529411765, 0.7254901960784313, 0.39215686274509803, 0.39215686274509803, 0.7254901960784313, 0.0, 0.0]

# get opacity transfer function/opacity map for 'TMP2maboveground'
tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
tMP2mabovegroundPWF.Points = [255.14999389648438, 0.0, 0.5, 0.0, 296.967529296875, 1.0, 0.5, 0.0]
tMP2mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contour1
contour1Display = Show(contour1, renderView1)

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(threshold1)
# ----------------------------------------------------------------


# SAUVE UNE COPIE D ECRAN DANS UN FICHIER PNG
WriteImage(sys.argv[1]+"_isovaleurs.png")

# REALISE LE ROGNAGE DES PARTIES EXTERNES PAR L UTILITAIRE convert D IMAGEMAGICK, QUI DOIT ETRE INSTALLE SUR L OS
# os.system('convert -trim -define png:color-type=6' + sys.argv[1]+".png " + sys.argv[1]+".png")
