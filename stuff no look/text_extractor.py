import keyboard
from PIL import Image
from pytesseract import pytesseract
print('-----')

# Setting up tesseract
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

# Image set-up
#"D:\Downloads\btd6_hotkeys1.png"
#"D:\Downloads\money3.png"
image_path = r"D:\Downloads\btd6_hotkeys1.png"
img = Image.open(image_path)
#img = img.convert('LA')
# img.show()

# 6,7,8 seem to be best
text = pytesseract.image_to_string(img, config='--psm 9')
print(text)

