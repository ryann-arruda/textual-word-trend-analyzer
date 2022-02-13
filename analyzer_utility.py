from nltk.tokenize import word_tokenize
from statistics import mean, pvariance
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

def process_data(occurrences):
	aux = list(occurrences.values())

	data_average = mean(aux)
	data_variance = pvariance(aux)

	for key in list(occurrences):

		if occurrences[key] <= data_average:
			del occurrences[key]


	for key in list(occurrences):

		if occurrences[key] - data_variance < 1:
			del occurrences[key]