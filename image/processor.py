from PIL import Image, ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        """Инициализация с изображением, переданным из ImageHandler."""
        self.image = image

    def apply_contour_filter(self):
        """Применение фильтра контуров (CONTOUR)."""
        if self.image:
            self.image = self.image.filter(ImageFilter.CONTOUR)
            print("Фильтр контуров (CONTOUR) успешно применен.")
        else:
            print("Сначала загрузите изображение для обработки!")

    def add_text(self, text="Вариант 3"):
        """Добавление текста 'Вариант 3' в центр изображения."""
        if self.image:
            draw = ImageDraw.Draw(self.image)
            font_size = max(20, min(self.image.size) // 20)
            try:
                font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", font_size)
            except Exception as e:
                print(f"Ошибка при загрузке шрифта: {e}")
                font = ImageFont.load_default()

            # Координаты для центрирования текста
            text_width = draw.textlength(text, font=font)
            text_height = font_size
            x = (self.image.size[0] - text_width) / 2
            y = (self.image.size[1] - text_height) / 2

            # Добавляем текст на изображение
            draw.text((x, y), text, font=font, fill=(255, 0, 0))
            print(f"Текст '{text}' успешно добавлен в центр изображения.")
        else:
            print("Сначала загрузите изображение для обработки!")

    def show_image(self):
        """Отображение изображения."""
        if self.image:
            self.image.show()
        else:
            print("Нет изображения для отображения!")

    def get_image(self):
        """Возвращает обработанное изображение."""
        return self.image