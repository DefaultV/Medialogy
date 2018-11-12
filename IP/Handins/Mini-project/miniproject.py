# Topic #6: Convert from RGB to HSI #
# Author: Jannick Drews             #
import cv2, numpy as np, matplotlib.pyplot as plt

def HSI_Conv(im):
    # Algorithm:
    original = im
    hsi_h = np.zeros((im.shape[1], im.shape[0]), np.float32)
    hsi_s = np.zeros((im.shape[1], im.shape[0]), np.float32)
    hsi_i = np.zeros((im.shape[1], im.shape[0]), np.float32)
    for x in range(im.shape[1]):
        for y in range(im.shape[0]):

            # Get RGB(Remember to use BGR_TO_RGB function further down for correct vals)
            red = int(im[x][y][0])
            green = int(im[x][y][1])
            blue = int(im[x][y][2])

            # Get HSI (Hue first)
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
            #print ("rgb: {},{},{}\nFormula return:{}".format(red, green, blue, formula))

            hue = 0.0
            if (green >= blue):
                hue = formula
            else:
                hue = 2*np.pi - formula
            #print("G>=B: {}".format(hue))
            hue = (hue * 180)/np.pi # rads to degrees
            #print("Degree conversion: {}\n".format(hue))

            # Saturation
            sum_rgb = red + green + blue
            division = np.divide(min(red,green,blue), float(sum_rgb))
            mult = 3.0 * division
            saturation = 1.0 - mult

            # Intensity
            intensity = np.divide(sum_rgb, 3)

            # Output respective channels
            hsi_h[x][y] = hue
            hsi_s[x][y] = saturation
            hsi_i[x][y] = intensity

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
    return hsi_h, hsi_s, hsi_i

# Fast implementation since the real assignment is RGB -> HSI
def BGR_TO_RGB(im):
    tmp = np.zeros((im.shape[0], im.shape[1]))
    tmp[:,:] = im[:,:,2]
    im[:,:,2] = im[:,:,0]
    im[:,:,0] = tmp[:,:]
    return im

img = cv2.imread("baboon.jpg", 3)
img = BGR_TO_RGB(img)
HSI_Conv(img)
