import language_check
import random
import os

def eval_txt(file_path, verbose=False):
	if not os.path.exists(file_path):
		raise OSError("File Not Found")
	else:
		with open(file_path, 'r') as f: 
			data_raw = f.read().replace('\n', '')
		tool = language_check.LanguageTool('en-US')
		matches = tool.check(data_raw)
		if verbose and len(matches) > 0:
			print(matches[random.randint(0, len(matches)-1)])
		return len(matches)

def eval_str(output, verbose=False):
	if len(output) == 0:
		raise ValueError("File is empty")
	else:
		tool = language_check.LanguageTool('en-US')
		matches = tool.check(output)
		if verbose and len(matches) > 0:
			print(random.choice(matches))
		return len(matches)