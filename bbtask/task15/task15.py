# Не вийшло в мене
from PIL import Image, ImageDraw, ImageFont

width, height = 800, 400
background_color = (100, 150, 255) 
text_color = (255, 255, 255) 

image = Image.new('RGB', (width, height), background_color)

draw = ImageDraw.Draw(image)

try:
    font = ImageFont.truetype("arial.ttf", 40) 
except IOError:
    font = ImageFont.load_default()  

text = "Я програмую на Пайтон дуже добре"

text_width, text_height = draw(text, font=font)

x = (width - text_width) / 2
y = (height - text_height) / 2

draw.text((x, y), text, font=font, fill=text_color)

image.save('programming_image.png')

image.show()