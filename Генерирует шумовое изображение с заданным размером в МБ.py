import os
import numpy as np
from PIL import Image
import io

def generate_noise_image_with_target_size(target_size_mb, initial_size=400):
    """
    Генерирует шумовое изображение с приблизительно заданным размером в МБ
    """
    # Начальный размер изображения
    size = initial_size
    
    while True:
        # Создаем случайное изображение
        noise = np.random.randint(0, 256, (size, size, 3), dtype=np.uint8)
        img = Image.fromarray(noise)
        
        # Сохраняем в байтовый поток
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        # Проверяем размер
        current_size_mb = len(img_byte_arr) / (1024 * 1024)
        
        # Если размер близок к целевому, возвращаем результат
        if abs(current_size_mb - target_size_mb) < 0.1:
            return img_byte_arr, size
        
        # Иначе увеличиваем размер изображения
        size += 50

# Создаем директорию для сохранения, если её нет
save_dir = os.path.join(os.path.expanduser("~"), "Downloads", "generated_images")
os.makedirs(save_dir, exist_ok=True)

# Генерация изображения размером около 2.8 МБ
img_data_28mb, size_28mb = generate_noise_image_with_target_size(2.8, initial_size=400)
path_28mb = os.path.join(save_dir, f"noise_{size_28mb}x{size_28mb}_2.8MB.png")

# Сохранение изображения
with open(path_28mb, "wb") as f:
    f.write(img_data_28mb)

# Проверка фактического размера
size_bytes_28mb = os.path.getsize(path_28mb)
size_mb_28mb = size_bytes_28mb / (1024 * 1024)

print(f"Изображение сохранено по пути: {path_28mb}")
print(f"Фактический размер файла: {size_mb_28mb:.2f} МБ") 