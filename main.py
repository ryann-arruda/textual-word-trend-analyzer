file_name = input("Insira o nome do arquivo a ser analisado: ")

text = ""

with open(file_name, 'r', encoding = "utf-8") as f:
	
	for line in f:
		text += line

print(text)