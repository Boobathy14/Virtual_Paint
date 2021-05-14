# Virtual_Paint

## Code Requirements:
This program is written in Python 3.9.5 and it uses the very famous OpenCV library. OpenCV is a computer vision and machine learning software library that includes many common image analysis algorithms that will help us build custom, intelligent computer vision applications.

## Object-Pre-processing(Find Colors of Object):
First, the model has to detect the color of the object. Here, i have used Yellow and Green color if you want you can just add the HSV color code. 
To pre-process we need to tunning the image, we can do this by using another py file which is attached in the same directory called 'Color_Trackbars'.

![green](https://user-images.githubusercontent.com/74816597/118251678-8225bb80-b4c5-11eb-98be-bf5679f4e8da.png)

![TRACKBARS](https://user-images.githubusercontent.com/74816597/118252364-4dfeca80-b4c6-11eb-8ee9-f052fc598749.png)


## Get Contours:
### What is Contours?
Contours can be explained simply as a curve joining all the continuous points, having same color or intensity.In OpenCV, finding contours is like finding white object from black background.

![contours](https://user-images.githubusercontent.com/74816597/118249042-97e5b180-b4c2-11eb-9fac-ca289d1b0325.png)

## Code Explanation
### Step 1: 
Import all the required package.

![import](https://user-images.githubusercontent.com/74816597/118249792-63bec080-b4c3-11eb-832a-4f7e7dedbfe5.png)
