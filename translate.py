from google_trans_new import google_translator
translator = google_translator(url_suffix="cn", timeout=5)

def file_to_list(source_file):
    """
    Convert a text file into a list of strings.

    Args:
        source_file: string representing the path of the file
    Returns:
        a list of sentence strings from the source file
    """
    text = []
    with open(source_file) as file:
        for line in file:
            text.append(line.strip())
    return text

def translate_to(source_text, dest_language):
    """
    Translate source text into destination language

    Args:
        source_text: list of lines representing the source text
        dest_language: string representing the destination language
    Returns:
        a list of translated string sentences
    """
    translated = []
    for line in source_text:
        translated.append(translator.translate(
            line, lang_tgt=dest_language))
    return translated

def translate_times(source_text, dest_language, number_of_times):
    """
    Translate source text into destination language and back to source language
    by a number of times

    Args:
        source_text ([type]): [description]
        dest_language ([type]): [description]
        number_of_times:
    """
    langs = (dest_language, "en")
    for index in range(number_of_times):
        source_text = translate_to(source_text, langs[index % 2])
    return source_text

def translate_file(source_file, dest_language):
    """
    Translate source file into destination language

    Args:
        source_file: string representing the path of the file
        dest_language: string representing the destination language
    """
    text = file_to_list(source_file)
    with open (f"output_{source_file}", "w") as file:
        translated = translate_to(text, dest_language)
        for line in translated:
            file.write(f"{line}\n")

def find_equilibrium(source_text, dest_language, count=0):
    """
    asd

    Args:
        source_text ([type]): [description]
        dest_language ([type]): [description]
        count (int, optional): [description]. Defaults to 0.

    Returns:
        [type]: [description]
    """
    check_result = translate_times(source_text, dest_language, 4)
    if source_text == check_result:
        return (source_text, count + 1)
    return find_equilibrium(check_result, dest_language, count + 1)

def find_max_equilibrium(equilibriums):
    """[summary]

    Args:
        equilibriums: [description]
    """
    maximum = 0
    max_lang = None
    for lang in equilibriums:
        if equilibriums[lang] > maximum:
            maximum = equilibriums[lang]
            max_lang = lang
    return (max_lang, maximum)