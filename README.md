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

