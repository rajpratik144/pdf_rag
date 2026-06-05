from pathlib import Path
import fitz
from core.logger import get_logger
logger = get_logger(__name__)

class PageRenderer:
    @staticmethod
    def render_page(pdf_path,page_number,output_dir="temp"):

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True,exist_ok=True)
        document = fitz.open(pdf_path)
        page = document.load_page(page_number - 1)
        pixmap = page.get_pixmap(matrix=fitz.Matrix(2,2))
        image_path = (output_dir/f"page_{page_number}.png")
        pixmap.save(str(image_path))
        document.close()
        logger.info(f"Rendered page {page_number}")
        
        return str(image_path)