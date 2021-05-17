# Virtual_Paint

## Code Requirements:
This program is written in Python 3.9.5 and it uses the very famous OpenCV library. OpenCV is a computer vision and machine learning software library that includes many common image analysis algorithms that will help us build custom, intelligent computer vision applications.

## Object-Pre-processing(Find Colors of Object):
First, the model has to detect the color of the object. Here, i have used Yellow and Green color if you want you can just add the HSV color code. 
To pre-process we need to tunning the image, we can do this by using another py file which is attached in the same directory called 'Color_Trackbars'.

![green](https://user-images.githubusercontent.com/74816597/118251678-8225bb80-b4c5-11eb-98be-bf5679f4e8da.png)


## Get Contours:
### What is Contours?
Contours are curve joining all the continuous points, having same color or intensity.In simple way Here, in the below image you can able to see the blue color outline of (pen cap) that called contours.
In OpenCV, finding contours is like finding white object from black background.

![image](https://user-images.githubusercontent.com/74816597/118523391-b5cd4380-b75a-11eb-9a74-0e00ae6f5848.png)


## Code Explanation
### Step 1: 
Import all the required package.

![import](https://user-images.githubusercontent.com/74816597/118249792-63bec080-b4c3-11eb-832a-4f7e7dedbfe5.png)

### Step 2:
#### Color Pick:
I have attached a file called Color_Trackbars.py. Where you can find the color of yor object(Pen cap).
first, the image or webcam should be converted to HSV format. Because, in HSV format only we can change the Hue,Saturation,val values according to our need.
Once you satisfied with your preprocessing note that values. In main file you need to create a another list (colors), which contain same value. 

![TRACKBARS](https://user-images.githubusercontent.com/74816597/118252364-4dfeca80-b4c6-11eb-8ee9-f052fc598749.png)


![image](https://user-images.githubusercontent.com/74816597/118529386-16f81580-b761-11eb-9a4a-f6270b10952e.png)

next, all these value has to send as numpy array to a list, where these values are used to find the mask of the image. 

### what is mask?
mask are nothing but the thing you need in a image will be white others will be in black.

![image](https://user-images.githubusercontent.com/74816597/118530214-072d0100-b762-11eb-8bad-85f206a3918c.png)
