from google_trans_new import google_translator
translator = google_translator(url_suffix="cn", timeout=5)

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

def translate_file(source_file, dest_language):
    """
    Translate source file into destination language

    Args:
        source_file: string representing the path of the file
        dest_language: string representing the destination language
    """
    text = []
    with open(source_file) as f:
        for line in f:
            print(line)
            text.append(line.strip())

    with open (f"output_{source_file}", "w") as f:
        translated = translate_to(text, "zh-CN")
        for line in translated:
            print(line)
            f.write(f"{line}\n")
