from pdf2image import convert_from_path
import os

PDF_PATH = r"C:\Users\omaar\OneDrive\Desktop\Brown Vintage Cafe Menu.pdf"
OUTPUT_DIR = "menu/static/menu/pdf_images"
POPPLER_PATH = r"C:\chemin\vers\poppler-xx\Library\bin"  # À personnaliser

os.makedirs(OUTPUT_DIR, exist_ok=True)

pages = convert_from_path(PDF_PATH, poppler_path=POPPLER_PATH)
for i, page in enumerate(pages):
    image_path = os.path.join(OUTPUT_DIR, f"menu_page_{i+1}.jpg")
    page.save(image_path, "JPEG")
    print(f"Saved {image_path}") 