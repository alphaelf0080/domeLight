import sys
sys.path.append("C:/Program Files/Pixar/RenderManProServer-21.2/lib/python2.7/Lib/site-packages")
import ice
import maya.cmds as cmds

## input File ##
fileName = 'C:/Program Files/Pixar/RenderManProServer-21.2/lib/RenderManAssetLibrary/EnvironmentMaps/Outdoor/LuxoJr.rma/Luxo-Jr_4000x2000.tex'
image = ice.Load(fileName)
#image = ice.Card(ice.constants.FLOAT, [1.0, 0.5, 0.3])


## output File jpg format ##

outputFileName = "d:/temp/aaa.jpg"
format = ice.constants.FMT_JPEG

image.SetMetaDataItem('JPEG_QUALITY', 100)
image.Save(outputFileName,format)
#image.Save(outputFileName, ice.constants.FMT_EXRFLOAT)


## output file exr16 format
outputFileName = "d:/temp/aaa_EXRFloat16.exr"
format = ice.constants.FMT_EXRHALF
image.Save(outputFileName,format)

## output file exr32 format
outputFileName = "d:/temp/aaa_EXRFloat32.exr"
format = ice.constants.FMT_EXRFLOAT
image.Save(outputFileName,format)



## output file tif8 format
outputFileName = "d:/temp/aaa_TIF8.tif"
format = ice.constants.FMT_TIFF8
image.Save(outputFileName,format)

## output file tif16 format
outputFileName = "d:/temp/aaa_TIF16.tif"
format = ice.constants.FMT_TIFF16
image.Save(outputFileName,format)

## output file tif32 format
outputFileName = "d:/temp/aaa_TIF32.tif"
format = ice.constants.FMT_TIFFFLOAT
image.Save(outputFileName,format)

## get metaData
ice.Image.GetMetaData(image)

## get image box
ice.Image.DataBox(image)

                       
## reSize reFormat to newSize                       
imageResizeDiff = ice.Image.Reformat(image,[0,39,0,19])
imageResizeSpec = ice.Image.Reformat(image,[0,0,3999,1999])

outputFileNameA = "d:/temp/bbb.jpg"
outputFileNameB = "d:/temp/bbb.exr"
formatA = ice.constants.FMT_JPEG
formatB = ice.constants.FMT_EXRHALF
imageResize.SetMetaDataItem('JPEG_QUALITY', 100)
imageResizeSpec.Save(outputFileNameA,formatA)
imageResizeDiff.Save(outputFileNameB,formatB)


