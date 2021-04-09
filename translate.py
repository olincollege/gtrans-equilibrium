"""
Translate from file and find equilibriums from text
"""
from google_trans_new import google_translator

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
        source_text: a list of strings representing the source text
        dest_language: a string representing the destination language
    Returns:
        a list of translated string texts
    """
    translated = []
    translator = google_translator(url_suffix="cn", timeout=5)
    for line in source_text:
        translated.append(translator.translate(
            line, dest_language))
    return translated


def translate_times(source_text, dest_language, number_of_times):
    """
    Translate source text into destination language and back to source language
    by a number of times

    Args:
        source_text: a list of strings representing the source text
        dest_language: a string representing the destination language
        number_of_times: an int representing the number of times to be 
            translated
    """
    langs = (dest_language, "en")
    for index in range(number_of_times):
        # Alternating index to pick langs to translate back and forth
        source_text = translate_to(source_text, langs[index % 2])
    return source_text


def find_equilibrium(source_text, dest_language, steps=0):
    """
    Finds the equilibrium of a certain text between English and a chosen
    language

    Args:
        source_text: a list of strings representing the source text
        dest_language: a string representing the destination language
        steps: an int representing the number of steps to reach equilibrium, 
            defaults to 0

    Returns:
        a tuple of the equilibrium text and the amount of steps taken
    """
    # Check if the text is at a translational equilibrium by translating that
    # text back and forth once and comparing that to the original text
    check_result = translate_times(source_text, dest_language, 2)
    if source_text == check_result:
        return (source_text, steps)
    # Recursively call this function again, but with a translated text as
    # source text
    return find_equilibrium(check_result, dest_language, steps + 1)

# def find_equilibrium(source_text, dest_language, potential_equilibriums=[], rounds=0):
#     temp = translate_times(source_text, dest_language, 2)
#     if source_text == temp:
#         return (source_text, rounds + 1)

#     potential_equilibriums.append(temp)
#     if rounds > 0 and \
#     temp == potential_equilibriums[rounds - 1] == \
#         potential_equilibriums[rounds]:
#         return (temp, rounds + 1)

#     if rounds > 2 and temp == potential_equilibriums[rounds - 2] == \
#         potential_equilibriums[rounds - 1] == \
#         potential_equilibriums[rounds - 3]:
#         return (temp, rounds + 1)

#     return find_equilibrium(temp, dest_language, potential_equilibriums, rounds + 1)


def find_max_equilibrium(equilibriums):
    """
    Finds the largest equilibrium step within a predetermined set of languages

    Note that if there are to be more than one largest language, only the first
    occurrance will be taken. See essay for a way to remove that largest
    language and then carry on with finding the next largest language

    Args:
        equilibriums: a dictionary in the format of {"language": no. of steps},
            containing a set of languages and their respective steps

    Returns: 
        a tuple of the language with the largest translational equilibrium and
        its 
    """
    maximum = 0
    max_lang = None
    for lang in equilibriums:
        if equilibriums[lang] > maximum:
            maximum = equilibriums[lang]
            max_lang = lang
    return (max_lang, maximum)
