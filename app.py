from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator

app = FastAPI()

class RequestModel(BaseModel):
    text: str
    language: str

class ResponseModel(BaseModel):
    translation: str

def translate_text(text, target_language):
    print("This is the text feeded for translation: ", text, type(text))
    print("This is the target_language feeded for translation: ", target_language, type(target_language))
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)

    except Exception as e:
        print(f"Error: {e}")
        return None

    print("HIHIHIHIHIHIHI_1: ", translation.text)
    return translation.text

def get_language_code(language):
    indic_language_codes = {"english": "en", "hindi": "hi", "gujarati": "gu", "arabic": "ar", "assamese": "as",
                            "bengali": "bn", "kannada": "kn", "malayalam": "ml", "marathi": "mr", "nepali": "ne",
                            "punjabi": "pa", "tamil": "ta", "telugu": "te", "thai": "th", "urdu": "ur",
                            "vietnamese": "vi"}

    foreign_language_codes = {"french": "fr", "german": "de", "italian": "it", "japanese": "ja", "korean": "ko",
                              "portuguese": "pt", "russian": "ru", "spanish": "es", "turkish": "tr"}

    language_code = indic_language_codes.get(language.lower())
    if not language_code:
        language_code = foreign_language_codes.get(language.lower())
    if not language_code:
        print(f"Error: Language {language} not supported.")
    return language_code

@app.post("/translate")
def extract_and_translate(request: RequestModel) -> ResponseModel:
    text = request.text
    target_language = request.language.lower()

    language_code = get_language_code(target_language)

    if not language_code:
        return {"translation": "Error: Language not supported."}

    translation = translate_text(text, language_code)
        print("HIHIHIHIHIHIHI_2: ", translation)
    
    if not translation:
        return {"translation": "Error: Translation failed."}

    return {"translation": translation}
