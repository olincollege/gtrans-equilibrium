# gtrans-equilibrium
Welcome to gtrans-equilibrium! This project examines how many steps it takes for a language to reach it's translational equilibrium with the help of Google Translate.

## Usage

README:
		Remember to open terminal or command prompt and get these packages by entering:

		pip install google_trans_new
		pip install BeautifulSoup
		pip install pandas
        pip install numpy
        pip install matplotlib
        pip install wordcloud

After cloning the repo, open the `translate.py` and at line 33 where the translator is instantiated:

`translator = google_translator(url_suffix="cn", timeout=5)` 

change the url_suffix parameter to "com", and then open `google_translate_equilibrium.ipynb` to run the code cells in order and see the results. 

The `grabbed_text.txt` and `output_grabbed_text.txt` files should change upon executing the above for your analysis.

## How the data was scraped

Since the program sprang off of [TranslationParty](www.translationparty.com), the "hot parties" section is where all of the data comes from. The text is scraped by the `party_scraper.py` file where the  requests and BeautifulSoup packages were used to find all divs of hot parties, their respective href links. The div id was found from inspecting the website elements, and since each "party" has its own caption and href link, it was easy to use the `getText()` on the href links that was found by `find(id="hotparties").find_all("a")`. If you wish to change the data source, change the request `URL` in `party_scraper.py` and go inspect the source's elements that you intend to use.

## How the visualizations were made

First, to view the visuals, [click here](https://github.com/olincollege/gtrans-equilibrium/blob/main/google_translate_equilibrium.ipynb)

The scatterplot can be created with two data lists and using the `matplotlib.pyplot.scatter` function to create a scatter plot. Note that in this implementation the x axis are variable names instead of values. Only the y axis represent values. Then all that's left are just title, xlabel and ylabel, and showing the plot with show(). More parameters can be found at the documentation: https://matplotlib.org/stable/contents.html.

The Wordcloud can be created with a string representing the text and using the `wordcloud.WordCloud().generate(text)`, in the most basic sense. A `matplotlib.pyplot` is needed again to show the image with `imshow()` and turning the axis off with `axis("off")`. A wordcloud can be created as simple as that, but more variations can be achieved as documented here: http://amueller.github.io/word_cloud.

Lastly, the table visual is achieved with three lists of data and converting lists into a `DataFrame` from `pandas`. A `column` need to be set for the table to have overhead titles, and the DataFrame can then be displayed as shown in the essay.