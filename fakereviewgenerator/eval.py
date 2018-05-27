""" This module performs grammer check on a text file content
or a string. This check allows an objective evaluation of
sampled text from the model
Functions:
eval_txt:This function reads a text file and performs
    grammer check on the text
eval_str: This function take string as a parameter and performs
    grammer check on it
"""
import random
import os
import language_check

def eval_txt(file_path, verbose=False):
    """ This function reads a text file and performs
    grammer check on the text
    Parameters:
        file_path: Complete path to the text file
        verbose: Verbose output (False)
    Return Value:
        Number of grammer errors, error details
    Exceptions:
        OSError: Raised if the text file is not found
    """
    if not os.path.exists(file_path):
        raise OSError("File Not Found")
    else:
        with open(file_path, 'r') as f:
            data_raw = f.read().replace('\n', '')
        tool = language_check.LanguageTool('en-US')
        matches = tool.check(data_raw)
        if verbose and len(matches) > 0:
            print(matches[random.randint(0, len(matches)-1)])
        return len(matches), matches

def eval_str(output, verbose=False):
    """ This function take string as a parameter and performs
    grammer check on it
    Parameters:
        output: String to run grammer check on
        verbose: Verbose output (False)
    Return Value:
        Number of grammer errors, error details
    """
    if len(output) == 0:
        raise ValueError("File is empty")
    else:
        tool = language_check.LanguageTool('en-US')
        matches = tool.check(output)
        if verbose and len(matches) > 0:
            print(random.choice(matches))
        return len(matches), matches
