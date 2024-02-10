from bs4 import BeautifulSoup

inputFile = open("/path/to/file.html", "r")
outputFile = open('/path/to/output.csv', 'w')
content = inputFile.read()
soup = BeautifulSoup(content, 'html.parser')

# array to hold list of ETP entries
outputFileEntries = []

for entry in soup.find_all("div", class_="document"):
	# string to hold a tentative CSV file single-line for an entry
	outputFileLine = ''
	for tag in entry:
		if tag.name is not None:
			formattedTagText = '\t'.join([line.strip() for line in tag.text.split('\n')])
			outputFileLine = outputFileLine + "\"" + formattedTagText + "\"" +  ', '
	outputFileEntries.append(outputFileLine)

for line in outputFileEntries:
	outputFile.write(line + "\n") 

inputFile.close()
outputFile.close()