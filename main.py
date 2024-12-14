import os
from src.translator import TranslatorService
from src.config import INPUT_FOLDER, OUTPUT_FOLDER, LANGUAGES

def main():
    input_file = os.path.join(INPUT_FOLDER, 'en.json')

    translator_service = TranslatorService()

    for lang in LANGUAGES:
        output_file = os.path.join(OUTPUT_FOLDER, f'{lang}.json')
        translator_service.translate_file(input_file, lang, output_file)

if __name__ == "__main__":
    main()
