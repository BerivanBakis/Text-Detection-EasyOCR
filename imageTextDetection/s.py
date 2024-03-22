import cv2
import easyocr

# Görüntüyü yükle
image_path = '11.jpg'
img = cv2.imread(image_path)
new_width = 600
new_height = int(img.shape[0] * (new_width / img.shape[1]))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.resize(img, (new_width, new_height))
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Kenar belirleme
edges = cv2.Canny(blur, 50, 150)

# Kenarları genişletme (dilation)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilated = cv2.dilate(edges, kernel, iterations=1)

# Metin tanıma
reader = easyocr.Reader(['en', 'tr'])
text = reader.readtext(img)

# Tanınan metinleri görüntü üzerine yazma
metin =''
for t in text:
    bbox, text, score = t
    metin += text + ' '
    cv2.rectangle(img, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])), (0, 255, 75), 2)
    cv2.putText(img, text, (int(bbox[0][0]), int(bbox[0][1])), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 75, 180), 2)
print(metin)
# Görüntüyü göster
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
