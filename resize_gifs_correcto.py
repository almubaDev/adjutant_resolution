# Archivo: resize_gifs_correcto.py

import os
from PIL import Image, ImageSequence

# Rutas relativas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, 'gifs')
OUTPUT_DIR = os.path.join(BASE_DIR, 'static', 'img', 'kufi')

# Asegurar que el directorio de salida completo existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Procesar todos los GIFs en la carpeta gifs
for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith('.gif'):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)

        with Image.open(input_path) as img:
            frames = []

            for frame in ImageSequence.Iterator(img):
                frame = frame.convert('RGBA')
                frame = frame.resize((512, 512), Image.Resampling.LANCZOS)
                frames.append(frame)

            frames[0].save(
                output_path,
                save_all=True,
                append_images=frames[1:],
                loop=img.info.get('loop', 0),
                duration=img.info.get('duration', 100),
                disposal=2,
                transparency=img.info.get('transparency', 0) if 'transparency' in img.info else 0,
                optimize=False
            )

print(f"✅ GIFs guardados correctamente en {OUTPUT_DIR}")
