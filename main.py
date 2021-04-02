from google_trans_new import LANGUAGES
import translate

SOURCE = "grabbed_text.txt"

text = translate.file_to_list(SOURCE)
equilibriums = {}
for key in LANGUAGES:
    equilibrium_pair = translate.find_equilibrium(text, key)
    equilibriums[key] = equilibrium_pair[1]
    translated_text = translate.translate_to(equilibrium_pair[0], key)
    with open (f"output_{SOURCE}", "a") as file:
        for line in translated_text:
            file.write(f"{key}: {line}\n")

print(equilibriums)
print(translate.find_max_equilibrium(equilibriums))