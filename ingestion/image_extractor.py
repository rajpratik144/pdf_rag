import pdfplumber
class ImageExtractor:

    @staticmethod
    def extract(pdf_path):
        images = []
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages,start=1):
                for image in page.images:
                    images.append({
                        "page":page_num,
                        "width":image.get("width"),
                        "height":image.get("height")})

        return images