from PIL import Image, ImageEnhance, ImageFilter
from pathlib import Path

src = Image.open("Lena.pgm").convert("L")
out_dir = Path("dataset")
out_dir.mkdir(exist_ok=True)

for i in range(20):
    # Create a large input image from the provided sample.
    img = src.resize((1024, 1024))

    # Vary each image to create distinct test inputs.
    if i % 4 == 1:
        img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    elif i % 4 == 2:
        img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    elif i % 4 == 3:
        img = img.rotate(90)

    img = ImageEnhance.Brightness(img).enhance(0.7 + (i % 7) * 0.1)
    img.save(out_dir / f"image_{i+1:02d}.pgm")

print(f"Created {len(list(out_dir.glob('*.pgm')))} images in {out_dir}/")
