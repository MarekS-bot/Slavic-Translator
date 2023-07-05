from mtranslate import translate
import re 

symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
           u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")

tr = {ord(a):ord(b) for a, b in zip(*symbols)}

slavic_languages = {
    'Polski':       'pl',
    'Czeski':       'cs',
    'Białoruski':   'be',
    'Rosyjski':     'ru',
    'Ukraiński':    'uk',
    'Bośniacki':    'bs',
    'Bułgarski':    'bg',
    'Chorwacki':    'hr',
    'Macedoński':   'mk',
    'Serbski':      'sr',
    'Słoweński':    'sl',
    'Słowacki':     'sk',
}

def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def give_space (func):
    def wrapper_give_space (*args, **kwargs):
        print ()
        func (*args, **kwargs)
        print ()
    return wrapper_give_space


@give_space
def slav_translate(to_translate):
    for k,v in slavic_languages.items():
        translation = translate(to_translate, v)
        if has_cyrillic(translation):
            translation_cyrtolat = translation.translate(tr)
            print(f"{k : >10}{':' : ^10}{translation_cyrtolat} [{translation}]")
        else:
            print(f"{k : >10}{':' : ^10}{translation}")


def main():
    to_translate = input("Do tłumaczenia: ")
    slav_translate(to_translate)


if __name__ == '__main__':
    main()
