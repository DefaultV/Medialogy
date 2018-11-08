# ################################# #
#                                   #
# Topic #6: Convert from RGB to HSI #
# Author: Jannick Drews             #
#                                   #
# ################################# #
# Make a Python program that can convert from RGB to HSI. 
# Input: 
#   - An RGB image 
# Output: 
#   - Three images:
#       * a H-image 
#       * a S-image
#       * an I-image
import cv2, numpy as np, matplotlib.pyplot as plt, math

#img = cv2.imread("img/lena.png", 3)
img = cv2.imread("baboon.jpg", 3)
original = img

def HSI_Conv(im):
    # Algorithm:
    original = im
    hsi_h = np.zeros((im.shape[0], im.shape[1]), np.float32)
    hsi_s = np.zeros((im.shape[0], im.shape[1]), np.float32)
    hsi_i = np.zeros((im.shape[0], im.shape[1]), np.float32)
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
             
            # Get RGB(Remember to use BGR_TO_RGB function further down for correct vals)
            red = int(im[x][y][0])
            green = int(im[x][y][1])
            blue = int(im[x][y][2])

            # Get HSI
            # Hue CORRECT
            top = (red - green) + (red - blue)
            bot = 2 * np.sqrt((red - green)*(red - green) + (red - blue)*(green - blue))
            if (bot == 0): # Exception if R = G = B
                saturation = 0.0
                hue = 0.0
                intensity = 255.0
                hsi_h[x][y] = hue
                hsi_s[x][y] = saturation
                hsi_i[x][y] = intensity
                continue
            formula = np.arccos( np.divide(top,bot) )
            print ("rgb: {},{},{} || formula:{} ||".format(red, green, blue, formula))

            hue = 0.0
            if (green >= blue):
                hue = formula
            else:
                hue = 2*np.pi - formula
            print("after boolean: ", hue)
            hue = (hue * 180)/np.pi # rads to degrees
            print("after degree conversion: ", hue)
            
            # Saturation CORRECT
            sum_rgb = red + green + blue
            division = np.divide(min(red,green,blue), float(sum_rgb))
            mult = 3.0 * division
            saturation = 1.0 - mult
            # print(min(red,green,blue), float(sum_rgb), saturation, division, mult)

            # Intensity CORRECT
            intensity = np.divide(sum_rgb, 3)
            #print(sum_rgb, intensity)
            
            # Output respective channels
            hsi_h[x][y] = hue
            hsi_s[x][y] = saturation
            hsi_i[x][y] = intensity
            #print("h s v; {} {} {}".format(hsi_h[x][y], hsi_s[x][y], hsi_i[x][y]))

    # Show plot:
    plt.subplot(141), plt.imshow(original), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(142), plt.imshow(hsi_h), plt.title('Hue')
    plt.xticks([]), plt.yticks([])
    plt.subplot(143), plt.imshow(hsi_s), plt.title('Saturation')
    plt.xticks([]), plt.yticks([])
    plt.subplot(144), plt.imshow(hsi_i), plt.title('Intensity')
    plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.waitKey(0)


# Fast implementation since the real assignment is RGB -> HSI
def BGR_TO_RGB(im):
    tmp = np.zeros((original.shape[0], original.shape[1]))
    tmp[:,:] = original[:,:,2]
    original[:,:,2] = original[:,:,0]
    original[:,:,0] = tmp[:,:]
    return original

img = BGR_TO_RGB(img)
HSI_Conv(img)
#HSI_Conv(DEBUG)
