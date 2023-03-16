from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator

app = FastAPI()

class RequestModel(BaseModel):
    text_TBT: str
    language: str

class ResponseModel(BaseModel):
    translation: str

def translate_text(text, target_language):
    print("This is the text feeded for translation: ", text, type(text))
    print("This is the target_language feeded for translation: ", target_language, type(target_language))
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
        print("THIS IS WHERE WE ARE PRINITING TRANSLATION: ", translation.text)

    except Exception as e:
        print(f"Error: {e}")
        return "translation cannot be performed"

    print("HIHIHIHIHIHIHI_1: ", translation.text)
    return translation.text

def get_language_code(language):
    indic_language_codes = {"english": "en", "hindi": "hi", "gujarati": "gu", "arabic": "ar", "assamese": "as",
                            "bengali": "bn", "kannada": "kn", "malayalam": "ml", "marathi": "mr", "nepali": "ne",
                            "punjabi": "pa", "tamil": "ta", "telugu": "te", "thai": "th", "urdu": "ur",
                            "vietnamese": "vi"}

    foreign_language_codes = {"french": "fr", "german": "de", "italian": "it", "japanese": "ja", "korean": "ko",
                              "portuguese": "pt", "russian": "ru", "spanish": "es", "turkish": "tr"}

    try:
        return indic_language_codes[language]
    except KeyError:
        try:
            return foreign_language_codes[language]
        except KeyError:
            print(f"Error: Language {language} not supported.")
            return None

@app.post("/translate")
def translate(request: RequestModel) -> ResponseModel:
    input_text = request.text_TBT
    target_language = request.language.lower()

    language_code = get_language_code(target_language)
    print(language_code)

    if not language_code:
        return {"translation": "Error: Language not supported."}

    translation = translate_text(input_text, language_code)
    print("HIHIHIHIHIHIHI_2: ", translation)
    
    if not translation:
        return {"translation": "Error: Translation failed."}

    return {"translation": translation}
