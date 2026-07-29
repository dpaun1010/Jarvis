from vision.ocr import ocr
from vision.caption import captioner
from vision.detector import detector


class VisionManager:

    def caption(self, path):

        return captioner.caption(path)

    def read(self, path):

        return ocr.read(path)

    def detect(self, path):

        return detector.detect(path)


manager = VisionManager()