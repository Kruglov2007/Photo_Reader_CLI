import cv2
import pytesseract

# 1. Указываем путь к установленному Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 2. Загружаем изображение и переводим в RGB для Tesseract
img = cv2.imread("./images/img_1.png")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 3. Настройки распознавания
tess_config = r'--oem 3 --psm 6'
lang_config = 'rus+eng'

print("Распознавание текста... Пожалуйста, подождите.")

# 4. Получаем чистый текст одной командой
recognized_text = pytesseract.image_to_string(img_rgb, config=tess_config, lang=lang_config)

# 5. Выводим результат в консоль PyCharm
print("\n=== РАСПОЗНАННЫЙ ТЕКСТ ===")
print(recognized_text)

# 6. Автоматически сохраняем результат в файл .txt
output_file = "result.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(recognized_text)

print(f"\n[Успешно] Текст сохранен в файл: {output_file}")
