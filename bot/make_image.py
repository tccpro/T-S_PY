import os

from PIL import Image,ImageDraw,ImageFont

def get_concat_h(imgs):
    images = []
    font = ImageFont.truetype("arial.ttf",size=35)
    for i in imgs:
        img = Image.open('downloads/images/'+i)
        # w = img.width
        # h = img.height
        # if w > 1.5 * h:
        #     img = img.crop(((w - 3 * h // 2) // 2, 0, (w + 3 * h // 2) // 2, h))
        # else:
        #     img = img.crop((0, (h - 2 * w // 3) // 2, w, (h + 2 * w // 3) // 2))
        img.thumbnail((300,200))
        default_image = Image.open('downloads/box.jpg')
        draw = ImageDraw.Draw(default_image)
        draw.text((1, 1),i.split('.')[1],font=font,fill='black')
        img.paste(default_image,(0,0))
        images.append(img)

    dst = Image.new('RGB',(600,((len(images)+1)//2)*200))
    for i in range(len(images)):
        dst.paste(images[i],((i%2)*300, (i//2)*200))
    img_name = 'downloads/gr_images/gr.'
    for i in imgs:
        img_name += i.split('.')[1]+'_'
    img_name=img_name+'.jpg'
    dst.save(img_name)
    return img_name

def get_gr_photo(keys):
    images = {}
    keyss=sorted(keys)
    for img in os.listdir('downloads/gr_images'):
        keysimage=sorted(img.split('.')[1].split('_'))
        if keyss == keysimage[1:]:
            return 'downloads/gr_images/' + img
    else:
        for file in os.listdir('downloads/images'):
            if file.split('.')[1] in keys:
                images[keys.index(file.split('.')[1])] = file
        imgs = [images[i] for i in sorted(images.keys())]
        return get_concat_h(imgs)
