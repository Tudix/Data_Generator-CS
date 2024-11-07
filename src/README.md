# Document Processing and Metadata Generation Project

This project is a Python-based solution for extracting structured data from Word documents, generating metadata, and organizing routing information for survey processing. It is designed to handle multi-language documents, extract essential project details, and produce well-organized output files for metadata and routing per language.

## Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Modules](#modules)
  - [Core Modules](#core-modules)
  - [Document Processing Modules](#document-processing-modules)
- [Settings Configuration](#settings-configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project parses a Word document to extract survey-related information across multiple sections. It then generates language-specific metadata and routing files in a structured format. Core functionalities include:
- **Multi-language support**: Processes survey information for each language separately.
- **Dynamic metadata generation**: Produces metadata files with categorized information.
- **Routing generation**: Defines survey routing logic based on extracted information.
- **Configurable settings**: Enables customization through a JSON configuration file.

## Project Structure

Below is the structure of the `src` folder, with descriptions of each folder and file.

```plaintext
src
├── config
│   └── settings.json            # Config file containing mappings and parameters
├── core
│   ├── __init__.py              # Imports core functions
│   ├── document_reader.py       # Reads and extracts text from the document
│   ├── json_settings.py         # Loads settings from settings.json
│   └── output_writer.py         # Writes language-specific output files
├── modules
│   ├── __init__.py              # Imports functions from module files
│   ├── brand_product_lists.py   # Manages brand/product lists per language
│   ├── brandproduct.py          # Generates HidLevels and BrandProduct codes
│   ├── cell.py                  # Extracts tested media count and formats cell output
│   ├── category_settings.py     # Extracts category settings and generates outputs
│   ├── exposure_type.py         # Extracts and maps exposure type information
│   ├── filler_media_info.py     # Extracts and formats filler media information
│   ├── media_info.py            # Handles media information and metadata generation
│   ├── project_name.py          # Extracts project name from the document
│   ├── qoe.py                   # Maps QOE-related questions to predefined responses
│   ├── survey_languages.py      # Extracts languages and organizes language dictionary
│   ├── tested_brand_product.py  # Extracts tested brand/product lists per language
│   └── verb_used.py             # Identifies and maps verbs used in the tested ad
└── main.py                      # Main script orchestrating the data extraction process
```

## Setup

1. **Clone the Repository:**
  ```bash
  git clone https://github.com/your-username/your-repo-name.git
  cd your-repo-name/src
  ```

2. **Install Dependencies:** Make sure you have Python installed (>= 3.6). Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

3. **Configure Settings:** The `settings.json` file (located in `src/config`) contains mappings and customizable parameters. Update this file based on your project's needs.

## Usage

1. **Place the Document:** Ensure your Word document is accessible in the project folder.
2. **Run the Main Script:**
```bash
python main.py
```
3. **Output Files:**
- For each language in the document, two files are generated:
  - `metadata_language_name.txt`: Contains metadata specific to the language.
  - `routing_language_name.txt`: Contains routing logic for survey questions.

## Modules

### Core Modules
- **document_reader.py:** Reads and parses the Word document, returning the document text.
- **json_settings.py:** Loads configurations from `settings.json`, providing mappings and parameters to other modules.
- **output_writer.py:** Manages output file creation, saving formatted metadata and routing information for each language.

### Document Processing Modules
Each document processing module performs a unique data extraction or formatting function. Below is a summary of key modules:
- **brand_product_lists.py:** Extracts brand/product lists by language and formats them based on specified criteria.
- **brandproduct.py:** Determines project type, generating `HidLevels` and `BrandProduct` codes based on the specified type (e.g., Brand, Product).
- **cell.py:** Extracts the number of tested media and creates cell definition output.
- **category_settings.py:** Extracts language-specific category settings and generates metadata and routing outputs.
- **exposure_type.py:** Maps exposure types based on keywords in the document.
- **filler_media_info.py:** Manages filler media details and formats filler ads for each language.
- **media_info.py:** Extracts media information, including routing and metadata formats per ad.
- **project_name.py:** Extracts the project name from the document.
- **qoe.py:** Maps responses for QOE-related questions based on pre-defined keywords.
- **survey_languages.py:** Builds a dictionary of all languages present in the document.
- **tested_brand_product.py:** Extracts tested brand and product lists for each language.
- **verb_used.py:** Identifies the verb used in tested ads, mapping it according to settings in `settings.json`.

## Settings Configuration
The `settings.json` file is crucial for the project’s customization. It contains mappings for keywords, codes, and settings used in various modules. Examples include:

- **Exposure Type Mappings:** Defines keywords to identify different exposure types.
- **Verb Mappings:** Specifies mappings for verbs used in ads to respective codes.

**Sample `settings.json`**
```json
{
  "exposure_type": {
    "standard": "_1",
    "digital": "_2"
  },
  "verb_used": {
    "choose": 1,
    "use": 2,
    "visit ": 3
  }
}
```

## Testing
Unit tests are provided in the `tests` folder. To run the tests:

```bash
pytest tests/
```

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request describing the feature or fix.

## License

This project is proprietary software and is not open-source. The following restrictions apply:

1. **Usage:** This software may not be used, copied, or accessed without prior written permission from the author.
2. **Distribution:** Redistribution, sharing, or reselling of this software, in whole or in part, is strictly prohibited without explicit permission from the author.
3. **Modification:** Modification or creation of derivative works based on this software is not permitted.
4. **Disclaimer:** This software is provided "as-is" without any warranties or guarantees. The author is not liable for any damages arising from the use or misuse of this software.

For inquiries regarding usage or licensing permissions, please contact the author directly.