from googletrans import Translator

translator = Translator()

inputlang = input("Enter the code for source language: ")
outputlang = input("Enter the code for destination language: ")

while (True):
    
    text = input("Enter the text you want to translate: ")
    translation = translator.translate(text, src="{}".format(inputlang), dest="{}".format(outputlang))
    print(translation.text)
    

# Language Codes for some languages 
# see the full list of codes here (iso639-1): https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
'''
Hindi --> hi
English --> en
German --> de
Russian --> ru
Spanish --> es
'''
