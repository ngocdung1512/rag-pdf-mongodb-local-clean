import pytesseract
from pdf2image import convert_from_path
import os

# Load đường dẫn từ biến môi trường hoặc khai báo trực tiếp
TESSERACT_PATH = os.getenv("TESSERACT_PATH") or r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = os.getenv("POPPLER_PATH") or r"C:\Program Files\Release-24.08.0-0\poppler-24.08.0\Library\bin"
PDF_FILE = "PDFs\sach-tieng-viet-lop-2-KNTT.pdf"  # Đổi tên file PDF tùy bạn
OUTPUT_TEXT_FILE = "extracted_text.txt"  # Tên file text xuất ra

# Thiết lập đường dẫn tesseract
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def main():
    print(f"Đang trích xuất ảnh từ file: {PDF_FILE}")
    try:
        images = convert_from_path(PDF_FILE, poppler_path=POPPLER_PATH)
        print(f"Tổng số trang ảnh tạo ra: {len(images)}")

        full_text = ""

        for i, image in enumerate(images):
            print(f"Đang xử lý trang {i+1}...")
            text = pytesseract.image_to_string(image, lang='vie')
            full_text += f"\n--- Trang {i+1} ---\n{text.strip()}\n"

        # Lưu nội dung vào file .txt
        with open(OUTPUT_TEXT_FILE, "w", encoding="utf-8") as f:
            f.write(full_text)

        print(f"\n✅ Đã lưu nội dung OCR vào file: {OUTPUT_TEXT_FILE}")

    except Exception as e:
        print(f"❌ Lỗi trong quá trình OCR: {e}")

if __name__ == "__main__":
    main()
