from PIL import Image, ImageDraw, ImageFont


image_path = input("Enter image path: ").replace("/", "\\")

text_type = int(input("Enter your choice:\n1. Only bottom text\n2. Bottom and top text\n"))

top_text = ""
bottom_text = ""

if text_type == 1:
    bottom_text = input("Enter bottom text: ")
elif text_type == 2:
    top_text = input("Enter top text: ")
    bottom_text = input("Enter bottom text: ")
else:
    print("Incorrect input!")
    quit()

image = Image.open(image_path)
width, height = image.size
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("Comic.ttf", size=70)

text = draw.textbbox((0, 0), top_text, font)

draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill="black")

draw.text(((width - text[2]) / 2, (height - text[3] - 10)), bottom_text, font=font, fill="black")

image.save("your_meme.jpg")
