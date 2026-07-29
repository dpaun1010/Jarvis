import easyocr


class OCR:

    def __init__(self):

        self.reader = easyocr.Reader(
            ["en"],
            gpu=False
        )

    def read(self, image_path: str):

        result = self.reader.readtext(
            image_path,
            detail=0
        )

        return "\n".join(result)


ocr = OCR()
