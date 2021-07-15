from PIL import Image
import numpy as np
import os, shutil
from QRcode import QR_area, QR_fromtext
from pyzbar.pyzbar import decode

def encrypt(input_image, share_size):               # Mã hóa ảnh màu với xor
    image = np.asarray(input_image)
    (row, column, depth) = image.shape
    shares = np.random.randint(0, 256, size=(row, column, depth, share_size))
    shares[:,:,:,-1] = image.copy()
    for i in range(share_size-1):
        shares[:,:,:,-1] = shares[:,:,:,-1] ^ shares[:,:,:,i]
    return shares

def decrypt(shares, share_size):                   # giải mã ảnh màu với xor
    for i in range(share_size - 1):
        shares[-1] = shares[-1][:,:,:] ^ shares[i][:,:,:]
    final_output = shares[-1]
    return final_output

def encrypt_with_QR(input_image, message, n):         # Mã hóa ảnh màu với QR, các ảnh sẽ được lưu vào thư mục output_colour
    # clean the output folder
    folder = 'output_colour'
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    # crop into square image
    input_image = input_image.convert('RGB')
    img_size = input_image.size[0]
    if (input_image.size[0] > input_image.size[1]):
        img_size = input_image.size[1]
    width, height = input_image.size
    left = (width - img_size) / 2
    top = (height - img_size) / 2
    right = (width + img_size) / 2
    bottom = (height + img_size) / 2
    square_img = input_image.crop((left, top, right, bottom))

    image_temp, pos_temp = QR_fromtext(message)
    image_temp = image_temp.convert('RGB')
    const_size = image_temp.size[0]
    square_img = square_img.resize((const_size,const_size), Image.NEAREST)
    shares = encrypt(square_img, n)
    results = []
    QR_image = np.asarray(image_temp).astype(np.uint8)
    QR_area0 = QR_area(image_temp, pos_temp)

    for i in range(n):
        temp = np.random.randint(0, 256, size=(const_size, const_size, 3))
        image = shares[:,:,:,i]
        for a in range(const_size):
            for b in range(const_size):
                if QR_area0[a][b] == 1:
                    temp[a][b] = QR_image[a][b]
                else:
                    temp[a][b] = image[a][b]
        temp = Image.fromarray(temp.astype(np.uint8))
        results.append(temp)
    for i in range(n):
        name = os.path.join('output_colour', 'Share_{}.png'.format(i + 1))
        print(name)
        results[i].save(name)


def decrypt_with_QR(shares):                      # giải mã các ảnh QR, và ghi thêm tên bệnh nhân
    share_size = len(shares)
    decoded_data = decode(shares[0])
    data = decoded_data[0].data.decode()
    image_temp, pos_temp = QR_fromtext(data)
    image_temp = image_temp.convert('RGB')
    const_size = image_temp.size[0]
    QR_image = np.asarray(image_temp).astype(np.uint8)
    QR_area0 = QR_area(image_temp, pos_temp)

    temps = []
    for i in range(share_size):
        temp = np.asarray(shares[i]).astype(np.uint8)
        temps.append(temp)
    final_output = decrypt(temps, share_size)
    for i in range(const_size):
        for j in range(const_size):
            if QR_area0[i][j] == 1:
                final_output[i][j] = QR_image[i][j]
    output_image = Image.fromarray(final_output.astype(np.uint8))
    output_name = os.path.join('output_colour','Output.png')
    output_image.save(output_name)
    print(output_name)
    return output_image, final_output


# Test thử chương trình

# Mã hóa
'''
message = "001200612738"
input_image = Image.open('Jennie_colour.jpg')
encrypt_with_QR(input_image, message, 3)
'''

# Giải mã
'''
images = []
input_image = Image.open('output_colour/Share_1.png')
images.append(input_image)
input_image = Image.open('output_colour/Share_2.png')
images.append(input_image)
input_image = Image.open('output_colour/Share_3.png')
images.append(input_image)
decrypt_with_QR(images)
'''
