from PIL import Image
from utils import key, encryptChannel, decryptChannel, split_image

keySpace=256

imgPath='input.jpeg'

# Open the image using PIL
im = Image.open(imgPath, 'r')

# Resize the image to 256*256 pixels
# im = im.resize((256, 256), Image.ANTIALIAS)

# Extract pizel values

img0, img1 = split_image(im.getdata())

rVal, gVal, bVal = zip(*im.getdata())
rVal0, gVal0, bVal0 = zip(*img0)
rVal1, gVal1, bVal1 = zip(*img1)

partImg = Image.new(im.mode, im.size)
partImg.putdata(list(zip(rVal0, gVal0, bVal0)))
partImg.save("part1.jpg")

partImg = Image.new(im.mode, im.size)
partImg.putdata(list(zip(rVal1, gVal1, bVal1)))
partImg.save("part2.jpg")

newImg = Image.new(im.mode, im.size)
newImg.putdata(list(zip(rVal, gVal, bVal)))
newImg.save("original.jpg")


k=key(0.49373,0.2324878,keySpace)
k_decrypt=key(0.49373,0.2324878,keySpace)

rC0 = encryptChannel(k, rVal0)
gC0 = encryptChannel(k, gVal0)
bC0 = encryptChannel(k, bVal0)

cypherImg = Image.new(im.mode, im.size)
cypherImg.putdata(list(zip(rC0, gC0, bC0)))
cypherImg.save("cipher0.jpg")

rC1 = encryptChannel(k, rVal1)
gC1 = encryptChannel(k, gVal1)
bC1 = encryptChannel(k, bVal1)

cypherImg = Image.new(im.mode, im.size)
cypherImg.putdata(list(zip(rC1, gC1, bC1)))
cypherImg.save("cipher1.jpg")

# Decrypting the image...
r0=decryptChannel(k_decrypt,rC0)
g0=decryptChannel(k_decrypt,gC0)
b0=decryptChannel(k_decrypt,bC0)
r1=decryptChannel(k_decrypt,rC1)
g1=decryptChannel(k_decrypt,gC1)
b1=decryptChannel(k_decrypt,bC1)

newImg = Image.new(im.mode, im.size)

newData=[]

for i in range(len(r0)):
    newData.append((r0[i]+r1[i],g0[i]+g1[i],b0[i]+b1[i]))
newImg.putdata(newData)
newImg.save("decoded.jpg")

