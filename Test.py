import numpy as np
import Schemes
import cv2

N = 1000

triAn = Schemes.Triangle(
    Schemes.Point(10,700),
    Schemes.Point(1000,700),
    Schemes.Point(500,100)
)

currentPoint = triAn.a.Copy()

width = 1024
height = 768

im = np.ones([height,width,3],dtype=np.uint8)
cv2.imshow('image',im)

i = 0

weights = np.array([10,1,1])
multNeeded = 1/np.sum(weights)
weights = np.dot(weights,multNeeded)

while True:
    if(i < N):
        cordX = int(currentPoint.x)
        cordY = int(currentPoint.y)
        im = cv2.circle(im,(cordX,cordY),1,(255,255,255),-1)

        newChoice = np.random.choice(
            [triAn.a,triAn.b,triAn.c],
            p=weights,
        )

        currentPoint = Schemes.Point.Between(currentPoint,newChoice)
        print(currentPoint.x,currentPoint.y)

        N+=1
        
    cv2.imshow('image',im)
    w = cv2.waitKey(1) 
    if(w == ord("q")):
        break


# for i in range(N):



