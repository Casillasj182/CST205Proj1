#Joel Casillas

import statistics #imports a library for the median function
from PIL import Image

img1 = Image.open("Project1Images//1.png") # imported all the images from pil to python to open and use
img2 = Image.open("Project1Images//2.png") 
img3 = Image.open("Project1Images//3.png")
img4 = Image.open("Project1Images//4.png")
img5 = Image.open("Project1Images//5.png")
img6 = Image.open("Project1Images//6.png")
img7 = Image.open("Project1Images//7.png")
img8 = Image.open("Project1Images//8.png")
img9 = Image.open("Project1Images//9.png")

print("Opened Files...")


#Prints out the image size so i can use for blank and to loop through

Width = img1.size[0]
Height = img1.size[1]
print("Width", Width,"Height",Height)


redmpixel=0 #Setting the pixels to default 0
greenmpixel=0
bluempixel=0


redPixelList=[]   #lists for the imgages Red,green and blue
greenPixelList=[]
bluePixelList=[]

newImage = Image.new("RGB",(Width,Height),"white") #creating a newimage that will be blank and itll be the size of the pic


imageList = [img1,img2,img3,img4,img5,img6,img7,img8,img9] #Made a list to store all the 9 images in it

for x in range(Width):       ##for loop to go through the pixels in the pic width, and range to 
    for y in range(Height):       ##for loop to go through the pixels in the pic height
        for Myimage in imageList:
            
            myRed, myGreen, myBlue = Myimage.getpixel((x,y)) # x and y will go through each pixel and through all 9 images
            
            redPixelList.append(myRed)
            greenPixelList.append(myGreen)
            bluePixelList.append(myBlue)
        redmpixel = statistics.median(redPixelList)
        greenmpixel=statistics.median(greenPixelList)
        bluempixel=statistics.median(bluePixelList)
        redPixelList=[]   #lists for the imgages Red,green and blue
        greenPixelList=[]
        bluePixelList=[]
        
        newImage.putpixel((x,y),(redmpixel,greenmpixel,bluempixel)) 
        
     
          
               
newImage.save('New image.jpg')           
            
            
            



