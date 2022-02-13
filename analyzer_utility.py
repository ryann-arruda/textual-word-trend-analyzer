from nltk.tokenize import word_tokenize
import re

def count_occurrences(cfdist, text):

	for word in word_tokenize(text):

		if re.match('[a-zA-Z\u00C0-\u00FF]+\-[a-zA-Z\u00C0-\u00FF]+|[a-zA-Z\u00C0-\u00FF]+', word) != None:
			condition = len(word)
			cfdist[condition][word.lower()] += 1

def join_occurrences(cfdist):
	occurrences = {}

	for i in cfdist.keys():
		occurrences.update(dict(cfdist[i]))

	return occurrences