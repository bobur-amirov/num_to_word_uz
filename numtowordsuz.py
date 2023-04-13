import re


def num_to_words(num):
    num = int(num)
    units = ["", "bir", "ikki", 'uch', "to‘rt", 'besh', 'olti', 'yetti', 'sakkiz', "to‘qqiz"]
    tens = ['', "o‘n", 'yigirma', "o‘ttiz", 'qirq', 'ellik', 'oltmish', 'yetmish', 'sakson', "to‘qson"]
    thousands = ['', 'ming', 'million', 'milliard', 'trillion', 'kvadrillion', 'kvintilion', 'sekstilion', 'septillion',
                 'oktilion', 'nonillion']
    words = []
    if num == 0:
        words.append('nol')
    else:
        numStr = '%d' % num
        numStrLen = len(numStr)

        groups = (numStrLen + 2) // 3
        numStr = numStr.zfill(groups * 3)
        for i in range(0, groups * 3, 3):
            h, t, u = int(numStr[i]), int(numStr[i + 1]), int(numStr[i + 2])
            g = groups - (i // 3 + 1)
            if h >= 1:
                words.append(units[h])
                words.append('yuz')
            if t > 1:
                words.append(tens[t])
                if u >= 1: words.append(units[u])
            elif t == 1:
                if u >= 1:
                    words.append(tens[1] + " " + units[u])
                else:
                    words.append(tens[t])
            else:
                if u >= 1: words.append(units[u])
            if (g >= 1) and ((h + t + u) > 0): words.append(thousands[g])
    return ' '.join(words)


def to_float(s):
    try:
        if '.' in s:
            return float(s)
        else:
            return int(s)
    except ValueError:
        return s


def text_in(str_text):
    for i in range(len(str_text)):
        if isinstance(to_float(str_text[i]), int):
            if to_float(str_text[i]) > 0:
                str_text[i] = num_to_words(to_float(str_text[i]))
            else:
                str_text[i] = f"minus {num_to_words(abs(to_float(str_text[i])))}"

    return str_text


def private_for_number(text):
    text = re.sub(r'([0-9]+)-([0-9]+)', r'\1 inchi \2 inchi', text)
    text = re.sub(r'([0-9]+)-([a-z]+)', r'\1 inchi \2', text)
    text = re.sub(r'([0-9]+)(\-)', r'\1 inchi \2', text)
    text = re.sub(r'([0-9])\,([0-9])', r'\1.\2 ', text)
    text = re.sub(r'([0-9])\,', r'\1 ', text)
    text = re.sub(r'([0-9])\.([0-9])', r'\1 butun \2 ', text)
    return text


def inchi_(text):
    text = re.sub(r"  inchi", r'inchi', text)
    text = re.sub(r" inchi", r'inchi', text)
    text = re.sub(r"ii", r'i', text)
    return text


def number_to_text(text):
    text = private_for_number(text)
    text = " ".join(text_in(text.split()))
    text = inchi_(text)
    return text

