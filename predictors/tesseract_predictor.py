import pytesseract
from enum import Enum

class TesseractMode(Enum):
    TEXT = "t"
    TEXT_WITH_NUMBERS = "tn"
    TABLE = "table"

class TesseractPredictor:
    def __init__(self, lang="fas", mode=TesseractMode.TEXT_WITH_NUMBERS, tesseract_path="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"):
        self._lang = lang
        self._mode = mode
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
    
    def predict_text_from_image(self, img):
        custom_config = r"--psm 6"
        if self._lang.find("fas") != -1:
            if self._mode == TesseractMode.TEXT_WITH_NUMBERS:
                custom_config = r'-c tessedit_char_whitelist="آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی ۰١۲۳۴۵۶۷۸۹.?!,،:;/"'
            elif self._mode == TesseractMode.TEXT:
                custom_config += r'-c tessedit_char_blacklist="۰١۲۳۴۵۶۷۸۹«»1234567890#"'
            elif self._mode == TesseractMode.TABLE:
                custom_config = r'-c tessedit_char_whitelist="آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی۰١۲۳۴۵۶۷۸۹"'

        return pytesseract.image_to_string(img, lang=self._lang, config=custom_config)