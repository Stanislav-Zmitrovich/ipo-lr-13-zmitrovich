from PIL import Image
from datetime import datetime

class ImageHandler:
    def __init__(self, image_path):
       
        self.image_path = image_path
        self.image = None

    def load_image(self):
        
        try:
            self.image = Image.open(self.image_path)
            print(f"Изображение успешно загружено: {self.image_path}")
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")

    def create_thumbnail(self, max_size=(200, 200)):
        """Создание уменьшенного изображения (thumbnail) с максимальными размерами 200x200 пикселей."""
        if self.image:
            self.image.thumbnail(max_size)
            print(f"Уменьшенное изображение создано с максимальными размерами {max_size}")
        else:
            print("Сначала загрузите изображение!")

    def save_image_with_date(self, output_prefix, format="JPEG"):
        """Сохранение уменьшенного изображения с текущей датой в имени файла."""
        if self.image:
            date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_path = f"{output_prefix}_{date_str}.jpg"
            try:
                self.image.save(output_path, format=format)
                print(f"Изображение успешно сохранено как: {output_path}")
            except Exception as e:
                print(f"Ошибка при сохранении изображения: {e}")
        else:
            print("Сначала загрузите изображение!")

    def get_image_for_processing(self):
        
        if self.image:
            return self.image.copy()
        else:
            print("Сначала загрузите изображение!")
            return None