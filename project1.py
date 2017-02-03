from PIL import Image

img = Image.open("Project1Images//1.png")
img2 = Image.open("Project1Images//2.png")
img3 = Image.open("Project1Images//3.png")
img4 = Image.open("Project1Images//4.png")
img5 = Image.open("Project1Images//5.png")
img6 = Image.open("Project1Images//6.png")
img7 = Image.open("Project1Images//7.png")
img8 = Image.open("Project1Images//8.png")
img9 = Image.open("Project1Images//9.png")

print("This is the image size", img.size)

pictureWidth = 495
pictureHeight = 557
#pixels
redmpixel=0
greenmpixel=0
bluempixel=0

#create lists for pixels
redpixelList={}
greenpixelList={}
bluepixelList={}

#create a new blank image with width and height of original
newImage = Image.new("RGB",(495,557),"white")

#store images in a list
imageList = [img,img2,img3,img4,img5,img6,img7,img8,img9]

for x in range(0,pictureWidth):
    for y in range(0,pictureHeight):
        for image in ImageList:
            redpixelList = redmpixel
            





