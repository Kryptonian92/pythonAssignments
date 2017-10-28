'''This code helps find files in the current directory that
contain certain text. For example, if you remember working with
a file that had a variable named "grades" in it, you can run the
code below and enter "grades" in the input to see a list of
notebooks and Python files that contain the word "grades".'''

import os

searchdir='.'
os.chdir(searchdir)

word = ''
while not word.strip():
    word = input('Search word: ')

ext_list = ['ipynb','py']
exclude_dirs = ['.ipynb_checkpoints']
matches = []

for dirpath, dirnames, filenames in os.walk('../'):
    dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
    filtered_filenames = [fname for fname in filenames if fname.split('.')[-1] in ext_list]
    
    for fname in filtered_filenames:
        filepath = dirpath + '/' + fname
        try:
            with open(filepath) as f:
                if word.lower() in f.read().lower():
                    matches.append(filepath)
        except Exception as e:
            print(filepath, e)

print('{} matches found.'.format(len(matches)))
for i, match in enumerate(matches,1):
    print('\t{}. {}'.format(i, match))

