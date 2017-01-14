import maya.cmds as cmds
import sys
#sys.path.append("C:/Program Files/Pixar/RenderManProServer-21.2/lib/python2.7/Lib/site-packages")
import ice


#createBaseLightBall = cmds.polySphere(n='baseLightBall',r=2,sx=40,sy=20,ch=0)



dir(__ice__)

fileName = "C:/temp/hdri/colorGrid_4k.exr"
#outputFileName = "C:/temp/hdri/colorGrid_4k.exr"
outputTempName = "C:/temp/hdri/colorGrid_4k_temp.jpg"
#format = ice.constants.FMT_EXRFLOAT
#format = ice.constants.FMT_TIFF8
#format = ice.constants.FMT_TIFF16
#format = ice.constants.FMT_TIFFFLOAT
#format = ice.constants.FMT_EXRHALF
#format = ice.constants.FMT_EXRFLOAT
#format = ice.constants.FMT_EXRUINT32
#format = ice.constants.FMT_PNG
format = ice.constants.FMT_JPEG


image = ice.Load(fileName)
saveFile = image
#imageResize = ice.Image.Reformat(image,[0,3999,0,1999])
#saveFile = ice.Image.Move(image,[300,300])


ice.Image.Save(saveFile,outputTempName,format)  #save file , name = outputTempName


imageResize = ice.Image.Reformat(image,[0,3999,0,1999])
image.Reformat([1000,500])



scaledImage = ice.Image.Scale(imageResize,[-1,1])


saveFile = ice.Image.Move(image,(500,300))

translateImage.Save(outputFileName, format)

ice.Image.Save(saveFile,outputTranslateFileName,format)

##test




cmds.select('*dyna_geo*')

cmds.select('*coin_paint*')

cmds.select('*dynaShape*')