from googletrans import Translator

translator = Translator()


def translate(input: str, to: str):
    return translator.translate(input, dest=to).text
