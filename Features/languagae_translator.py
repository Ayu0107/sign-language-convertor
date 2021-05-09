# 'pip install googletrans==3.1.0a0' use this instead of 'pip install googletrans' for installing packages
from googletrans import Translator, constants

input_langauge='en'
output_language='ko' #korean

sentance = '안녕하세요'
trans = Translator()

# for language codes visit https://py-googletrans.readthedocs.io/en/latest/ scroll down ot see supported languages
translated = trans.translate(sentance, dest='en', src='ko')
print(translated.text)
