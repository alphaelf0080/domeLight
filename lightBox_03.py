import maya.cmds as cmds
import sys
sys.path.append("C:/Program Files/Pixar/RenderManProServer-21.2/lib/python2.7/Lib/site-packages")
import ice


createDomeShpere(self):
createBaseLightBall = cmds.polySphere(n='baseLightBall',r=2,sx=40,sy=20,ch=0)
#cmds.setAttr('baseLightBall.rotate.rotateY',-72)

print createBaseLightBall

cmds.polyEvaluate('baseLightBall',v=True)
bigHdriCordDict(self):        #define every calculated range for each vertex ,4K image 

widthPixels = 4000
higthPixels = 2000
subX = 40
subY = 20

widthBlock = widthPixels/subX
hightBlock = higthPixels/subY


borderVertex = [u'baseLightBall.vtx[0]', u'baseLightBall.vtx[40]', u'baseLightBall.vtx[80]', u'baseLightBall.vtx[120]', u'baseLightBall.vtx[160]', u'baseLightBall.vtx[200]', u'baseLightBall.vtx[240]', u'baseLightBall.vtx[280]', u'baseLightBall.vtx[320]', u'baseLightBall.vtx[360]', u'baseLightBall.vtx[400]', u'baseLightBall.vtx[440]', u'baseLightBall.vtx[480]', u'baseLightBall.vtx[520]', u'baseLightBall.vtx[560]', u'baseLightBall.vtx[600]', u'baseLightBall.vtx[640]', u'baseLightBall.vtx[680]', u'baseLightBall.vtx[720]']
polarVertxx = [u'baseLightBall.vtx[760]', u'baseLightBall.vtx[761]']
print borderVertex[0]
print len(borderVertex)




#cmds.polyEvaluate('pPlane1',v=True)

cordDict = {}

yRange = 0
for t in range(0,subY-1):
    xRange = 0
    for s in range(0,subX):
        #print s
        yRange = hightBlock * (t+1)
        #pixelSmallZone = 
        cordDict.update({(t*subX)+s:[xRange-(widthBlock/2),xRange+((widthBlock/2)-1),yRange-(hightBlock/2), yRange+((hightBlock/2)-1)]})
        xRange = xRange + widthBlock
    
edgePointIndex = {0:[[0,49,50,149],[3950,3999,50,149]],
                  40:[[0,49,150,249],[3950,3999,150,249]],
                  80:[[0,49,250,349],[3950,3999,250,349]],
                  120:[[0,49,350,449],[3950,3999,350,449]],
                  160:[[0,49,450,549],[3950,3999,450,549]],
                  200:[[0,49,550,649],[3950,3999,550,649]],
                  240:[[0,49,650,749],[3950,3999,650,749]],
                  280:[[0,49,750,849],[3950,3999,750,849]],
                  320:[[0,49,850,949],[3950,3999,850,949]],
                  360:[[0,49,950,1049],[3950,3999,950,1049]],
                  400:[[0,49,1050,1149],[3950,3999,1050,1149]],
                  440:[[0,49,1150,1249],[3950,3999,1150,1249]],
                  480:[[0,49,1250,1349],[3950,3999,1250,1349]],
                  520:[[0,49,1350,1449],[3950,3999,1350,1449]],
                  560:[[0,49,1450,1549],[3950,3999,1450,1549]],
                  600:[[0,49,1550,1649],[3950,3999,1550,1649]],
                  640:[[0,49,1650,1749],[3950,3999,1650,1749]],
                  680:[[0,49,1750,1849],[3950,3999,1750,1849]],
                  720:[[0,49,1850,1949],[3950,3999,1850,1949]],
                  761:[[0,3999,0,49]],
                  760:[[0,3999,1950,1999]]                                  
                  }



for num in edgePointIndex:
    cordDict.update({num:edgePointIndex[num]})
    print num,cordDict[num]
        

#def bigHDRI_blockRangeDict(self,imageName):    #define the 4K hdri image ,each range of block, total 762(0 to 761)
    
bigimageBlockRangeBlockDict = {0: [[0, 49, 50, 149], [3950, 3999, 50, 149]], 1: [50, 149, 50, 149], 2: [150, 249, 50, 149], 3: [250, 349, 50, 149], 4: [350, 449, 50, 149], 5: [450, 549, 50, 149], 6: [550, 649, 50, 149], 7: [650, 749, 50, 149], 8: [750, 849, 50, 149], 9: [850, 949, 50, 149], 10: [950, 1049, 50, 149], 11: [1050, 1149, 50, 149], 12: [1150, 1249, 50, 149], 13: [1250, 1349, 50, 149], 14: [1350, 1449, 50, 149], 15: [1450, 1549, 50, 149], 16: [1550, 1649, 50, 149], 17: [1650, 1749, 50, 149], 18: [1750, 1849, 50, 149], 19: [1850, 1949, 50, 149], 20: [1950, 2049, 50, 149], 21: [2050, 2149, 50, 149], 22: [2150, 2249, 50, 149], 23: [2250, 2349, 50, 149], 24: [2350, 2449, 50, 149], 25: [2450, 2549, 50, 149], 26: [2550, 2649, 50, 149], 27: [2650, 2749, 50, 149], 28: [2750, 2849, 50, 149], 29: [2850, 2949, 50, 149], 30: [2950, 3049, 50, 149], 31: [3050, 3149, 50, 149], 32: [3150, 3249, 50, 149], 33: [3250, 3349, 50, 149], 34: [3350, 3449, 50, 149], 35: [3450, 3549, 50, 149], 36: [3550, 3649, 50, 149], 37: [3650, 3749, 50, 149], 38: [3750, 3849, 50, 149], 39: [3850, 3949, 50, 149], 40: [[0, 49, 150, 249], [3950, 3999, 150, 249]], 41: [50, 149, 150, 249], 42: [150, 249, 150, 249], 43: [250, 349, 150, 249], 44: [350, 449, 150, 249], 45: [450, 549, 150, 249], 46: [550, 649, 150, 249], 47: [650, 749, 150, 249], 48: [750, 849, 150, 249], 49: [850, 949, 150, 249], 50: [950, 1049, 150, 249], 51: [1050, 1149, 150, 249], 52: [1150, 1249, 150, 249], 53: [1250, 1349, 150, 249], 54: [1350, 1449, 150, 249], 55: [1450, 1549, 150, 249], 56: [1550, 1649, 150, 249], 57: [1650, 1749, 150, 249], 58: [1750, 1849, 150, 249], 59: [1850, 1949, 150, 249], 60: [1950, 2049, 150, 249], 61: [2050, 2149, 150, 249], 62: [2150, 2249, 150, 249], 63: [2250, 2349, 150, 249], 64: [2350, 2449, 150, 249], 65: [2450, 2549, 150, 249], 66: [2550, 2649, 150, 249], 67: [2650, 2749, 150, 249], 68: [2750, 2849, 150, 249], 69: [2850, 2949, 150, 249], 70: [2950, 3049, 150, 249], 71: [3050, 3149, 150, 249], 72: [3150, 3249, 150, 249], 73: [3250, 3349, 150, 249], 74: [3350, 3449, 150, 249], 75: [3450, 3549, 150, 249], 76: [3550, 3649, 150, 249], 77: [3650, 3749, 150, 249], 78: [3750, 3849, 150, 249], 79: [3850, 3949, 150, 249], 80: [[0, 49, 250, 349], [3950, 3999, 250, 349]], 81: [50, 149, 250, 349], 82: [150, 249, 250, 349], 83: [250, 349, 250, 349], 84: [350, 449, 250, 349], 85: [450, 549, 250, 349], 86: [550, 649, 250, 349], 87: [650, 749, 250, 349], 88: [750, 849, 250, 349], 89: [850, 949, 250, 349], 90: [950, 1049, 250, 349], 91: [1050, 1149, 250, 349], 92: [1150, 1249, 250, 349], 93: [1250, 1349, 250, 349], 94: [1350, 1449, 250, 349], 95: [1450, 1549, 250, 349], 96: [1550, 1649, 250, 349], 97: [1650, 1749, 250, 349], 98: [1750, 1849, 250, 349], 99: [1850, 1949, 250, 349], 100: [1950, 2049, 250, 349], 101: [2050, 2149, 250, 349], 102: [2150, 2249, 250, 349], 103: [2250, 2349, 250, 349], 104: [2350, 2449, 250, 349], 105: [2450, 2549, 250, 349], 106: [2550, 2649, 250, 349], 107: [2650, 2749, 250, 349], 108: [2750, 2849, 250, 349], 109: [2850, 2949, 250, 349], 110: [2950, 3049, 250, 349], 111: [3050, 3149, 250, 349], 112: [3150, 3249, 250, 349], 113: [3250, 3349, 250, 349], 114: [3350, 3449, 250, 349], 115: [3450, 3549, 250, 349], 116: [3550, 3649, 250, 349], 117: [3650, 3749, 250, 349], 118: [3750, 3849, 250, 349], 119: [3850, 3949, 250, 349], 120: [[0, 49, 350, 449], [3950, 3999, 350, 449]], 121: [50, 149, 350, 449], 122: [150, 249, 350, 449], 123: [250, 349, 350, 449], 124: [350, 449, 350, 449], 125: [450, 549, 350, 449], 126: [550, 649, 350, 449], 127: [650, 749, 350, 449], 128: [750, 849, 350, 449], 129: [850, 949, 350, 449], 130: [950, 1049, 350, 449], 131: [1050, 1149, 350, 449], 132: [1150, 1249, 350, 449], 133: [1250, 1349, 350, 449], 134: [1350, 1449, 350, 449], 135: [1450, 1549, 350, 449], 136: [1550, 1649, 350, 449], 137: [1650, 1749, 350, 449], 138: [1750, 1849, 350, 449], 139: [1850, 1949, 350, 449], 140: [1950, 2049, 350, 449], 141: [2050, 2149, 350, 449], 142: [2150, 2249, 350, 449], 143: [2250, 2349, 350, 449], 144: [2350, 2449, 350, 449], 145: [2450, 2549, 350, 449], 146: [2550, 2649, 350, 449], 147: [2650, 2749, 350, 449], 148: [2750, 2849, 350, 449], 149: [2850, 2949, 350, 449], 150: [2950, 3049, 350, 449], 151: [3050, 3149, 350, 449], 152: [3150, 3249, 350, 449], 153: [3250, 3349, 350, 449], 154: [3350, 3449, 350, 449], 155: [3450, 3549, 350, 449], 156: [3550, 3649, 350, 449], 157: [3650, 3749, 350, 449], 158: [3750, 3849, 350, 449], 159: [3850, 3949, 350, 449], 160: [[0, 49, 450, 549], [3950, 3999, 450, 549]], 161: [50, 149, 450, 549], 162: [150, 249, 450, 549], 163: [250, 349, 450, 549], 164: [350, 449, 450, 549], 165: [450, 549, 450, 549], 166: [550, 649, 450, 549], 167: [650, 749, 450, 549], 168: [750, 849, 450, 549], 169: [850, 949, 450, 549], 170: [950, 1049, 450, 549], 171: [1050, 1149, 450, 549], 172: [1150, 1249, 450, 549], 173: [1250, 1349, 450, 549], 174: [1350, 1449, 450, 549], 175: [1450, 1549, 450, 549], 176: [1550, 1649, 450, 549], 177: [1650, 1749, 450, 549], 178: [1750, 1849, 450, 549], 179: [1850, 1949, 450, 549], 180: [1950, 2049, 450, 549], 181: [2050, 2149, 450, 549], 182: [2150, 2249, 450, 549], 183: [2250, 2349, 450, 549], 184: [2350, 2449, 450, 549], 185: [2450, 2549, 450, 549], 186: [2550, 2649, 450, 549], 187: [2650, 2749, 450, 549], 188: [2750, 2849, 450, 549], 189: [2850, 2949, 450, 549], 190: [2950, 3049, 450, 549], 191: [3050, 3149, 450, 549], 192: [3150, 3249, 450, 549], 193: [3250, 3349, 450, 549], 194: [3350, 3449, 450, 549], 195: [3450, 3549, 450, 549], 196: [3550, 3649, 450, 549], 197: [3650, 3749, 450, 549], 198: [3750, 3849, 450, 549], 199: [3850, 3949, 450, 549], 200: [[0, 49, 550, 649], [3950, 3999, 550, 649]], 201: [50, 149, 550, 649], 202: [150, 249, 550, 649], 203: [250, 349, 550, 649], 204: [350, 449, 550, 649], 205: [450, 549, 550, 649], 206: [550, 649, 550, 649], 207: [650, 749, 550, 649], 208: [750, 849, 550, 649], 209: [850, 949, 550, 649], 210: [950, 1049, 550, 649], 211: [1050, 1149, 550, 649], 212: [1150, 1249, 550, 649], 213: [1250, 1349, 550, 649], 214: [1350, 1449, 550, 649], 215: [1450, 1549, 550, 649], 216: [1550, 1649, 550, 649], 217: [1650, 1749, 550, 649], 218: [1750, 1849, 550, 649], 219: [1850, 1949, 550, 649], 220: [1950, 2049, 550, 649], 221: [2050, 2149, 550, 649], 222: [2150, 2249, 550, 649], 223: [2250, 2349, 550, 649], 224: [2350, 2449, 550, 649], 225: [2450, 2549, 550, 649], 226: [2550, 2649, 550, 649], 227: [2650, 2749, 550, 649], 228: [2750, 2849, 550, 649], 229: [2850, 2949, 550, 649], 230: [2950, 3049, 550, 649], 231: [3050, 3149, 550, 649], 232: [3150, 3249, 550, 649], 233: [3250, 3349, 550, 649], 234: [3350, 3449, 550, 649], 235: [3450, 3549, 550, 649], 236: [3550, 3649, 550, 649], 237: [3650, 3749, 550, 649], 238: [3750, 3849, 550, 649], 239: [3850, 3949, 550, 649], 240: [[0, 49, 650, 749], [3950, 3999, 650, 749]], 241: [50, 149, 650, 749], 242: [150, 249, 650, 749], 243: [250, 349, 650, 749], 244: [350, 449, 650, 749], 245: [450, 549, 650, 749], 246: [550, 649, 650, 749], 247: [650, 749, 650, 749], 248: [750, 849, 650, 749], 249: [850, 949, 650, 749], 250: [950, 1049, 650, 749], 251: [1050, 1149, 650, 749], 252: [1150, 1249, 650, 749], 253: [1250, 1349, 650, 749], 254: [1350, 1449, 650, 749], 255: [1450, 1549, 650, 749], 256: [1550, 1649, 650, 749], 257: [1650, 1749, 650, 749], 258: [1750, 1849, 650, 749], 259: [1850, 1949, 650, 749], 260: [1950, 2049, 650, 749], 261: [2050, 2149, 650, 749], 262: [2150, 2249, 650, 749], 263: [2250, 2349, 650, 749], 264: [2350, 2449, 650, 749], 265: [2450, 2549, 650, 749], 266: [2550, 2649, 650, 749], 267: [2650, 2749, 650, 749], 268: [2750, 2849, 650, 749], 269: [2850, 2949, 650, 749], 270: [2950, 3049, 650, 749], 271: [3050, 3149, 650, 749], 272: [3150, 3249, 650, 749], 273: [3250, 3349, 650, 749], 274: [3350, 3449, 650, 749], 275: [3450, 3549, 650, 749], 276: [3550, 3649, 650, 749], 277: [3650, 3749, 650, 749], 278: [3750, 3849, 650, 749], 279: [3850, 3949, 650, 749], 280: [[0, 49, 750, 849], [3950, 3999, 750, 849]], 281: [50, 149, 750, 849], 282: [150, 249, 750, 849], 283: [250, 349, 750, 849], 284: [350, 449, 750, 849], 285: [450, 549, 750, 849], 286: [550, 649, 750, 849], 287: [650, 749, 750, 849], 288: [750, 849, 750, 849], 289: [850, 949, 750, 849], 290: [950, 1049, 750, 849], 291: [1050, 1149, 750, 849], 292: [1150, 1249, 750, 849], 293: [1250, 1349, 750, 849], 294: [1350, 1449, 750, 849], 295: [1450, 1549, 750, 849], 296: [1550, 1649, 750, 849], 297: [1650, 1749, 750, 849], 298: [1750, 1849, 750, 849], 299: [1850, 1949, 750, 849], 300: [1950, 2049, 750, 849], 301: [2050, 2149, 750, 849], 302: [2150, 2249, 750, 849], 303: [2250, 2349, 750, 849], 304: [2350, 2449, 750, 849], 305: [2450, 2549, 750, 849], 306: [2550, 2649, 750, 849], 307: [2650, 2749, 750, 849], 308: [2750, 2849, 750, 849], 309: [2850, 2949, 750, 849], 310: [2950, 3049, 750, 849], 311: [3050, 3149, 750, 849], 312: [3150, 3249, 750, 849], 313: [3250, 3349, 750, 849], 314: [3350, 3449, 750, 849], 315: [3450, 3549, 750, 849], 316: [3550, 3649, 750, 849], 317: [3650, 3749, 750, 849], 318: [3750, 3849, 750, 849], 319: [3850, 3949, 750, 849], 320: [[0, 49, 850, 949], [3950, 3999, 850, 949]], 321: [50, 149, 850, 949], 322: [150, 249, 850, 949], 323: [250, 349, 850, 949], 324: [350, 449, 850, 949], 325: [450, 549, 850, 949], 326: [550, 649, 850, 949], 327: [650, 749, 850, 949], 328: [750, 849, 850, 949], 329: [850, 949, 850, 949], 330: [950, 1049, 850, 949], 331: [1050, 1149, 850, 949], 332: [1150, 1249, 850, 949], 333: [1250, 1349, 850, 949], 334: [1350, 1449, 850, 949], 335: [1450, 1549, 850, 949], 336: [1550, 1649, 850, 949], 337: [1650, 1749, 850, 949], 338: [1750, 1849, 850, 949], 339: [1850, 1949, 850, 949], 340: [1950, 2049, 850, 949], 341: [2050, 2149, 850, 949], 342: [2150, 2249, 850, 949], 343: [2250, 2349, 850, 949], 344: [2350, 2449, 850, 949], 345: [2450, 2549, 850, 949], 346: [2550, 2649, 850, 949], 347: [2650, 2749, 850, 949], 348: [2750, 2849, 850, 949], 349: [2850, 2949, 850, 949], 350: [2950, 3049, 850, 949], 351: [3050, 3149, 850, 949], 352: [3150, 3249, 850, 949], 353: [3250, 3349, 850, 949], 354: [3350, 3449, 850, 949], 355: [3450, 3549, 850, 949], 356: [3550, 3649, 850, 949], 357: [3650, 3749, 850, 949], 358: [3750, 3849, 850, 949], 359: [3850, 3949, 850, 949], 360: [[0, 49, 950, 1049], [3950, 3999, 950, 1049]], 361: [50, 149, 950, 1049], 362: [150, 249, 950, 1049], 363: [250, 349, 950, 1049], 364: [350, 449, 950, 1049], 365: [450, 549, 950, 1049], 366: [550, 649, 950, 1049], 367: [650, 749, 950, 1049], 368: [750, 849, 950, 1049], 369: [850, 949, 950, 1049], 370: [950, 1049, 950, 1049], 371: [1050, 1149, 950, 1049], 372: [1150, 1249, 950, 1049], 373: [1250, 1349, 950, 1049], 374: [1350, 1449, 950, 1049], 375: [1450, 1549, 950, 1049], 376: [1550, 1649, 950, 1049], 377: [1650, 1749, 950, 1049], 378: [1750, 1849, 950, 1049], 379: [1850, 1949, 950, 1049], 380: [1950, 2049, 950, 1049], 381: [2050, 2149, 950, 1049], 382: [2150, 2249, 950, 1049], 383: [2250, 2349, 950, 1049], 384: [2350, 2449, 950, 1049], 385: [2450, 2549, 950, 1049], 386: [2550, 2649, 950, 1049], 387: [2650, 2749, 950, 1049], 388: [2750, 2849, 950, 1049], 389: [2850, 2949, 950, 1049], 390: [2950, 3049, 950, 1049], 391: [3050, 3149, 950, 1049], 392: [3150, 3249, 950, 1049], 393: [3250, 3349, 950, 1049], 394: [3350, 3449, 950, 1049], 395: [3450, 3549, 950, 1049], 396: [3550, 3649, 950, 1049], 397: [3650, 3749, 950, 1049], 398: [3750, 3849, 950, 1049], 399: [3850, 3949, 950, 1049], 400: [[0, 49, 1050, 1149], [3950, 3999, 1050, 1149]], 401: [50, 149, 1050, 1149], 402: [150, 249, 1050, 1149], 403: [250, 349, 1050, 1149], 404: [350, 449, 1050, 1149], 405: [450, 549, 1050, 1149], 406: [550, 649, 1050, 1149], 407: [650, 749, 1050, 1149], 408: [750, 849, 1050, 1149], 409: [850, 949, 1050, 1149], 410: [950, 1049, 1050, 1149], 411: [1050, 1149, 1050, 1149], 412: [1150, 1249, 1050, 1149], 413: [1250, 1349, 1050, 1149], 414: [1350, 1449, 1050, 1149], 415: [1450, 1549, 1050, 1149], 416: [1550, 1649, 1050, 1149], 417: [1650, 1749, 1050, 1149], 418: [1750, 1849, 1050, 1149], 419: [1850, 1949, 1050, 1149], 420: [1950, 2049, 1050, 1149], 421: [2050, 2149, 1050, 1149], 422: [2150, 2249, 1050, 1149], 423: [2250, 2349, 1050, 1149], 424: [2350, 2449, 1050, 1149], 425: [2450, 2549, 1050, 1149], 426: [2550, 2649, 1050, 1149], 427: [2650, 2749, 1050, 1149], 428: [2750, 2849, 1050, 1149], 429: [2850, 2949, 1050, 1149], 430: [2950, 3049, 1050, 1149], 431: [3050, 3149, 1050, 1149], 432: [3150, 3249, 1050, 1149], 433: [3250, 3349, 1050, 1149], 434: [3350, 3449, 1050, 1149], 435: [3450, 3549, 1050, 1149], 436: [3550, 3649, 1050, 1149], 437: [3650, 3749, 1050, 1149], 438: [3750, 3849, 1050, 1149], 439: [3850, 3949, 1050, 1149], 440: [[0, 49, 1150, 1249], [3950, 3999, 1150, 1249]], 441: [50, 149, 1150, 1249], 442: [150, 249, 1150, 1249], 443: [250, 349, 1150, 1249], 444: [350, 449, 1150, 1249], 445: [450, 549, 1150, 1249], 446: [550, 649, 1150, 1249], 447: [650, 749, 1150, 1249], 448: [750, 849, 1150, 1249], 449: [850, 949, 1150, 1249], 450: [950, 1049, 1150, 1249], 451: [1050, 1149, 1150, 1249], 452: [1150, 1249, 1150, 1249], 453: [1250, 1349, 1150, 1249], 454: [1350, 1449, 1150, 1249], 455: [1450, 1549, 1150, 1249], 456: [1550, 1649, 1150, 1249], 457: [1650, 1749, 1150, 1249], 458: [1750, 1849, 1150, 1249], 459: [1850, 1949, 1150, 1249], 460: [1950, 2049, 1150, 1249], 461: [2050, 2149, 1150, 1249], 462: [2150, 2249, 1150, 1249], 463: [2250, 2349, 1150, 1249], 464: [2350, 2449, 1150, 1249], 465: [2450, 2549, 1150, 1249], 466: [2550, 2649, 1150, 1249], 467: [2650, 2749, 1150, 1249], 468: [2750, 2849, 1150, 1249], 469: [2850, 2949, 1150, 1249], 470: [2950, 3049, 1150, 1249], 471: [3050, 3149, 1150, 1249], 472: [3150, 3249, 1150, 1249], 473: [3250, 3349, 1150, 1249], 474: [3350, 3449, 1150, 1249], 475: [3450, 3549, 1150, 1249], 476: [3550, 3649, 1150, 1249], 477: [3650, 3749, 1150, 1249], 478: [3750, 3849, 1150, 1249], 479: [3850, 3949, 1150, 1249], 480: [[0, 49, 1250, 1349], [3950, 3999, 1250, 1349]], 481: [50, 149, 1250, 1349], 482: [150, 249, 1250, 1349], 483: [250, 349, 1250, 1349], 484: [350, 449, 1250, 1349], 485: [450, 549, 1250, 1349], 486: [550, 649, 1250, 1349], 487: [650, 749, 1250, 1349], 488: [750, 849, 1250, 1349], 489: [850, 949, 1250, 1349], 490: [950, 1049, 1250, 1349], 491: [1050, 1149, 1250, 1349], 492: [1150, 1249, 1250, 1349], 493: [1250, 1349, 1250, 1349], 494: [1350, 1449, 1250, 1349], 495: [1450, 1549, 1250, 1349], 496: [1550, 1649, 1250, 1349], 497: [1650, 1749, 1250, 1349], 498: [1750, 1849, 1250, 1349], 499: [1850, 1949, 1250, 1349], 500: [1950, 2049, 1250, 1349], 501: [2050, 2149, 1250, 1349], 502: [2150, 2249, 1250, 1349], 503: [2250, 2349, 1250, 1349], 504: [2350, 2449, 1250, 1349], 505: [2450, 2549, 1250, 1349], 506: [2550, 2649, 1250, 1349], 507: [2650, 2749, 1250, 1349], 508: [2750, 2849, 1250, 1349], 509: [2850, 2949, 1250, 1349], 510: [2950, 3049, 1250, 1349], 511: [3050, 3149, 1250, 1349], 512: [3150, 3249, 1250, 1349], 513: [3250, 3349, 1250, 1349], 514: [3350, 3449, 1250, 1349], 515: [3450, 3549, 1250, 1349], 516: [3550, 3649, 1250, 1349], 517: [3650, 3749, 1250, 1349], 518: [3750, 3849, 1250, 1349], 519: [3850, 3949, 1250, 1349], 520: [[0, 49, 1350, 1449], [3950, 3999, 1350, 1449]], 521: [50, 149, 1350, 1449], 522: [150, 249, 1350, 1449], 523: [250, 349, 1350, 1449], 524: [350, 449, 1350, 1449], 525: [450, 549, 1350, 1449], 526: [550, 649, 1350, 1449], 527: [650, 749, 1350, 1449], 528: [750, 849, 1350, 1449], 529: [850, 949, 1350, 1449], 530: [950, 1049, 1350, 1449], 531: [1050, 1149, 1350, 1449], 532: [1150, 1249, 1350, 1449], 533: [1250, 1349, 1350, 1449], 534: [1350, 1449, 1350, 1449], 535: [1450, 1549, 1350, 1449], 536: [1550, 1649, 1350, 1449], 537: [1650, 1749, 1350, 1449], 538: [1750, 1849, 1350, 1449], 539: [1850, 1949, 1350, 1449], 540: [1950, 2049, 1350, 1449], 541: [2050, 2149, 1350, 1449], 542: [2150, 2249, 1350, 1449], 543: [2250, 2349, 1350, 1449], 544: [2350, 2449, 1350, 1449], 545: [2450, 2549, 1350, 1449], 546: [2550, 2649, 1350, 1449], 547: [2650, 2749, 1350, 1449], 548: [2750, 2849, 1350, 1449], 549: [2850, 2949, 1350, 1449], 550: [2950, 3049, 1350, 1449], 551: [3050, 3149, 1350, 1449], 552: [3150, 3249, 1350, 1449], 553: [3250, 3349, 1350, 1449], 554: [3350, 3449, 1350, 1449], 555: [3450, 3549, 1350, 1449], 556: [3550, 3649, 1350, 1449], 557: [3650, 3749, 1350, 1449], 558: [3750, 3849, 1350, 1449], 559: [3850, 3949, 1350, 1449], 560: [[0, 49, 1450, 1549], [3950, 3999, 1450, 1549]], 561: [50, 149, 1450, 1549], 562: [150, 249, 1450, 1549], 563: [250, 349, 1450, 1549], 564: [350, 449, 1450, 1549], 565: [450, 549, 1450, 1549], 566: [550, 649, 1450, 1549], 567: [650, 749, 1450, 1549], 568: [750, 849, 1450, 1549], 569: [850, 949, 1450, 1549], 570: [950, 1049, 1450, 1549], 571: [1050, 1149, 1450, 1549], 572: [1150, 1249, 1450, 1549], 573: [1250, 1349, 1450, 1549], 574: [1350, 1449, 1450, 1549], 575: [1450, 1549, 1450, 1549], 576: [1550, 1649, 1450, 1549], 577: [1650, 1749, 1450, 1549], 578: [1750, 1849, 1450, 1549], 579: [1850, 1949, 1450, 1549], 580: [1950, 2049, 1450, 1549], 581: [2050, 2149, 1450, 1549], 582: [2150, 2249, 1450, 1549], 583: [2250, 2349, 1450, 1549], 584: [2350, 2449, 1450, 1549], 585: [2450, 2549, 1450, 1549], 586: [2550, 2649, 1450, 1549], 587: [2650, 2749, 1450, 1549], 588: [2750, 2849, 1450, 1549], 589: [2850, 2949, 1450, 1549], 590: [2950, 3049, 1450, 1549], 591: [3050, 3149, 1450, 1549], 592: [3150, 3249, 1450, 1549], 593: [3250, 3349, 1450, 1549], 594: [3350, 3449, 1450, 1549], 595: [3450, 3549, 1450, 1549], 596: [3550, 3649, 1450, 1549], 597: [3650, 3749, 1450, 1549], 598: [3750, 3849, 1450, 1549], 599: [3850, 3949, 1450, 1549], 600: [[0, 49, 1550, 1649], [3950, 3999, 1550, 1649]], 601: [50, 149, 1550, 1649], 602: [150, 249, 1550, 1649], 603: [250, 349, 1550, 1649], 604: [350, 449, 1550, 1649], 605: [450, 549, 1550, 1649], 606: [550, 649, 1550, 1649], 607: [650, 749, 1550, 1649], 608: [750, 849, 1550, 1649], 609: [850, 949, 1550, 1649], 610: [950, 1049, 1550, 1649], 611: [1050, 1149, 1550, 1649], 612: [1150, 1249, 1550, 1649], 613: [1250, 1349, 1550, 1649], 614: [1350, 1449, 1550, 1649], 615: [1450, 1549, 1550, 1649], 616: [1550, 1649, 1550, 1649], 617: [1650, 1749, 1550, 1649], 618: [1750, 1849, 1550, 1649], 619: [1850, 1949, 1550, 1649], 620: [1950, 2049, 1550, 1649], 621: [2050, 2149, 1550, 1649], 622: [2150, 2249, 1550, 1649], 623: [2250, 2349, 1550, 1649], 624: [2350, 2449, 1550, 1649], 625: [2450, 2549, 1550, 1649], 626: [2550, 2649, 1550, 1649], 627: [2650, 2749, 1550, 1649], 628: [2750, 2849, 1550, 1649], 629: [2850, 2949, 1550, 1649], 630: [2950, 3049, 1550, 1649], 631: [3050, 3149, 1550, 1649], 632: [3150, 3249, 1550, 1649], 633: [3250, 3349, 1550, 1649], 634: [3350, 3449, 1550, 1649], 635: [3450, 3549, 1550, 1649], 636: [3550, 3649, 1550, 1649], 637: [3650, 3749, 1550, 1649], 638: [3750, 3849, 1550, 1649], 639: [3850, 3949, 1550, 1649], 640: [[0, 49, 1650, 1749], [3950, 3999, 1650, 1749]], 641: [50, 149, 1650, 1749], 642: [150, 249, 1650, 1749], 643: [250, 349, 1650, 1749], 644: [350, 449, 1650, 1749], 645: [450, 549, 1650, 1749], 646: [550, 649, 1650, 1749], 647: [650, 749, 1650, 1749], 648: [750, 849, 1650, 1749], 649: [850, 949, 1650, 1749], 650: [950, 1049, 1650, 1749], 651: [1050, 1149, 1650, 1749], 652: [1150, 1249, 1650, 1749], 653: [1250, 1349, 1650, 1749], 654: [1350, 1449, 1650, 1749], 655: [1450, 1549, 1650, 1749], 656: [1550, 1649, 1650, 1749], 657: [1650, 1749, 1650, 1749], 658: [1750, 1849, 1650, 1749], 659: [1850, 1949, 1650, 1749], 660: [1950, 2049, 1650, 1749], 661: [2050, 2149, 1650, 1749], 662: [2150, 2249, 1650, 1749], 663: [2250, 2349, 1650, 1749], 664: [2350, 2449, 1650, 1749], 665: [2450, 2549, 1650, 1749], 666: [2550, 2649, 1650, 1749], 667: [2650, 2749, 1650, 1749], 668: [2750, 2849, 1650, 1749], 669: [2850, 2949, 1650, 1749], 670: [2950, 3049, 1650, 1749], 671: [3050, 3149, 1650, 1749], 672: [3150, 3249, 1650, 1749], 673: [3250, 3349, 1650, 1749], 674: [3350, 3449, 1650, 1749], 675: [3450, 3549, 1650, 1749], 676: [3550, 3649, 1650, 1749], 677: [3650, 3749, 1650, 1749], 678: [3750, 3849, 1650, 1749], 679: [3850, 3949, 1650, 1749], 680: [[0, 49, 1750, 1849], [3950, 3999, 1750, 1849]], 681: [50, 149, 1750, 1849], 682: [150, 249, 1750, 1849], 683: [250, 349, 1750, 1849], 684: [350, 449, 1750, 1849], 685: [450, 549, 1750, 1849], 686: [550, 649, 1750, 1849], 687: [650, 749, 1750, 1849], 688: [750, 849, 1750, 1849], 689: [850, 949, 1750, 1849], 690: [950, 1049, 1750, 1849], 691: [1050, 1149, 1750, 1849], 692: [1150, 1249, 1750, 1849], 693: [1250, 1349, 1750, 1849], 694: [1350, 1449, 1750, 1849], 695: [1450, 1549, 1750, 1849], 696: [1550, 1649, 1750, 1849], 697: [1650, 1749, 1750, 1849], 698: [1750, 1849, 1750, 1849], 699: [1850, 1949, 1750, 1849], 700: [1950, 2049, 1750, 1849], 701: [2050, 2149, 1750, 1849], 702: [2150, 2249, 1750, 1849], 703: [2250, 2349, 1750, 1849], 704: [2350, 2449, 1750, 1849], 705: [2450, 2549, 1750, 1849], 706: [2550, 2649, 1750, 1849], 707: [2650, 2749, 1750, 1849], 708: [2750, 2849, 1750, 1849], 709: [2850, 2949, 1750, 1849], 710: [2950, 3049, 1750, 1849], 711: [3050, 3149, 1750, 1849], 712: [3150, 3249, 1750, 1849], 713: [3250, 3349, 1750, 1849], 714: [3350, 3449, 1750, 1849], 715: [3450, 3549, 1750, 1849], 716: [3550, 3649, 1750, 1849], 717: [3650, 3749, 1750, 1849], 718: [3750, 3849, 1750, 1849], 719: [3850, 3949, 1750, 1849], 720: [[0, 49, 1850, 1949], [3950, 3999, 1850, 1949]], 721: [50, 149, 1850, 1949], 722: [150, 249, 1850, 1949], 723: [250, 349, 1850, 1949], 724: [350, 449, 1850, 1949], 725: [450, 549, 1850, 1949], 726: [550, 649, 1850, 1949], 727: [650, 749, 1850, 1949], 728: [750, 849, 1850, 1949], 729: [850, 949, 1850, 1949], 730: [950, 1049, 1850, 1949], 731: [1050, 1149, 1850, 1949], 732: [1150, 1249, 1850, 1949], 733: [1250, 1349, 1850, 1949], 734: [1350, 1449, 1850, 1949], 735: [1450, 1549, 1850, 1949], 736: [1550, 1649, 1850, 1949], 737: [1650, 1749, 1850, 1949], 738: [1750, 1849, 1850, 1949], 739: [1850, 1949, 1850, 1949], 740: [1950, 2049, 1850, 1949], 741: [2050, 2149, 1850, 1949], 742: [2150, 2249, 1850, 1949], 743: [2250, 2349, 1850, 1949], 744: [2350, 2449, 1850, 1949], 745: [2450, 2549, 1850, 1949], 746: [2550, 2649, 1850, 1949], 747: [2650, 2749, 1850, 1949], 748: [2750, 2849, 1850, 1949], 749: [2850, 2949, 1850, 1949], 750: [2950, 3049, 1850, 1949], 751: [3050, 3149, 1850, 1949], 752: [3150, 3249, 1850, 1949], 753: [3250, 3349, 1850, 1949], 754: [3350, 3449, 1850, 1949], 755: [3450, 3549, 1850, 1949], 756: [3550, 3649, 1850, 1949], 757: [3650, 3749, 1850, 1949], 758: [3750, 3849, 1850, 1949], 759: [3850, 3949, 1850, 1949], 760: [[0, 3999, 0, 49]], 761: [[0, 3999, 1950, 1999]]}



## HDRI image input and output fileName
bigHdriFileName = 'C:/Program Files/Pixar/RenderManProServer-21.2/lib/RenderManAssetLibrary/EnvironmentMaps/Outdoor/LuxoJr.rma/Luxo-Jr_4000x2000.tex'
hdriImage =ice.Load(bigHdriFileName)
tempHdriFileName = 'C:/temp/hdri/LuxoJr_4000x2000.exr'



    
## get metaData
ice.Image.GetMetaData(hdriImage)



print"hello world"
## get image box
ice.Image.DataBox(hdriImage)

## resize HdriImage to 4000 x 2000 and export to  file
imageResizeSpec = ice.Image.Reformat(hdriImage,[0,0,3999,1999])
format = ice.constants.FMT_EXRHALF
hdriImage.Save(tempHdriFileName,format)
hdriBeCalu = ice.Load(tempHdriFileName)
## export 16float exr to 4K HDRI






print aa
sumScaleY = 0
for s in range(0,200):
    for t in range(0,100):
        print s,t
        pixelScaleY = ice.Image.GetPixelVal(hdriBeCalu,s,t)[1] 
        sumScaleY = sumScaleY +pixelScaleY
print sumScaleY
        createCube = cmds.polyCube(sx=1,sy=1,sz=1)[0]
        cmds.setAttr('%s.scalePivotY'%createCube,-0.5)
        cmds.setAttr('%s.translateX'%createCube,s)
        cmds.setAttr('%s.translateZ'%createCube,t)
        cmds.setAttr('%s.scaleY'%createCube,pixelScaleY)
        

## creat joint all vertex
cmds.joint(n="jointOrigin")       
for vertexNum in bigimageBlockRangeBlockDict:
    if vertexNum % 40 == 0:
        pass
    elif vertexNum == 761:
        pass
        
    else :
        minX = bigimageBlockRangeBlockDict[vertexNum][0]
        maxX = bigimageBlockRangeBlockDict[vertexNum][1]
        minY = bigimageBlockRangeBlockDict[vertexNum][2]
        maxY = bigimageBlockRangeBlockDict[vertexNum][3]
        #print minX,maxX
        sumScaleY = 0
        for s in range(minX,maxX+1):
            for t in range(minY,maxY+1):
                pixelScaleY = ice.Image.GetPixelVal(hdriBeCalu,s,t)[1] 
                sumScaleY = sumScaleY + pixelScaleY
    #createCube = cmds.polyCube(sx=1,sy=1,sz=1)[0] 
    vertexName = 'baseLightBall.vtx['+str(vertexNum)+']'  # get pre vertex name
    cmds.select(cl=True)
    jointVertexName = 'joint_'+ str(vertexNum)
    jointOriginPreVertex = 'O_joint_'+ str(vertexNum)
    cmds.joint(n = jointOriginPreVertex )
    cmds.parent(jointOriginPreVertex,'jointOrigin')
    cmds.select(cl=True)
    #print jointVertexName ,jointOriginPreVertex

    cmds.joint(n=jointVertexName,p=(cmds.pointPosition(vertexName)[0],cmds.pointPosition(vertexName)[1],cmds.pointPosition(vertexName)[2]))
    cmds.parent(jointVertexName,jointOriginPreVertex)
    cmds.joint(jointOriginPreVertex,e=True,zso=True, oj='xyz')
    cmds.setAttr('%s.scaleX'%jointOriginPreVertex , sumScaleY/1000)
   # cmds.setAttr('%s.scalePivotY'%createCube,-0.5)
   # cmds.setAttr('%s.translateX'%createCube,cmds.pointPosition(vertexName)[0])
   # cmds.setAttr('%s.translateZ'%createCube,cmds.pointPosition(vertexName)[2])
   # cmds.setAttr('%s.scaleY'%createCube,sumScaleY)
   
   cmds.scale('O_joint_1',y=2,r=True,os=True)
    
    
for n in range(0,10):
    vertexName = 'baseLightBall.vtx['+str(vertexNum)+']'
    print vertexName
    print cmds.pointPosition(vertexName)
    
    
    
    
    print vertexNum, sumScaleY
    sumScaleY = sumScaleY +
0%40
1%40
760%40
print range(bigimageBlockRangeBlockDict[1][0],bigimageBlockRangeBlockDict[1][1]+1)    
print len(range(bigimageBlockRangeBlockDict[1][0],bigimageBlockRangeBlockDict[1][1]+1) )
        
        print ice.Image.GetPixelVal(hdriBeCalu,s,t) 
    print ice.Image.GetPixelVal(hdriBeCalu,2,2) 
    print pixelValue
    

bigimageBlockRangeBlockDict[1][0]