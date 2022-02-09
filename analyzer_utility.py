from nltk.tokenize import word_tokenize
import re

def count_occurrences(cfdist, text):

	for word in word_tokenize(text):

		if re.match('[a-zA-Z\u00C0-\u00FF]+\-[a-zA-Z\u00C0-\u00FF]+|[a-zA-Z\u00C0-\u00FF]+', word) != None:
			condition = len(word)
			cfdist[condition][word.lower()] += 1