FILEPATH = "file"

def get_todos(filepath=FILEPATH):
	"""
	Read a Text file
	:param filepath: default files/todo.txt
	:return:  an array with all the iems in the file
	"""


	with open(filepath, 'r') as file_local:
		todos_local = file_local.readlines()
	return todos_local
#print(help(get_todos))

def write_todos(todos_arg, filepath=FILEPATH):
	"""
	Write element in into a file
	:param todos_arg:
	:param filepath: default files/todo.txt
	:return: Novalue
	"""
	with open(filepath,'w') as file:
		file.writelines(todos_arg)
print (__name__)
if __name__ == "__main__":
	print("Hello from functions")
	print(get_todos())
