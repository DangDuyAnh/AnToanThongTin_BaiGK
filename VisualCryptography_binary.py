import numpy as np
import os, shutil
from PIL import Image
from itertools import permutations
from QRcode import QR_area, QR_fromtext
from pyzbar.pyzbar import decode

def whitepixel(n):
    if n == 2:
        init_matrix = np.array([[0, 1],
                                [0, 1]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r]])

    elif n == 3:
        init_matrix = np.array([[0, 1, 1],
                                [0, 1, 1],
                                [0, 1, 1]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r]])

    elif n == 4:
        init_matrix = np.array([[0, 1, 1, 1],
                                [0, 1, 1, 1],
                                [0, 1, 1, 1],
                                [0, 1, 1, 1]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        list4 = list(permutations(init_matrix[3]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r], list4[r]])

    elif n == 5:
        init_matrix = np.array([[0, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        list4 = list(permutations(init_matrix[3]))
        list5 = list(permutations(init_matrix[4]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r], list4[r], list5[r]])

    elif n == 6:
        init_matrix = np.array([[0, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        list4 = list(permutations(init_matrix[3]))
        list5 = list(permutations(init_matrix[4]))
        list6 = list(permutations(init_matrix[5]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r], list4[r], list5[r], list6[r]])

    elif n == 7:
        init_matrix = np.array([[0, 1, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1, 1]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        list4 = list(permutations(init_matrix[3]))
        list5 = list(permutations(init_matrix[4]))
        list6 = list(permutations(init_matrix[5]))
        list7 = list(permutations(init_matrix[6]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r], list4[r], list5[r], list6[r], list7[r]])

    elif n == 8:
        init_matrix = np.array([[0, 1, 1, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1, 1, 1],
                                [0, 1, 1, 1, 1, 1, 1, 1]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        list4 = list(permutations(init_matrix[3]))
        list5 = list(permutations(init_matrix[4]))
        list6 = list(permutations(init_matrix[5]))
        list7 = list(permutations(init_matrix[6]))
        list8 = list(permutations(init_matrix[7]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r], list4[r], list5[r], list6[r], list7[r], list8[r]])

    else:
        print("Value of n is out of range !!!")
        exit()

    return res

def blackpixel(n):
    if n == 2:
        init_matrix = np.array([[0, 1],
                                [1, 0]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r]])

    elif n == 3:
        init_matrix = np.array([[0, 1, 1],
                                [1, 0, 1],
                                [1, 1, 0]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r]])

    elif n == 4:
        init_matrix = np.array([[0, 1, 1, 1],
                                [1, 0, 1, 1],
                                [1, 1, 0, 1],
                                [1, 1, 1, 0]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        list4 = list(permutations(init_matrix[3]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r], list4[r]])

    elif n == 5:
        init_matrix = np.array([[0, 1, 1, 1, 1],
                                [1, 0, 1, 1, 1],
                                [1, 1, 0, 1, 1],
                                [1, 1, 1, 0, 1],
                                [1, 1, 1, 1, 0]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        list4 = list(permutations(init_matrix[3]))
        list5 = list(permutations(init_matrix[4]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r], list4[r], list5[r]])

    elif n == 6:
        init_matrix = np.array([[0, 1, 1, 1, 1, 1],
                                [1, 0, 1, 1, 1, 1],
                                [1, 1, 0, 1, 1, 1],
                                [1, 1, 1, 0, 1, 1],
                                [1, 1, 1, 1, 0, 1],
                                [1, 1, 1, 1, 1, 0]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        list4 = list(permutations(init_matrix[3]))
        list5 = list(permutations(init_matrix[4]))
        list6 = list(permutations(init_matrix[5]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r], list4[r], list5[r], list6[r]])

    elif n == 7:
        init_matrix = np.array([[0, 1, 1, 1, 1, 1, 1],
                                [1, 0, 1, 1, 1, 1, 1],
                                [1, 1, 0, 1, 1, 1, 1],
                                [1, 1, 1, 0, 1, 1, 1],
                                [1, 1, 1, 1, 0, 1, 1],
                                [1, 1, 1, 1, 1, 0, 1],
                                [1, 1, 1, 1, 1, 1, 0]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        list4 = list(permutations(init_matrix[3]))
        list5 = list(permutations(init_matrix[4]))
        list6 = list(permutations(init_matrix[5]))
        list7 = list(permutations(init_matrix[6]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r], list4[r], list5[r], list6[r], list7[r]])

    elif n == 8:
        init_matrix = np.array([[0, 1, 1, 1, 1, 1, 1, 1],
                                [1, 0, 1, 1, 1, 1, 1, 1],
                                [1, 1, 0, 1, 1, 1, 1, 1],
                                [1, 1, 1, 0, 1, 1, 1, 1],
                                [1, 1, 1, 1, 0, 1, 1, 1],
                                [1, 1, 1, 1, 1, 0, 1, 1],
                                [1, 1, 1, 1, 1, 1, 0, 1],
                                [1, 1, 1, 1, 1, 1, 1, 0]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        list4 = list(permutations(init_matrix[3]))
        list5 = list(permutations(init_matrix[4]))
        list6 = list(permutations(init_matrix[5]))
        list7 = list(permutations(init_matrix[6]))
        list8 = list(permutations(init_matrix[7]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r], list4[r], list5[r], list6[r], list7[r], list8[r]])

    else:
        print("Value of n is out of range !!!")
        exit()

    return res

def encrypt(input_image, n):
    input_matrix = np.asarray(input_image)
    (row, column) = input_matrix.shape
    shares = np.empty(n, dtype=object)
    for i in range(n):
        shares[i] = np.empty((row, n * column)).astype('uint8')

    for i in range(row):
        for j in range(column):
            if input_matrix[i][j] == 1:
                colour = whitepixel(n)
                for k in range(n):
                    for jj in range(n * j, n * (j + 1)):
                        shares[k][i, jj] = colour[k][jj - n * j]
            elif input_matrix[i][j] == 0:
                colour = blackpixel(n)
                for k in range(n):
                    for jj in range(n * j, n * (j + 1)):
                        shares[k][i, jj] = colour[k][jj - n * j]
    return shares

def decrypt(shares):
    n = len(shares)
    overlap_matrix = shares[0]
    for i in range(1, n):
        overlap_matrix = overlap_matrix & shares[i]
    (row, column) = shares[0].shape
    column = int(column / n)
    extraction_matrix = np.ones((row, column))

    for i in range(row):
        for j in range(column):
            cnt = np.sum(overlap_matrix[i, n * j:n * (j + 1)])
            if cnt == 0:
                extraction_matrix[i][j] = 0

    extraction_output = Image.fromarray(extraction_matrix.astype(np.uint8) * 255)
    overlap_output = Image.fromarray(overlap_matrix.astype(np.uint8))
    extraction_output = extraction_output.resize((overlap_output.size[0], overlap_output.size[0]))
    extraction_matrix = np.asarray(extraction_output)
    return overlap_matrix, extraction_matrix

def encrypt_with_QR(input_image, message, share_size):         # Mã hóa ảnh binary với QR, các ảnh sẽ được lưu vào thư mục output_binary
    # clean the output folder
    folder = 'output_binary'
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
    input_image = input_image.convert('1')
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
    image_temp = image_temp.convert('1')
    const_size = image_temp.size[0]
    square_img = square_img.resize((int(const_size / (share_size - share_size % 2)), (int(const_size / (share_size - share_size % 2))) * (share_size - share_size % 2)))
    shares = encrypt(square_img, share_size)
    results = []
    QR_image = np.asarray(image_temp).astype(np.uint8)
    QR_area0 = QR_area(image_temp, pos_temp)
    
    for i in range(share_size):
        temp = np.random.randint(0, 256, size=(const_size, const_size))
        image = shares[i]
        for a in range(const_size):
            for b in range(const_size):
                if QR_area0[a][b] == 1:
                    temp[a][b] = QR_image[a][b]
                else:
                    temp[a][b] = image[a][b]
        temp = Image.fromarray(temp.astype(np.uint8)* 255)
        results.append(temp)
    for i in range(share_size):
        name = os.path.join(folder, 'Share_{}.png'.format(i + 1))
        print(name)
        results[i].save(name)

def decrypt_with_QR(shares):                      # giải mã các ảnh QR, và ghi thêm tên bệnh nhân
    share_size = len(shares)
    decoded_data = decode(shares[0])
    data = decoded_data[0].data.decode()
    image_temp, pos_temp = QR_fromtext(data)
    image_temp = image_temp.convert('1')
    const_size = image_temp.size[0]
    QR_image = np.asarray(image_temp).astype(np.uint8)*255
    QR_area0 = QR_area(image_temp, pos_temp)
    
    temps = []
    for i in range(share_size):
        temp = np.asarray(shares[i])
        temps.append(temp)
    overlap_matrix, extraction_matrix = decrypt(temps)
    for i in range(const_size):
        for j in range(const_size):
            if QR_area0[i][j] == 1:
                overlap_matrix[i][j] = QR_image[i][j]
                extraction_matrix[i][j] = QR_image[i][j]
    extraction_output = Image.fromarray(extraction_matrix.astype(np.uint8))
    overlap_output = Image.fromarray(overlap_matrix.astype(np.uint8))
    output_name = os.path.join('output_binary','Overlap.png')
    overlap_output.save(output_name, mode='1')
    extraction_output.save("output_binary/Extraction.png", mode='1')
    print(output_name)
    return overlap_output, extraction_output


# Test thử chương trình

# Mã hóa
'''
message = "001200612738"
input_image = Image.open('Jennie_binary.jpg')
encrypt_with_QR(input_image, message, 5)
'''

# Giải mã
'''
images = []
input_image = Image.open('output_binary/Share_1.png')
images.append(input_image)
input_image = Image.open('output_binary/Share_2.png')
images.append(input_image)
input_image = Image.open('output_binary/Share_3.png')
images.append(input_image)
input_image = Image.open('output_binary/Share_4.png')
images.append(input_image)
input_image = Image.open('output_binary/Share_5.png')
images.append(input_image)
decrypt_with_QR(images)
'''