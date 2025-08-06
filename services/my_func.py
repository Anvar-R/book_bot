def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    
    text = text[start: min(len(text), start + size)]

    lst = [',', '.', '!', '?', ':', ';']
    prev_char = ''
    while len(text) >= 2:
        if all([text[-1] in lst, text[-2] in lst]):
            text = text[:-3]
        elif text[-1] in lst and text[-2].isalpha() and prev_char.isspace():
            return text, len(text)
            break
        else:
            prev_char = text[-1]
            text = text[:-1]
    return text, len(text)


def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    dict = {}
    counter = 1
    start = 0
    size = page_size
    with open(path, 'r', encoding='utf-8') as file:
        buff = file.read()
    while buff:
        res = _get_part_text(buff, start, size)
        dict[counter] = res[0].lstrip()
        #start += res[1]
        buff = buff[res[1]+1:]
        counter += 1
    return dict


