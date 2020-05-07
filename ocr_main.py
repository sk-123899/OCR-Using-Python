import check
import pytesseract
from PIL import Image

img=Image.open('image2.jpg')
text=pytesseract.image_to_string(img)
file1=open(r"D:\shreyas\All Projects\ocr project in python\lc.txt","w")
file1.writelines(text)
file1.close()

print(text)

check.name_check()


