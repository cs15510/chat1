
def read_file(filename):
	lines = []
	with open (filename, "r", encoding = "utf-8-sig") as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == "Allen":
			person = "Allen"
			continue
		elif line == "Tom":
			person = "Tom"
			continue

		if person:
			new.append(person + ": " + line)
	return new

def write(filename, lines):
	with open(filename, "w", encoding = "utf-8") as f:
		for line in lines:
			f.write(line + "\n")

def main(input_filename, output_filename):
	lines = read_file(input_filename)
	lines = convert(lines)
	write(output_filename,lines)

main("input.txt", "output.txt")
