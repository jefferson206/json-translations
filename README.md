# Translation Project

## Description
This project translates an English JSON file into multiple languages using the Google Translate API.

## Folder Structure
- `toTranslate/`: Contains the source JSON file (`en.json`).
- `translated/`: Contains the translated JSON files.
- `src/`: Contains the Python scripts for translation logic.
- `main.py`: Main script that triggers the translation process.

## Setup
1. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt

2. In the src/config.py there is a variable called LANGUAGES, it's an array of languages like the example: ['pt', 'es', 'it', 'fr'].
It will translate for the languages you pass in this array.

## Run App
3. To run this app:
   ```bash
   python main.py