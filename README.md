# Compiler Tests Generator

This project provides a flexible framework for generating, translating, and managing compiler test cases across multiple programming languages. It is designed to help you maintain a library of test cases in YAML format and automatically generate language-specific code and metadata for each test.

## Features
- **YAML-based test management:** Write your tests in a simple YAML format, including metadata, code, expected output, and language applicability.
- **Language translation:** Use alias mappings to translate generic code templates into specific programming languages (C, Go, Zig, etc.).
- **Randomization:** Supports random integer and letter generation for test placeholders.
- **Selective test generation:** Only generate tests for the selected language or for tests marked as "All".
- **Output organization:** Generates code files and a summary YAML for each language/version in a structured output directory.

## Directory Structure
```
compiler-tests-generator/
├── data/
│   ├── languages/           # Language alias YAML files (C.yaml, go.yaml, zig.yaml, ...)
│   └── tests/               # Test case YAML files (v1.0.yaml, v2.1.yaml, ...)
├── output/                  # Generated code and metadata (created by generate.py)
├── generate.py              # Main script to generate code and metadata
├── requirements.txt         # Python dependencies
└── README.md
```

## Setup
1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### 1. Prepare your test YAML
- Write your test cases in `data/tests/vX.Y.yaml` using the following format:
  ```yaml
  - description: Valid Input
    code: "..."
    input: "..."
    output: |
      ...
    exception: false
    languages: [All]  # or [C], [Go], etc.
  ```

### 2. Prepare your language YAML
- Define language-specific aliases in `data/languages/{LANG}.yaml`:
  ```yaml
  extension: c
  aliases:
    - "&LBRA": "{"
    - "&RBRA": "}"
    # ...
  ```

### 3. Generate tests
Run the generator for a specific version and language:
```bash
python generate.py v2.3 C
```
- This will create code files and a `tests.yaml` in `output/C/v2.3/`.
- Only tests with `languages: [All]` or `languages: [C]` will be included.

### 4. Output
- For each test, a code file (e.g., `test001.c`) is generated with all aliases replaced.
- A `tests.yaml` file is generated with metadata for all included tests.

## Test Placeholders
- `$` in code: replaced by a random integer (1-9)
- `?` in code: replaced by a random lowercase letter (except 'l')
- `&NL` in code: replaced by a newline (or removed in v2.1+ YAMLs)

## Adding a New Language
1. Create a new YAML in `data/languages/` (e.g., `Rust.yaml`) with `extension` and `aliases`.
2. Add `Rust` as a value in the `languages` field of relevant tests.
3. Run the generator as above.

## License
MIT License

## TODO
Fix 2.4 for C tests. Compare with 2.3