import sys

import requests
from bs4 import BeautifulSoup

SESSION = requests.Session()


def examples(tlang, word):
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.com'  # This is another valid field
    }

    lang_pair = langs[slang].lower() + '-' + langs[tlang].lower()

    url = 'https://context.reverso.net/translation/' + lang_pair + '/' + word

    try:
        r = SESSION.get(url, headers=headers)
    except:
        print('Something wrong with your internet connection')

    s = BeautifulSoup(r.content, 'lxml')

    word_divs = s.find(id='translations-content')

    try:
        words = [w for d in word_divs.find_all() if (w := d.text.strip())]
    except AttributeError:
        print('Sorry, unable to find ' + word)
        sys.exit()

    sents_divs = s.find(id='examples-content')
    sents = [sent.text.strip() for sent in sents_divs.find_all(attrs={"class": 'text'})]
    return words, sents


def display_examples(tlang, words, sents, n=5, file=None):
    lines = ['\n']
    lines.append(langs[tlang] + ' Translations:\n')
    for w in words[:n]:
        lines.append(w + '\n')
    lines.append('\n')

    def remove_marks(sent):
        return sent.replace(',', '').replace('"', '')

    lines.append(langs[tlang] + ' Examples:\n')
    for oe, te in zip(sents[:n], sents[1:n + 1]):
        lines.append(remove_marks(oe) + '\n')
        lines.append(remove_marks(te) + '\n')
        lines.append('\n')

    for l in lines:
        print(l.strip())

    f.writelines(lines)


langs = dict(zip(list(range(1, 14)),
                 ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish',
                  'Portuguese', 'Romanian', 'Russian', 'Turkish']))


def get_lang_number(str_lang):
    return list(langs.keys())[list(langs.values()).index(str_lang.title())]


if __name__ == '__main__':
    try:
        slang = get_lang_number(sys.argv[1])
    except ValueError:
        print("Sorry, the program doesn't support " + sys.argv[1])
        sys.exit()
    try:
        tlang = 0 if sys.argv[2] == 'all' else get_lang_number(sys.argv[2])
    except ValueError:
        print("Sorry, the program doesn't support " + sys.argv[2])
        sys.exit()
    word = sys.argv[3]
else:
    print("Hello, you're welcome to the translator. Translator supports: ")
    for i, lang in langs.items():
        print(f'{i}. {lang}')

    slang = int(input('Type the number of your language: '))
    tlang = int(input("Type the number of a language you want to translate to or '0' to translate to all languages: "))
    word = input('Type the word you want to translate: ')

f = open(word + '.txt', 'wt', encoding='utf-8')

if tlang == 0:
    for t in langs.keys():
        if t == slang:
            continue
        words, sents = examples(t, word)
        display_examples(t, words, sents, 1, file=f)
else:
    words, sents = examples(tlang, word)
    display_examples(tlang, words, sents, 5, file=f)

f.close()
