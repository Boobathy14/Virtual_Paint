# Virtual_Paint

## Code Requirements:
This program is written in Python 3.9.5 and it uses the very famous OpenCV library. OpenCV is a computer vision and machine learning software library that includes many common image analysis algorithms that will help us build custom, intelligent computer vision applications.

## Object-Pre-processing(Find Colors of Object):
First, the model has to detect the color of the object. Here, i have used Yellow and Green color if you want you can just add the HSV color code. 
To pre-process we need to tunning the image, we can do this by using another py file which is attached in the same directory called 'Color_Trackbars'.

![green](https://user-images.githubusercontent.com/74816597/118251678-8225bb80-b4c5-11eb-98be-bf5679f4e8da.png)

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


next, all these value has to send as numpy array to a list, where these values are used to find the mask of the image. 

![image](https://user-images.githubusercontent.com/74816597/118529386-16f81580-b761-11eb-9a4a-f6270b10952e.png)

![image](https://user-images.githubusercontent.com/74816597/118591581-09bf4300-b7c2-11eb-9f3c-065250c9dc8e.png)


### what is mask?
mask are nothing but the thing you need in a image will be white others will be in black.

![image](https://user-images.githubusercontent.com/74816597/118530214-072d0100-b762-11eb-8bad-85f206a3918c.png)

### Step3:
## Get Contours:
### What is Contours?
Contours are curve joining all the continuous points, having same color or intensity.In simple way Here, in the below image you can able to see the blue color outline of (pen cap) that called contours.
In OpenCV, finding contours is like finding white object from black background.

![image](https://user-images.githubusercontent.com/74816597/118523391-b5cd4380-b75a-11eb-9a74-0e00ae6f5848.png)

![image](https://user-images.githubusercontent.com/74816597/118591257-8271cf80-b7c1-11eb-848b-c2f70fc0bf91.png)

### Further reference(Open source article):
https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html

### Step 4:
def_draw_it(user define function), it calculate point(pen cap top point). draw based on the respective color.
![image](https://user-images.githubusercontent.com/74816597/118591695-3ecb9580-b7c2-11eb-9ec6-a7965f9018ff.png)

### Step 5:
call all the function in while loop, because as video is a combination of multiple image. Each frame has to calculated and considered as a image.
![image](https://user-images.githubusercontent.com/74816597/118595593-e055e580-b7c8-11eb-85e6-61e25a8a29c3.png)

### Video clip:

## Final Output:
https://drive.google.com/file/d/1Emen1N378KWXw9k0Co4qC4nZT6nl0nKM/view?usp=sharing

https://user-images.githubusercontent.com/74816597/118668503-8ed24880-b812-11eb-8a8f-a67fbf5d2a2c.mp4







