from nltk.probability import ConditionalFreqDist
import analyzer_utility as anut

file_name = input("Insira o nome do arquivo a ser analisado: ")

text = ""

with open(file_name, 'r', encoding = "utf-8") as f:
	
	for line in f:
		text += line

	cfdist = ConditionalFreqDist()
	anut.count_occurrences(cfdist, text)

	occurrences = anut.join_occurrences(cfdist)