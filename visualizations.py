"""
Creating three visualizations to present the translational equilibrium findings
"""
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from google_trans_new import LANGUAGES
import translate

SOURCE = "grabbed_text.txt"
text = translate.file_to_list(SOURCE)
EQUILIBRIUMS = {}
for index in range(64):
    lang = list(LANGUAGES.keys())[index]
    equilibrium_pair = translate.find_equilibrium(text, lang)
    EQUILIBRIUMS[lang] = equilibrium_pair[1]
    equilibrium_text = translate.translate_to(equilibrium_pair[0], lang)
    with open(f"output_{SOURCE}", "a") as file:
        for line in equilibrium_text:
            file.write(f"{lang}: {line}\n")
print(EQUILIBRIUMS)
print(translate.find_max_equilibrium(EQUILIBRIUMS))

# Scatterplot using matplotlib
x = np.array(list(EQUILIBRIUMS.keys()))
y = np.array(list(EQUILIBRIUMS.values()))
plt.rcParams['figure.figsize'] = [20, 5]
plt.rcParams["figure.dpi"] = 1080
plt.scatter(x, y)
plt.title('Steps to a Translational Equilibrium', fontsize=16)
plt.xlabel('Language', fontsize=12)
plt.ylabel('Steps to Equilibrium', fontsize=12)
plt.show()

# Wordcloud using matplotlib and wordcloud
RESULT = "output_grabbed_text.txt"
text = translate.file_to_list(RESULT)
translated = translate.translate_to(text, "en")
word_cloud = WordCloud(repeat=True, max_words=100).generate(
    "".join(translated))
plt.rcParams['figure.figsize'] = [20, 5]
plt.imshow(word_cloud)
plt.axis("off")
plt.show()

# Table using matplotlib and pandas dataframe
temp = dict(EQUILIBRIUMS)
max_equilibriums = {}
translated = []
for _ in range(3):
    current_max = translate.find_max_equilibrium(temp)
    lang = current_max[0]
    translated.append(translate.translate_to(
        translate.find_equilibrium(text, lang)[0], "en"))
    max_equilibriums[current_max[0]] = current_max[1]
    del temp[current_max[0]]
data = [list(max_equilibriums.keys()),
        [list(max_equilibriums.values())],
        ["".join(eng_text) for eng_text in translated]]
df = DataFrame(data).transpose()
df.columns = ["Language",
              "Steps to Translational Equilibrium", "Equilibrium Text"]
print(df)
plt.show()
