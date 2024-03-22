import cv2
import easyocr
import numpy as np
from matplotlib import pyplot as plt
image_file = "resim15-1.jpg"
img = cv2.imread(image_file)
new_width = 800
new_height = int(img.shape[0] * (new_width / img.shape[1]))
img = cv2.resize(img, (new_width, new_height))
img2 = cv2.resize(img, (new_width, new_height))

# Gri tonlama
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding işlemi
_, thresh = cv2.threshold(img, 180, 252, cv2.THRESH_OTSU)
siyah_piksel_sayisi = thresh.size - cv2.countNonZero(thresh)
if siyah_piksel_sayisi < thresh.size * 0.45:
    img = thresh


kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_open)

kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel_close)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
img = clahe.apply(img)

reader = easyocr.Reader(['en', 'tr'])
text = reader.readtext(img2)

# Tanınan metinleri görüntü üzerine yazma
metin =''
for t in text:
    bbox, text, score = t
    metin += text + ' '
    cv2.rectangle(img2, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])), (0, 255, 75), 2)
    cv2.putText(img2, text, (int(bbox[0][0]), int(bbox[0][1])), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 75, 180), 2)
print(metin)


cv2.imshow("Orjinal Resim ", img2)
cv2.waitKey(0)
