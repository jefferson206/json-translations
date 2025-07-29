import json
from googletrans import Translator
from deep_translator import GoogleTranslator
from .config import ORIGIN_LANGUAGE

class TranslatorService:
    def __init__(self, src_lang=f'{ORIGIN_LANGUAGE}'):
        self.src_lang = src_lang
        self.translator = Translator()

    def translate_dict(self, d, target_lang):
        translated = {}

        for key, value in d.items():
            if isinstance(value, dict):
                translated[key] = self.translate_dict(value, target_lang)
            elif isinstance(value, list):
                translated_list = []
                for item in value:
                    if isinstance(item, str):
                        if not item.strip():
                            translated_list.append(item)
                        else:
                            try:
                                translated_item = GoogleTranslator(source=self.src_lang, target=target_lang).translate(item)
                                translated_list.append(translated_item)
                            except Exception as e:
                                print(f"Error translating '{item}': {e}")
                                translated_list.append(item)
                    elif isinstance(item, dict):
                        translated_list.append(self.translate_dict(item, target_lang))
                    else:
                        translated_list.append(item)
                translated[key] = translated_list
            elif isinstance(value, str):
                if not value.strip():
                    translated[key] = value
                else:
                    try:
                        translated_value = GoogleTranslator(source=self.src_lang, target=target_lang).translate(value)
                        translated[key] = translated_value
                    except Exception as e:
                        print(f"Error translating '{value}': {e}")
                        translated[key] = value
            else:
                translated[key] = value

        return translated


    def translate_file(self, input_file, target_lang, output_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        translated_data = self.translate_dict(data, target_lang)
        folder_name = output_file.split("\\")[0]
        file_name = output_file.split("\\")[1]
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(translated_data, file, ensure_ascii=False, indent=4)

        print(f"Translated file saved in {folder_name} folder as {file_name}")
