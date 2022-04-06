import os
from PIL import Image
from html2image import Html2Image

def create_image_file(input_path):
    hti = Html2Image()
    
    path = input_path
    dir_list = os.listdir(path)

    ctr = 1

    for j in dir_list:

        file_path = path+'/'+j
        
        with open(file_path) as f:
            hti.screenshot(f.read(), save_as='out.png')
        
        file_name = ''
        
        img_name = j.split(".")
        if len(img_name[0]) == 6:
            file_name = img_name[0][5]
        elif len(img_name[0]) == 7:
            file_name = img_name[0][5]+img_name[0][6]
        
        read_path = './'
        files = os.listdir(read_path)

        for f in files:
            print(f)
            if f == "out.png":
                im = Image.open(f, 'r')
                im = im.crop((0, 0, 398, 298))
                im.save("./out{}.png".format(file_name))
    
input_path = "D:/Event/results/COE19B003"
create_image_file(input_path)