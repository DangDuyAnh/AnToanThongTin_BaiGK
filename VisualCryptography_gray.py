import numpy as np
import os, shutil
from PIL import Image
from itertools import permutations
from QRcode import QR_area, QR_fromtext
from pyzbar.pyzbar import decode

def whitepixel(n):
    if n == 2:
        init_matrix = np.array([[0, 0, 1, 1],
                                [0, 0, 1, 1]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r]])
    elif n == 3:
        init_matrix = np.array([[0, 0, 1, 1],
                                [0, 0, 1, 1],
                                [0, 0, 1, 1]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r]])
    elif n == 4:
        init_matrix = np.array([[0, 0, 1, 1],
                                [0, 0, 1, 1],
                                [0, 0, 1, 1],
                                [0, 0, 1, 1]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        list4 = list(permutations(init_matrix[3]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r], list4[r]])
    else:
        print("Value of n is out of range !!!")
        exit()
    return res

def blackpixel(n):
    if n == 2:
        init_matrix = np.array([[0, 0, 1, 1],
                                [1, 1, 0, 0]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r]])

    elif n == 3:
        init_matrix = np.array([[1, 1, 0, 0],
                                [0, 1, 1, 0],
                                [1, 0, 0, 1]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r]])

    elif n == 4:
        init_matrix = np.array([[1, 1, 0, 0],
                                [0, 1, 1, 0],
                                [0, 0, 1, 1],
                                [1, 0, 0, 1]])
        list1 = list(permutations(init_matrix[0]))
        list2 = list(permutations(init_matrix[1]))
        list3 = list(permutations(init_matrix[2]))
        list4 = list(permutations(init_matrix[3]))
        r = np.random.randint(0, len(list1))
        res = np.array([list1[r], list2[r], list3[r], list4[r]])

    else:
        print("Value of n is out of range !!!")
        exit()

    return res

def encrypt(input_matrix, n):
    (row, column) = input_matrix.shape
    shares = np.empty(n, dtype=object)
    for i in range(n):
        shares[i] = np.empty((2 * row, 2 * column)).astype('uint8')
    for i in range(row):
        for j in range(column):
            if input_matrix[i][j] == 1:
                colour = whitepixel(n)
                for k in range(n):
                    shares[k][2 * i, 2 * j] = colour[k][0]
                    shares[k][2 * i, 2 * j + 1] = colour[k][1]
                    shares[k][2 * i + 1, 2 * j] = colour[k][2]
                    shares[k][2 * i + 1, 2 * j + 1] = colour[k][3]
            elif input_matrix[i][j] == 0:
                colour = blackpixel(n)
                for k in range(n):
                    shares[k][2 * i, 2 * j] = colour[k][0]
                    shares[k][2 * i, 2 * j + 1] = colour[k][1]
                    shares[k][2 * i + 1, 2 * j] = colour[k][2]
                    shares[k][2 * i + 1, 2 * j + 1] = colour[k][3]
    return shares

def decrypt(shares):
    n = len(shares)
    overlap_matrix = shares[0]
    for i in range(1, n):
        overlap_matrix = overlap_matrix & shares[i]
    (row, column) = shares[0].shape
    row = int(row / 2)
    column = int(column / 2)
    extraction_matrix = np.ones((row, column))

    for i in range(row):
        for j in range(column):
            cnt = np.sum(overlap_matrix[2 * i:2 * (i + 1), 2 * j:2 * (j + 1)])
            if cnt == 0:
                extraction_matrix[i][j] = 0

    return overlap_matrix, extraction_matrix

def convertGrayToBinary(image):
    grayScaleImage = image.copy()
    (row, column) = grayScaleImage.shape
    binaryImage = np.ones((row, column, 8))
    for i in range(8):
        binaryImage[:, :, i] = (grayScaleImage.copy()) % 2
        grayScaleImage = (grayScaleImage / 2).astype('uint8')

    return binaryImage

def convertBinaryToGray(image):
    binaryImage = image.copy()
    (row, column, _) = binaryImage.shape
    grayScaleImage = np.zeros((row, column))
    for i in range(8):
        grayScaleImage = (grayScaleImage * 2 + binaryImage[:, :, 7 - i]).astype('uint8')
    return grayScaleImage

def BLD_encrypt(input_image, n):
    input_matrix = np.asarray(input_image)
    binaryDecomposition = convertGrayToBinary(input_matrix.copy())
    (row, column, _) = binaryDecomposition.shape
    binaryShares = np.empty(n, dtype=object)
    for i in range(n):
        binaryShares[i] = np.zeros((2 * row, 2 * column, 8)).astype('uint8')
    for index in range(8):
        shares = encrypt(binaryDecomposition[:, :, index], n)
        for i in range(n):
            binaryShares[i][:, :, index] = shares[i]
    secret_shares = []
    for i in range(n):
        secret_shares.append(convertBinaryToGray(binaryShares[i]))
    return secret_shares

def BLD_decrypt(secret_shares):
    binaryShares = []
    n = len(secret_shares)
    for i in range(n):
        binaryShares.append(convertGrayToBinary(secret_shares[i]))
        binaryShares[i] = binaryShares[i].astype('uint8')
    (row, column, _) = binaryShares[0].shape
    binaryOverlapMatrix = np.zeros((row, column, 8)).astype('uint8')
    binaryExtractionMatrix = np.zeros((int(row / 2), int(column / 2), 8)).astype('uint8')
    for index in range(8):
        shares = []
        for i in range(n):
            shares.append(binaryShares[i][:, :, index])
        binaryOverlapMatrix[:, :, index], binaryExtractionMatrix[:, :, index] = decrypt(shares)
    overlap_matrix = convertBinaryToGray(binaryOverlapMatrix)
    extraction_matrix = convertBinaryToGray(binaryExtractionMatrix)
    extraction_output = Image.fromarray(extraction_matrix.astype(np.uint8))
    overlap_output = Image.fromarray(overlap_matrix.astype(np.uint8))
    extraction_output = extraction_output.resize((overlap_output.size[0], overlap_output.size[0]))
    extraction_matrix = np.asarray(extraction_output)
    return overlap_matrix, extraction_matrix

def encrypt_with_QR(input_image, message, share_size):         # Mã hóa ảnh xám với QR, các ảnh sẽ được lưu vào thư mục output_gray
    # clean the output folder
    folder = 'output_gray'
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    
    # crop thành ảnh vuông
    input_image = input_image.convert('L')
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
    image_temp = image_temp.convert('L')
    const_size = image_temp.size[0]
    square_img = square_img.resize((int(const_size/(share_size - share_size%2)),int(const_size/(share_size - share_size%2))))
    shares = BLD_encrypt(square_img, share_size)
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
        temp = Image.fromarray(temp.astype(np.uint8))
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
    image_temp = image_temp.convert('L')
    const_size = image_temp.size[0]
    QR_image = np.asarray(image_temp).astype(np.uint8)
    QR_area0 = QR_area(image_temp, pos_temp)
    
    temps = []
    for i in range(share_size):
        temp = np.asarray(shares[i])
        temps.append(temp)
    overlap_matrix, extraction_matrix = BLD_decrypt(temps)
    for i in range(const_size):
        for j in range(const_size):
            if QR_area0[i][j] == 1:
                overlap_matrix[i][j] = QR_image[i][j]
                extraction_matrix[i][j] = QR_image[i][j]
    extraction_output = Image.fromarray(extraction_matrix.astype(np.uint8))
    overlap_output = Image.fromarray(overlap_matrix.astype(np.uint8))
    output_name = os.path.join('output_gray','Overlap.png')
    overlap_output.save(output_name)
    extraction_output.save("output_gray/Extraction.png")
    print(output_name)
    return overlap_output, extraction_output

# Test thử chương trình

# Mã hóa
'''
message = "001200612738"
input_image = Image.open('Jennie_gray.jpg')
encrypt_with_QR(input_image, message, 3)
'''

# Giải mã
'''
images = []
input_image = Image.open('output_gray/Share_1.png')
images.append(input_image)
input_image = Image.open('output_gray/Share_2.png')
images.append(input_image)
input_image = Image.open('output_gray/Share_3.png')
images.append(input_image)
output_image, final_output = decrypt_with_QR(images)
'''