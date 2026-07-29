from pathlib import Path
from PIL import Image


class ImageLoader:

    def load(self, path: str):

        image = Image.open(path)

        return image.convert("RGB")


loader = ImageLoader()