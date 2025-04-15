from nltk.tokenize import sent_tokenize , word_tokenize
#mport nltk
#nltk.download('punkt_tab')

paragraph ='''The sun's dipped below the horizon, painting the sky with hues of amber and rose. 
A soft breeze rustled the leaves, carrying with it the scent of jasmine. 
In that quiet moment, the world seemed to pause, wrapped in golden stillness.'''


sent = sent_tokenize(paragraph)

print(sent)

words_token = word_tokenize(paragraph)
print(words_token)