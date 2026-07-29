from PIL import Image

from transformers import pipeline


class Captioner:

    def __init__(self):

        self.pipeline = pipeline(
        "image-text-to-text",
        model="Salesforce/blip-image-captioning-base"
)
        )

    def caption(self, path: str):

        image = Image.open(path)

        result = self.pipeline(image)

        return result[0]["generated_text"]


captioner = Captioner()