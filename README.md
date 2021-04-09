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

## Implementation

