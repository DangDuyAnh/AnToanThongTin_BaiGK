import os
import argparse
from PIL import Image, ExifTags

import VisualCryptography_colour as vc
folder = 'output_colour'

# from VisualCryptography_binary import *
# folder = 'output_binary'

# from VisualCryptography_gray import *
# folder = 'output_gray'

def readImage(path):
    try:
        im = Image.open(path)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        exif = im._getexif()
        if exif[orientation] == 3:
            im=im.rotate(180, expand=True)
        elif exif[orientation] == 6:
            im=im.rotate(270, expand=True)
        elif exif[orientation] == 8:
            im=im.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError, TypeError):
        # cases: image don't have getexif
        pass
    return im

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='input_path', type=str, help='path of input images')
    parser.add_argument('-m', dest='message', type=str, help='personal information to generate qr code')
    # parser.add_argument('-n', dest='num_of_shares', type=int, default=4, help='number of qr shares')
    args = parser.parse_args()

    # check input arguments
    im_name = args.input_path
    message = args.message
    n = 4 # args.num_of_shares
    if not os.path.exists(im_name):
        print('Cannot find input path: {0}'.format(im_name))
        exit()

    # encryptography
    input_image = readImage(im_name)
    vc.encrypt_with_QR(input_image, message, n)

    # decryptography
    images = []
    for i in range(1, n + 1):
        input_image = readImage(os.path.join(folder, 'Share_{}.png'.format(i)))
        images.append(input_image)
    vc.decrypt_with_QR(images)