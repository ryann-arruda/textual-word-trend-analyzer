from nltk.probability import ConditionalFreqDist
import analyzer_utility as anut
import matplotlib.pyplot as plt
from pathlib import *
import os

file_name = input("Insira o nome do arquivo a ser analisado: ")

text = ""

if Path(file_name).suffix == ".txt" and os.path.exists(file_name):

	with open(file_name, 'r', encoding = "utf-8") as f:
		
		for line in f:
			text += line

	cfdist = ConditionalFreqDist()
	anut.count_occurrences(cfdist, text)

	occurrences = anut.join_occurrences(cfdist)

	anut.process_data(occurrences)

	fig, ax = plt.subplots()

	ax.bar(occurrences.keys(), occurrences.values())
	plt.show()
	
else:
	print("File not found or incorrect extension!")