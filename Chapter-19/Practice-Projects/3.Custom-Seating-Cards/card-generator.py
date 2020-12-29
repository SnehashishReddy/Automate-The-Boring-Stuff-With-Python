from PIL import Image, ImageFont, ImageDraw, ImageOps

with open('guests.txt','r') as file:
    lst = file.read().splitlines()
x = 0
while x < len(lst):
    img = Image.open("flower.jpg")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("OpenSans-ExtraBold.ttf", 24)
    ifont = ImageFont.truetype("OpenSans-BoldItalic.ttf", 13)
    rfont = ImageFont.truetype("OpenSans-Regular.ttf", 24)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((3, 100),"It would be a pleasure to have the company of",(0,0,0),font=ifont)
    draw.text((90, 115),str(lst[x]),(0,0,0),font=font)
    draw.text((25, 150),"at 11010 Memory Lane on the Evening of",(0,0,0),font=ifont)
    draw.text((110, 165),"April 1st",(0,0,0),font=rfont)
    draw.text((115, 200),"at 7 o' clock",(0,0,0),font=ifont)
    img.save(lst[x] + '.jpg')
    img = Image.open(lst[x] + '.jpg')
    bordered_img = ImageOps.expand(img, border=5)
    bordered_img.save(lst[x] + '.jpg')
    x+=1