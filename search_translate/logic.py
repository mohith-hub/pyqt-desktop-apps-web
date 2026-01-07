from deep_translator import GoogleTranslator

def perform_search(query):
    return f"Searching for: {query}"

def translate_ui_labels(lang):
    translator = GoogleTranslator(source="en", target=lang)
    return {
        "title": translator.translate("Search Engine"),
        "search": translator.translate("Search"),
        "translate": translator.translate("Translate UI"),
        "placeholder": translator.translate("Enter search query")
    }
