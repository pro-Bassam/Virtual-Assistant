from translate import Translator


def trans(text):

    translator = Translator(to_lang="French")
    translation = translator.translate(text)
    return(translation)
