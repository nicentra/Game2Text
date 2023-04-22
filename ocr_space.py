  
import requests
from config import r_config, OCR_CONFIG

OCRSPACE_API_KEY = r_config(OCR_CONFIG, 'ocr_space_api_key') # Contact owner for developer key
OCRSPACE_API_ENGINE = r_config(OCR_CONFIG, 'ocr_space_api_engine')
OCRSPACE_API_SCALE = r_config(OCR_CONFIG, 'ocr_space_api_scale')
OCRSPACE_API_URL_USA = "https://apipro1.ocr.space/parse/image"
OCRSPACE_API_URL_EU = "https://apipro2.ocr.space/parse/image"

def ocr_space_file(filename, overlay=False, api_key=OCRSPACE_API_KEY, language='jpn', url=OCRSPACE_API_URL_EU, engine=OCRSPACE_API_ENGINE, scale=OCRSPACE_API_SCALE):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to ShareX Key.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'eng'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'scale': scale,
               'OCREngine': engine,
               }
    with open(filename, 'rb') as f:
        r = requests.post(url,
                          files={filename: f},
                          data=payload,
                          )
    result = r.json()
    if (result):
        if (result["ParsedResults"]):
            parsedText = result["ParsedResults"][0]['ParsedText']
            return "".join(parsedText.splitlines()) # force output to one line
    return "Error: OCR Failed"
