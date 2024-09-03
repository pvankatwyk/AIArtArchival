
# AIArtArchival: Image Captioning and Keyword Extraction Tool

This tool automatically generates captions and extracts keywords (nouns and verbs) from  images of artwork. The results are saved in a JSON file. You don't need to know how to code to use this tool; just follow the instructions below.

## Prerequisites

Before running the tool, you need to set up the environment. You can do this by first installing Python, then using `pipx` to install Poetry, which is a tool for dependency management in Python.

### Step 1: Install Python

1. **Download and Install Python**
   - Download Python from [python.org](https://www.python.org/downloads/) and follow the installation instructions.
   - Make sure to check the box to add Python to your PATH during installation.

### Step 2: Install pipx

1. **Install pipx**
   - Open a terminal (Command Prompt on Windows) and run the following command to install `pipx`:

     ```bash
     python -m pip install --user pipx
     python -m pipx ensurepath
     ```

2. **Close and Reopen the Terminal**
   - After installing `pipx`, close and reopen your terminal for the changes to take effect.

### Step 3: Install Poetry using pipx

1. **Install Poetry**
   - With `pipx` installed, you can now install Poetry by running:

     ```bash
     pipx install poetry
     ```

### Step 4: Set Up the Project

1. **Clone the Repository**
   - Clone the repository containing the code:

     ```bash
     git clone https://github.com/pvankatwyk/AIArtArchival.git
     cd AIArtArchival
     ```

2. **Install Dependencies**
   - Use Poetry to install the required dependencies:

     ```bash
     poetry install
     ```

3. **Run the Script**
   - Activate the virtual environment and run the script:

     ```bash
     poetry run python aiartarchival/archive.py
     ```

## How to Use the Tool

1. **Place Your Images in the Correct Folder:**
   - Place all the images you want to process in a folder on your computer. Update the `artwork_directory` variable in the code with the path to this folder.

2. **Run the Script:**
   - Follow the steps in the "Run the Script" section above.

3. **View the Results:**
   - After running the script, a file named `captions_and_keywords.json` will be created in the same directory as the script.
   - This file contains the generated captions and extracted keywords for each image.

## Example Output

The output file (`captions_and_keywords.json`) will look something like this:

```json
[
    {
        "image": "example.jpg",
        "caption": "A beautiful sunset over the mountains.",
        "keywords": {
            "nouns": ["sunset", "mountains"],
            "verbs": ["over"]
        }
    },
    {
        "image": "another_image.png",
        "caption": "A dog playing in the park.",
        "keywords": {
            "nouns": ["dog", "park"],
            "verbs": ["playing"]
        }
    }
]
```

## Troubleshooting

- **spaCy Model Download**: If you get an error about spaCy not finding the language model, ensure you've followed Step 3 above.

- **Other Errors**: If you encounter any issues, please reach out for support.
