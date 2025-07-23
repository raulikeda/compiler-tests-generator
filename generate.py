import sys
import os
import yaml
from random import randint
import string

# Load language dictionaries from external YAML files
def load_language_dict(language):
    lang_file = f'./data/languages/{language}.yaml'
    with open(lang_file, 'r') as f:
        return yaml.safe_load(f)

def flatten_aliases(aliases):
    # aliases is a list of dicts
    flat = {}
    for d in aliases:
        flat.update(d)
    return flat

version = sys.argv[1]
language = sys.argv[2]

# Load the language dictionary
data = load_language_dict(language)
ext = data['extension']
aliases = flatten_aliases(data['aliases']) if 'aliases' in data else {k: v for k, v in data.items() if k != 'extension'}

with open(f'./data/tests/{version}.yaml','r') as file:
    tests_data = yaml.safe_load(file)

# Filter tests by language
def test_applies(test, language):
    langs = test.get('languages', [])
    return 'All' in langs or any(l.lower() == language.lower() for l in langs)

filtered_tests = [test for test in tests_data if test_applies(test, language)]

# Prepare output dirs
dir_base = f'./output/{language}/{version}'
os.makedirs(dir_base, exist_ok=True)
for file in os.listdir(dir_base):
    os.remove(os.path.join(dir_base, file))

meta_tests = []

for i, test in enumerate(filtered_tests, 1):
    idx = i
    name = f'test{idx:03d}'
    description = test.get('description', '')
    code = test.get('code', '')
    input_val = test.get('input', '')
    output_val = test.get('output', '')
    exception_val = test.get('exception', False)

    # Translate code using aliases
    for k, v in aliases.items():
        if k == "&NL" and v == "\\n":
            code = code.replace(k, "\n")            
        else:
            code = code.replace(k, v)

        output_val = output_val.replace(k, v)
        

    # Replace $ with random int between 1 and 9
    while '$' in code:
        code = code.replace('$', str(randint(1, 9)), 1)

    # Replace ? with a random lowercase letter except 'l'
    letters = [c for c in string.ascii_lowercase if c != 'l']
    randletter = letters[randint(0, len(letters)-1)]
    while '?' in code:
        code = code.replace('?', randletter, 1)

    # Write code file
    code_filename = f'{name}.{ext}'
    with open(os.path.join(dir_base, code_filename), 'w') as f:
        f.write(code)

    input_val = [] if input_val == '' else input_val.split('\n')
    output_val = output_val.split('\n')

    # Collect metadata
    meta_tests.append({
        'index': idx,
        'name': name,
        'description': description,
        'input': input_val,
        'output': output_val,
        'exception': exception_val
    })


# Write metadata YAML
meta_yaml = {'tests': meta_tests}
with open(os.path.join(dir_base, 'tests.yaml'), 'w') as f:
    yaml.dump(meta_yaml, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

print(f'Generated {len(meta_tests)} tests for {language} {version} in {dir_base}')
