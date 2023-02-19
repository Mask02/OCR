import cv2
import pytesseract


img = cv2.imread(r"C:\Users\shoai\OneDrive\Desktop\OCR(Object Image Recognization)\images\1.png")
img = cv2.cvtColor (img, cv2.COLOR_BGR2RGB)
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print("\n\nOCR Text:\n\t")
print(pytesseract.image_to_string(img))
print("\n\n")

# Dectecting words
hImg, wImg,_ = img.shape

boxes = pytesseract.image_to_data(img)
print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        if len(b)==12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x,y), (w+x, h+y), (0,0, 255), 1)
            cv2.putText(img, b[11], (x, y-2), cv2.FONT_HERSHEY_PLAIN, 1, (25, 25, 255), 1)


cv2.imshow("img", img)
cv2.waitKey(0)