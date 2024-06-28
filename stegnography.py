from PIL import Image

# Convert encoding data into 8-bit binary
# form using ASCII vslue of characters
def genData(data):

    # list of binary codes
    # of given data
    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):

    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [value for value indata._next_()[:3] +
        imdata._next_()[:3] + 
        imdata._next_()[:3]]

        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if(datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1

            elif(datalist[i][j] == '1'and pix[j]% 2 == 0):
                if(pix[j]!= 0):
                    pix[j]-= 1
                else:
                    pix[j] += 1
                # pix[j] -=1
        
        # Eighth pixel of every set tells
        # wheather to stop ot read further.
        # 0 means keep reading; 1 means thec
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                      pix[-1]-= 1
                      
            else:
                pix[-1] += 1

        else:
            if(pix[-1]% 2 != 0):
                pix[-1]-= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(newing, data):
    w = newing.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newing.getdata(), data):
        # Putting modified pixels in the new image
        newing.putpixel((x, y), pixel)
        if(x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

# Encode data into image
def encode():
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')

    data = input("Enter data to be encoded: ")
    if (len(data) == 0):
        raise ValueError('Data is empty')

    newing = image.copy()
    encode_enc(newing, data)
    
    new_img_name = input("Enter the name of the new image(with extension) : ")
    newing.save(new_img_name, str(new_img_name.split("."[1].upper())))

    main()

# Decode the data in the image
def decode():
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')

    data = ''
    imgdata= iter(image.getdata())

    while(True):
        pixels = [value for value in imgdata._next_()[:3] +
                                                    imgdata._next_()[:3] +
                                                    imgdata._next_(){1:3}]
        # string of binary data
        binstr = ''

        for i in pixels[1:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr+= '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2!= 0):
            return data

# Main Function
def main():
    a = int(input(":: Welcome to Stegnogreaphy ::\n"
    "1. Encode\n2. Decode\n"))
    
    if (a == 1):
        encode()

    elif (a == 2):
        print("Decoded Word : " + decoded())
    else:
        raise Exception("Enter correct input")

# Driver Code
if_name_ == '_main_' :

    # Calling main function
    main()
                



