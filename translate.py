from google_trans_new import google_translator
# translator = google_translator(url_suffix="hk", timeout=10, proxies={'http':'192.168.0.135:1087','https':'192.168.0.135:1087'})
from multiprocessing.dummy import Pool as ThreadPool
import time
import random

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

    With the adaptation from the google_trans_new documentation, multithreaded
    translation can be achieved with the request function and a pool of threads

    Args:
        source_text: list of lines representing the source text
        dest_language: string representing the destination language
    Returns:
        a list of translated string sentences
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
        source_text ([type]): [description]
        dest_language ([type]): [description]
        number_of_times:
    """
    langs = (dest_language, "en")
    for index in range(number_of_times):
        source_text = translate_to(source_text, langs[index % 2])
    return source_text

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
    check_result = translate_times(source_text, dest_language, 2)
    if source_text == check_result:
        return (source_text, count)
    return find_equilibrium(check_result, dest_language, count + 1)

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