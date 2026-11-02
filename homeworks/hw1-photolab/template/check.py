import cv2
import os
import glob

print(f"{'Файл':<15} | {'Размеры (ШxВ)':<12} | {'Макс. сторона':<12} | {'Вес (МБ)':<8} | {'Статус'}")
print("-" * 75)

for path in sorted(glob.glob("data/*.jpg")):
    img = cv2.imread(path)
    if img is not None:
        h, w = img.shape[:2]
        max_side = max(h, w)
        size_mb = os.path.getsize(path) / (1024 * 1024)
        
        # Проверка условий задания: <= 2000px и <= 1.5 МБ
        is_ok = max_side <= 2000 and size_mb <= 1.5
        status = "✅ ОК" if is_ok else "❌ Много"
        
        print(f"{os.path.basename(path):<15} | {w}x{h} px{' '*(12-len(f'{w}x{h} px'))} | {max_side} px{' '*(12-len(f'{max_side} px'))} | {size_mb:.2f} МБ{' '*(8-len(f'{size_mb:.2f}'))} | {status}")
    else:
        print(f"{os.path.basename(path):<15} | Не удалось прочитать файл")
