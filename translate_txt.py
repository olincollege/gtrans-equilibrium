from google_trans_new import google_translator
translator = google_translator(url_suffix="cn", timeout=5)

def translate_to(source_text, dest_language):
    """
    Translate source text into destination language

    Args:
        source_text: list of lines representing the source text
        dest_language: string representing the destination language
    """
    translated = []
    for line in source_text:
        translated.append(translator.translate(
            line, lang_tgt=dest_language))
    return translated
text = []
with open("grabbed_text.txt") as f:
    for line in f:
        print(line)
        text.append(line.strip())

with open ("grabbed_text.txt", "a") as f:
    translated = translate_to(text, "zh-CN")
    for line in translated:
        f.write(f"\n{line}")