import json
from googletrans import Translator
from deep_translator import GoogleTranslator

class TranslatorService:
    def __init__(self, src_lang='en'):
        self.src_lang = src_lang
        self.translator = Translator()

    def translate_dict(self, d, target_lang):
        translated_dict = {}
        for key, value in d.items():
            if isinstance(value, dict):
                translated_dict[key] = self.translate_dict(value, target_lang)
            elif isinstance(value, str):
                if not value.strip():
                    translated_dict[key] = value
                else:
                    try:
                        translated_value = GoogleTranslator(source='en', target=target_lang).translate(value)
                        translated_dict[key] = translated_value
                    except Exception as e:
                        print(f"Error translating '{value}': {e}")
                        translated_dict[key] = value
            else:
                translated_dict[key] = value
        return translated_dict

    def translate_file(self, input_file, target_lang, output_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        translated_data = self.translate_dict(data, target_lang)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(translated_data, file, ensure_ascii=False, indent=4)

        print(f"Translated file saved as {output_file}")