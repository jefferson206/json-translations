import os
from src.translator import TranslatorService
from src.config import INPUT_FOLDER, OUTPUT_FOLDER, LANGUAGES_CODES, FILE_NAME, TRANSLATED_NAME, USE_TRANSLATED_NAME

def main():
    input_file = os.path.join(INPUT_FOLDER, f'{FILE_NAME}.json')

    translator_service = TranslatorService()

    for lang in LANGUAGES_CODES:
        output_file = os.path.join(OUTPUT_FOLDER, f'{TRANSLATED_NAME}-{lang}.json' if USE_TRANSLATED_NAME else f'{lang}.json')
        translator_service.translate_file(input_file, lang, output_file)

if __name__ == "__main__":
    main()
