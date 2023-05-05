# Language Translation App 

### Overview : 
The Language Translation App is a simple yet powerful application that allows users to translate English text to Hindi or Marathi with the click of a button. Built with Streamlit and the Transformers library, this app leverages the power of state-of-the-art pre-trained language models to provide accurate and efficient translation services. With just a few lines of code, users can easily deploy the app and start translating text to the language of their choice. Whether you are a language enthusiast, a researcher, or a business professional, this app provides an intuitive and accessible platform to bridge the gap between different languages and cultures.

### Dataset : 

The Hindi translation model was trained on the KD4 dataset(https://opus.nlpl.eu/KDE4.php) , which contains over 97227 sentence pairs in English and Hindi. This dataset was created by crawling the web and selecting high-quality, parallel sentence pairs using a combination of heuristics and manual filtering. The dataset covers a wide range of topics and domains, making it well-suited for training a general-purpose translation model.

The Marathi translation model, on the other hand, was trained on the Tab-delimited Bilingual Sentence Pairs dataset (http://www.manythings.org/anki/), which contains around 56360 sentence pairs in English and Marathi. This dataset was created specifically for machine translation research and covers a wide range of domains, including news articles, books, and movie subtitles. The dataset was carefully curated to ensure high-quality sentence pairs and to maintain a balanced distribution of sentence lengths and difficulty levels.

By using high-quality and diverse datasets like these for training, the Hindi and Marathi models used in the Language Translation App are capable of providing accurate and reliable translations for a variety of text inputs.


### Tech Stack : 
- Python 
- Tensorflow 
- Huggingface Transformers Library 
- Streamlit 



## How to Use this App for Language Translation : 

- Clone this repository : `$ git clone https://github.com/Vinayakmane47/language-translation-transformer.git`
- Creat a virtual environment : `$ conda create -n env python=3.7 -y`
- Install requirements    : `$ pip install -r requirements.txt` 
- Run this App : `$ python app.py` 


## Results : 
#### BLEU Scores : 

| Language | BLEU-Score             |
| --------------- | --------------- |
| English-Hindi   | 36.63           |
| English-Marathi  | 31.66          |



#### English to Hindi : 
![image](https://user-images.githubusercontent.com/103372852/236200498-2a6021f0-7ab6-4401-bb3a-06c22469df52.png)

### Engish to Marathi 
![image](https://user-images.githubusercontent.com/103372852/236200603-5441d059-cca5-4255-9429-7648a0546dc6.png)


### Application URL : 
[language-translation-App](https://huggingface.co/spaces/VinayakMane47/Language-Translation)



