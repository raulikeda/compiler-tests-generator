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

def translate_code(metalanguage_code, target_language):
    # Load the language dictionary
    data = load_language_dict(target_language)
    ext = data['extension']
    aliases = flatten_aliases(data['aliases']) if 'aliases' in data else {k: v for k, v in data.items() if k != 'extension'}

    code = metalanguage_code

    # Translate code using aliases
    for k, v in aliases.items():
        if k == "&NL" and v == "\\n":
            code = code.replace(k, "\n")            
        else:
            code = code.replace(k, v)

    # Replace $ with random int between 1 and 9
    while '$' in code:
        code = code.replace('$', str(randint(1, 9)), 1)

    # Replace ? with a random lowercase letter except 'l'
    letters = [c for c in string.ascii_lowercase if c != 'l']
    randletter = letters[randint(0, len(letters)-1)]
    while '?' in code:
        code = code.replace('?', randletter, 1)

    return code

# The rest of the original logic can be kept if needed, but for the function, this is the core
# If you want to generate files, you can add more functions or modify as needed
