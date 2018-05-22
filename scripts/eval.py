import language_check
import random

def eval_txt(file_path, verbose=False):
	with open('tn_output_raw.txt', 'r') as f: 
		data_raw = f.read().replace('\n', '')
	tool = language_check.LanguageTool('en-US')
	matches = tool.check(data_raw)
	if verbose:
		print(matches[random.randint(0, len(matches)-1)])
	return len(matches)

def eval_str(output, verbose=False):
	tool = language_check.LanguageTool('en-US')
	matches = tool.check(output)
	if verbose:
		print(matches[random.randint(0, len(matches)-1)])
	return len(matches)