from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, font_path=None, font_size=30, image_size=(400, 200), text_color=(0, 0, 0), background_color=(255, 255, 255)):
    """
    Създава изображение с текст.

    :param text: Текстът, който искаш да се покаже.
    :param font_path: Път към файл с шрифт (ако не е зададен, ще се използва стандартен шрифт).
    :param font_size: Размер на шрифта.
    :param image_size: Размер на изображението (широчина, височина).
    :param text_color: Цвят на текста (R, G, B).
    :param background_color: Цвят на фона (R, G, B).
    :return: Обект на изображението.
    """
    # Създаване на празно изображение
    image = Image.new("RGB", image_size, background_color)
    draw = ImageDraw.Draw(image)

    # Зареждане на шрифт
    try:
        if font_path:
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.load_default()  # Стандартен шрифт
    except IOError:
        print("Грешка при зареждане на шрифта. Използвам стандартен шрифт.")
        font = ImageFont.load_default()

    # Изчисляване на размера на текста с textbbox
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Изчисляване на позицията на текста (центриране)
    x = (image_size[0] - text_width) / 2
    y = (image_size[1] - text_height) / 2

    # Добавяне на текста към изображението
    draw.text((x, y), text, font=font, fill=text_color)

    return image

# Примерно използване
if __name__ == "__main__":
    text = "ERROR 404"
    image = text_to_image(
        text,
        font_path="arial.ttf",  # Път към шрифтов файл
        font_size=40,
        image_size=(600, 300),
        text_color=(255, 255, 255),
        background_color=(0, 0, 0)
    )

    # Запазване на изображението
    image.save("output_image.png")
    print("Изображението е запазено като 'output_image.png'")

    # Показване на изображението
    image.show()