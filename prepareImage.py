# ==============================================================================
#   copyright (C) 2018 De Groskovskaja Marco
#
#   Licensed under the Apache License, Version 2.0;
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# ==============================================================================

from PIL import Image, ImageFilter
import cv2
import numpy as np

def imageprepare(argv):
    im = cv2.imread(argv)

    # Convert to grayscale and apply Gaussian filtering
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

    # Threshold the image
    ret, im_th_inv = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)
    ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY)
    # Find contours in the image
    _, contours, hierarchy = cv2.findContours(im_th_inv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # List of the digits in the image
    digits = []
    imgToPrint = im.copy()
    # Kernel: morphologyEx
    kernel1 = np.ones((10, 10), dtype=np.uint8)
    kernel2 = np.ones((2, 2), dtype=np.uint8)
    for i in range(0, len(contours)):
        cnt = contours[i]
        #mask = np.zeros(im2.shape,np.uint8)
        #cv2.drawContours(mask,[cnt],0,255,-1)
        x,y,w,h = cv2.boundingRect(cnt)
        # If the rect is enought to contain the digit
		## NOTE: these values can be changed if necessary
        if (w > 20) and (h > 20):
            imgToPrint = cv2.rectangle(imgToPrint,(x,y),(x+w,y+h),(0,255,0),2)
            # Take each digit
            digit = im_th[y:y+h,x:x+w]
            cv2.imwrite('./extracted_img/dig_'+str(i)+'.jpg', digit)
            # Resize the image
            roi = digit.copy()
            if not (w<(h*2)):#If is not number 1
                roi = cv2.resize(roi, (500, 500), interpolation=cv2.INTER_AREA)
                roi = cv2.morphologyEx(roi, cv2.MORPH_CLOSE, kernel2)
                roi = cv2.morphologyEx(roi, cv2.MORPH_OPEN, kernel2)

                for counter in range (0, 0):
                    roi = cv2.erode(roi, kernel2)
                roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)

            cv2.imwrite('./extracted_img/roi_'+str(i)+'.jpg', roi)

            edited_img = imageprepare2('./extracted_img/roi_'+str(i)+'.jpg', i)

            # Append each digit
            digits.append(edited_img)
            
            
    #cv2.imshow("Resulting Image with Rectangular ROIs", imgToPrint)
    #cv2.waitKey()
    
    return digits

def imageprepare2(argv, counter):
    """
    This function returns the pixel values.
    The input is a png file location.
    """
    im = Image.open(argv).convert('L')
    width = float(im.size[0])
    height = float(im.size[1])
    newImage = Image.new('L', (28, 28), (255)) #creates white canvas of 28x28 pixels
    
    if width > height: #check which dimension is bigger
        #Width is bigger. Width becomes 20 pixels.
        nheight = int(round((20.0/width*height),0)) #resize height according to ratio width
        #if (nheigth == 0): #rare case but minimum is 1 pixel
        #    nheigth = 1  
        # resize and sharpen
        img = im.resize((20,nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wtop = int(round(((28 - nheight)/2),0)) #caculate horizontal pozition
        newImage.paste(img, (4, wtop)) #paste resized image on white canvas
    else:
        #Height is bigger. Heigth becomes 20 pixels. 
        nwidth = int(round((20.0/height*width),0)) #resize width according to ratio height
        if (nwidth == 0): #rare case but minimum is 1 pixel
            nwidth = 1
         # resize and sharpen
        img = im.resize((nwidth,20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wleft = int(round(((28 - nwidth)/2),0)) #caculate vertical pozition
        newImage.paste(img, (wleft, 4)) #paste resized image on white canvas

    tv = list(newImage.getdata()) #get pixel values
    
    #normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    tva = [ (255-x)*1.0/255.0 for x in tv]
    newImage.save('./extracted_img/tva_'+str(counter)+'.jpg')
    return tva
