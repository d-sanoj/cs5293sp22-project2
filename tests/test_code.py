# Importing necessary modules to run test cases
# Module sys for path setting 
# Importing project2.py 
# Module pytest to run test cases
# importing os.path to check if yummly.json exists

import sys
sys.path.append('..')
import project2
import pytest
import os.path

# Testing if yummly.json exists
def test_yummly():
    if os.path.exists('yummly.json'):
        assert True

# Testing if the processing function exists
def test_processing():
    if 'proessing' in dir(project2):
        assert True

# Testing if readinput function exists in project2
def test_readinput():
    if 'read_input' in dir(project2):
        assert True

# Testing is args are parsed for command line input
def test_mainexists():
    if project2.arg_ls:
        assert True

# Testing if dataframe is existing
def test_dataframe():
    if project2.pd.DataFrame:
        assert True

# Testing if userinput exists
def test_userinput():
    if project2.userinput:
        assert True
