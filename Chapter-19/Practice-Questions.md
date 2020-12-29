# Solutions for the Practice Questions in Chapter 19

## 1. What is an RGBA value?
It's a tuple of 4 integers, each ranging from 0 to 255. R denotes amount of Red, G denotes amount of Green, B denoted amount of Blue and A denotes the transparency.
## 2. How can you get the RGBA value of 'CornflowerBlue' from the Pillow module?
```
ImageColor.getcolor('CornflowerBlue','RGBA')
```
## 3. What is a box tuple?
A 4 integer tuple consisting of: the left-edge abscissa, the top-edge ordinate, the width and the height
## 4. What function returns an Image object for, say, an image file named zophie.png?
Image.open('zophie.png')
## 5. How can you find out the width and height of an Image object’s image?
imageObj.size
## 6. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?
imageObj.crop((0,50,50,50))
## 7. After making changes to an Image object, how could you save it as an image file?
imageObj.save('file_name.png')
## 8. What module contains Pillow’s shape-drawing code?
The ImageDraw module
## 9. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?
ImageDraw objects have drawing methods. To get an ImageDraw object, we should pass the Image object to the ImageDraw.Draw() function