from googletrans import Translator
from papago import Papago
import asyncio
import requests
import time
from config import r_config, TRANSLATION_CONFIG

def multi_translate(text):
    service =  r_config(TRANSLATION_CONFIG, 'translation_service')
    if service == 'Papago':
        return asyncio.run(papago_translate(text))
    elif service == 'DeepL Translate':
        return deepl_translate(text)
    elif service == 'Google Translate':
        return google_translate(text)
    else:
        return 'Error: No Translation Service Available'

async def papago_translate(text):
    papago = Papago(r_config(TRANSLATION_CONFIG, "source_lang") or 'ja',  r_config(TRANSLATION_CONFIG, "target_lang") or "en")
    res = await papago.translate(text, honorific=True)
    if res['translatedText']:
        return res['translatedText']
    else:
        return 'Failed to Translate'

def deepl_translate(text):
    api_key =  r_config(TRANSLATION_CONFIG, 'deepl_api_key')
    text = text[:140] if len(text) > 140 else text

    import deepl
    translator = deepl.Translator(api_key)
    result = translator.translate_text(
        text,
        source_lang=r_config(TRANSLATION_CONFIG, "source_lang").upper() or "JA",
        target_lang=r_config(TRANSLATION_CONFIG, "target_lang").upper() or "EN-GB",
        split_sentences='nonewlines')
    
    # response = requests.post(
    # "https://www2.deepl.com/jsonrpc",
    # json = {
    #     "jsonrpc":"2.0",
    #     "method": "LMT_handle_jobs",
    #     "params": {
    #         "jobs":[{
    #             "kind":"default",
    #             "raw_en_sentence": text,
    #             "raw_en_context_before":[],
    #             "raw_en_context_after":[],
    #             "preferred_num_beams":4,
    #             "quality":"fast"
    #         }],
    #         "lang":{
    #             "user_preferred_langs":["EN"],
    #             "source_lang_user_selected": r_config(TRANSLATION_CONFIG, "source_lang").upper() or "JA",
    #             "target_lang": r_config(TRANSLATION_CONFIG, "target_lang").upper() or "EN"
    #         },
    #         "priority":-1,
    #         "commonJobParams":{},
    #         "timestamp": int(round(time.time() * 1000))
    #     },
    #     "id": 40890008
    # })
    # output = response.json()
    # if output is not None:
    #     if 'result' in output:
    #         return output['result']['translations'][0]['beams'][0]["postprocessed_sentence"]
    #     if 'error' in output:
    #         return 'Error: ' + output['error']['message']

    if result.text is not None:
        return result.text

    return 'Failed to Translate'

def google_translate(text):
    translator = Translator()
    result = translator.translate(text)
    return result.text