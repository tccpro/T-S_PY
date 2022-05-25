# from PIL import ImageFont, Image, ImageDraw
#
# font = ImageFont.truetype("arial.ttf",size=35)
# img = Image.open('downloads/images/img.14.jpeg')
# # w=img.width
# # h=img.height
# # if w>1.5*h:
# #     img = img.crop(((w-3*h//2)//2,0,(w+3*h//2)//2,h))
# # else:
# #     img = img.crop((0,(h-2*w//3)//2,w,(h+2*w//3)//2))
# img.thumbnail((300,200))
# default_image = Image.open('downloads/box.jpg')
# draw = ImageDraw.Draw(default_image)
# draw.text((1, 1),'11',font=font,fill='black')
# img.paste(default_image,(0,0))
# img.save('test1.png')
#
