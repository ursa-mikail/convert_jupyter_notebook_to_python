""" convert_jupyter_notebook_to_python.py
Extract code cells from a Jupyter notebook (.ipynb) file and writing them into a Python script (.py) file. 
"""
#!pip install nbformat 
import nbformat

def extract_code_from_ipynb(ipynb_file, output_file):
    # Open the Jupyter notebook file in read mode with UTF-8 encoding
    with open(ipynb_file, 'r', encoding='utf-8') as file:
        # Read the notebook content using nbformat
        notebook = nbformat.read(file, as_version=4)
    
    # Extract all code cells from the notebook
    code_cells = [cell['source'] for cell in notebook['cells'] if cell['cell_type'] == 'code']
    
    # Open the output file in write mode with UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as file:
        # Write each code cell to the output file, separated by double newlines
        for i, code in enumerate(code_cells, 1):
            file.write(code)
            file.write('\n\n')


# [Usage]
dir_start = './sample_data/'
# Replace 'notebook.ipynb' and 'output.py' with your file names
# extract_code_from_ipynb(dir_start + 'notebook.ipynb', dir_start + 'output.py')

import requests

# URL of the Jupyter notebook
url = 'https://raw.githubusercontent.com/billbuchanan/ipython-notebooks/refs/heads/master/MachineLearning/LogisticRegression/DigitsClassification.ipynb'

# Download the notebook file
response = requests.get(url)
notebook_file = 'DigitsClassification.ipynb'

# Save the content to a local file
with open(dir_start + notebook_file, 'wb') as file:
    file.write(response.content)

# Extract code cells and save to a Python script
extract_code_from_ipynb(dir_start + notebook_file, dir_start + 'output.py')

