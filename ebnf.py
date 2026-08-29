import sys
import yaml
import os

version = sys.argv[1] if len(sys.argv) > 1 else "v1.0"
language = sys.argv[2] if len(sys.argv) > 2 else "C"

# Open ebnf file
ebnf_file = f"./data/ebnf/{version}.yaml"
with open(ebnf_file, "r") as f:
    ebnf = f.read()

# open dictionary file
dictionary_file = f"./data/languages/{language}.yaml"
with open(dictionary_file, "r") as f:
    dictionary = yaml.safe_load(f)['aliases']

for word in dictionary:
    for k, v in word.items():
        if k == "&LF" and v == "":
            ebnf = ebnf.replace(k, "\\n")
        elif v == "":
            ebnf = ebnf.replace('"' + k + '"', "ε")
            ebnf = ebnf.replace(", ε", "")
        else:
            ebnf = ebnf.replace(k, v)

if not os.path.exists(f"./output/syntax/{version}"):
    os.makedirs(f"./output/syntax/{version}")

with open(f"./output/syntax/{version}/ebnf-{language.lower()}.txt", "w") as f:
    f.write(ebnf)
