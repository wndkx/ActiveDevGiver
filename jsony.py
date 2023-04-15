import ast
def load_from_string(string: str):
	if 'null' in string:
		new = string.replace('null', 'None')
		return ast.literal_eval(new)
	else:
		return ast.literal_eval(string)

def load_from_file(filename: str):
	string = open(filename, "r").read()
	if 'null' in string:
		new = string.replace('null', 'None')
		return ast.literal_eval(new)
	else:
		return ast.literal_eval(string)