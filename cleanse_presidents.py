with open('P00000001-ALL.csv', 'rb') as input_file, open('P00000001-ALL.cleansed.csv', 'wb') as output_file:
	for line in input_file:
		if line.endswith(',\n'):
			output_file.write(line[:-2])
			output_file.write('\n')
		else:
			output_file.write(line)
