import numpy as np
from skimage import io
from PIL import Image

## print each color percentage of 19x19 pixel used pixels color count
## RED
def checkRedPercentage(redCount,startXPoint,startYPoint):
    # 픽셀  하나값을  받아서  빨강인지 확인

    redPercentage = '{0:.2f}'.format((redCount / (19*19))*100)
#    print("red :", redPercentage ,"\n X : ", startXPoint, " Y : " ,startYPoint)

    if float(redPercentage) >= 62.00:
        stone_color= 'red'
        return startXPoint+9,startYPoint+9,stone_color


## Yellow
def checkYellowPercentage(yellowCount,startXPoint,startYPoint):

    yellowPercentage = '{0:.2f}'.format((yellowCount / (19*19))*100)
#    print("yellow :", yellowPercentage,"\n X : ", startXPoint, " Y : " ,startYPoint)

    if float(yellowPercentage) >= 62.00:
        stone_color = "yellow"
        return startXPoint + 9, startYPoint + 9, stone_color




## Check 1x1 each pixel have colors while 19x19 Size
def checkPixel(xPoint,yPoint,image,shot_list):

    redCount = 0
    yellowCount = 0

    pixel = []

    startXPoint = xPoint
    startYPoint= yPoint


    for y in range(yPoint,yPoint+19):

        pixel = image[y]


        for x in range(xPoint,xPoint+19 ):
            # pixel[StartYPoint][]
            #check black, blue, stoneColor




            if ((pixel[x][0] == 255) and (pixel[x][1] == 255) and (pixel[x][2] == 0)):

                yellowCount += 1

            if ((pixel[x][0] == 255) and (pixel[x][1] == 0) and (pixel[x][2] == 0)):

                redCount += 1

            #if ((pixel[x][0] == 255)and (pixel[x][1] == 255) and (pixel[x][2]== 255)):
            #    yellowCount +=1
            #    redCount +=1

            if((pixel[x][0] == 0)and (pixel[x][1] == 0) and (pixel[x][2]== 255)):
                yellowCount +=1
                redCount +=1







    shot_list.append(checkYellowPercentage(yellowCount,startXPoint,startYPoint))
    shot_list.append(checkRedPercentage(redCount,startXPoint,startYPoint))





    return shot_list


def main():

    filename = "SHOT_1_5.png"
    image = io.imread(filename,as_grey=False)
    im = Image.open(filename)
    arr = im.load()



    print (image[2][3])
    print(len(image)-(len(image[0])%19))
    xPoint = 0
    yPoint = 0
    shot_list = []


    for y in range(yPoint,len(image)-(len(image)%19),19):
        for x in range(xPoint,len(image[0])-(len(image[0])%19),19):

            checkPixel(x, y, image,shot_list)


    from operator import is_not
    from functools import partial
    print (list(filter(partial(is_not,None),shot_list)))





if __name__ == "__main__":
    main()

