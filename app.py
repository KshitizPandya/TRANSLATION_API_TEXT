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
#     indic_language_codes = {"english": "en", "hindi": "hi", "gujarati": "gu", "arabic": "ar", "assamese": "as",
#                             "bengali": "bn", "kannada": "kn", "malayalam": "ml", "marathi": "mr", "nepali": "ne",
#                             "punjabi": "pa", "tamil": "ta", "telugu": "te", "thai": "th", "urdu": "ur",
#                             "vietnamese": "vi"}
    language_codes = {"Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar", "Armenian": "hy", "Assamese": "as",
                      "Aymara": "ay", "Azerbaijani": "az", "Bambara": "bm", "Basque": "eu", "Belarusian": "be", "Bengali": "bn",
                      "Bhojpuri": "bh", "Bosnian": "bs", "Bulgarian": "bg", "Catalan": "ca", "Cebuano": "ceb", "Chichewa": "ny",
                      "Chinese (Simplified)": "zh-CN", "Chinese (Traditional)": "zh-TW", "Corsican": "co", "Croatian": "hr",
                      "Czech": "cs", "Danish": "da", "Dhivehi": "dv", "Dogri": "doi", "Dutch": "nl", "English": "en", "Esperanto": "eo",
                      "Estonian": "et", "Ewe": "ee", "Filipino": "fil", "Finnish": "fi", "French": "fr", "Frisian": "fy", "Galician": "gl",
                      "Georgian": "ka", "German": "de", "Greek": "el", "Guarani": "gn", "Gujarati": "gu", "Haitian Creole": "ht", "Hausa": "ha",
                      "Hawaiian": "haw", "Hebrew": "he", "Hindi": "hi", "Hmong": "hmn", "Hungarian": "hu", "Icelandic": "is", "Igbo": "ig",
                      "Ilocano": "ilo", "Indonesian": "id", "Irish": "ga", "Italian": "it", "Japanese": "ja", "Javanese": "jv", "Kannada": "kn",
                      "Kazakh": "kk", "Khmer": "km", "Kinyarwanda": "rw", "Konkani": "kok", "Korean": "ko", "Krio": "kri", "Kurdish (Kurmanji)": "ku",
                      "Kurdish (Sorani)": "ckb", "Kyrgyz": "ky", "Lao": "lo", "Latin": "la", "Latvian": "lv", "Lingala": "ln", "Lithuanian": "lt",
                      "Luganda": "lg", "Luxembourgish": "lb", "Macedonian": "mk", "Maithili": "mai", "Malagasy": "mg", "Malay": "ms", "Malayalam": "ml",
                      "Maltese": "mt", "Maori": "mi", "Marathi": "mr", "Meiteilon (Manipuri)": "mni", "Mizo": "lus", "Mongolian": "mn", "Myanmar (Burmese)": "my",
                      "Nepali": "ne", "Norwegian": "no", "Odia (Oriya)": "or", "Oromo": "om", "Pashto": "ps", "Persian": "fa", "Polish": "pl", "Portuguese": "pt", 
                      "Punjabi": "pa", "Quechua": "qu", "Romanian": "ro", "Russian": "ru", "Samoan": "sm", "Sanskrit": "sa", "Scots Gaelic": "gd", "Sepedi": "nso", 
                      "Serbian": "sr", "Sesotho": "st", "Shona": "sn", "Sindhi": "sd", "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so", 
                      "Spanish": "es", "Sundanese": "su", "Swahili": "sw", "Swedish": "sv", "Tajik": "tg", "Tamil": "ta", "Tatar": "tt", "Telugu": "te", 
                      "Thai": "th", "Tigrinya": "ti", "Tsonga": "ts", "Turkish": "tr", "Turkmen": "tk", "Twi": "tw", "Ukrainian": "uk", "Urdu": "ur", "Uyghur": "ug",
                      "Uzbek": "uz", "Vietnamese": "vi", "Welsh": "cy", "Xhosa": "xh", "Yiddish": "yi", "Yoruba": "yo", "Zulu": "zu"}

#     try:
#         return indic_language_codes[language]
#     except KeyError:
    try:
        return language_codes[language]
    except KeyError:
        print(f"Error: Language {language} not supported.")
        return None

@app.post("/translate")
def translate(request: RequestModel) -> ResponseModel:
    input_text = request.text_TBT
    target_language = request.language

    language_code = get_language_code(target_language)
    print(language_code)

    if not language_code:
        return {"translation": "Error: Language not supported."}

    translation = translate_text(input_text, language_code)
    print("HIHIHIHIHIHIHI_2: ", translation)
    
    if not translation:
        return {"translation": "Error: Translation failed."}

    return {"translation": translation}
