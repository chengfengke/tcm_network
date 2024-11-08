# TCM Formula and Disease Analysis Script

This Python script enables users to analyze Traditional Chinese Medicine (TCM) formulas and their associated herbs, chemical ingredients, and protein targets. Using an API, the script fetches information about formulas, herbs, chemical ingredients, and disease targets, and aggregates relevant data for further analysis.

## Prerequisites

Ensure you have the following dependencies installed:
- `requests`: For making HTTP requests to the API.
- `urllib`: For encoding URL parameters.
- `json`: For handling JSON payloads and responses.

## Files

The script requires the following Python files for defining object structures:

- `formula.py`: Contains the `Formula` class to store TCM formula details.
- `herb.py`: Contains the `Herb` class to store herb data.
- `ingredient.py`: Contains the `Ingredient` class for handling individual herb ingredients.
- `protein.py`: Contains the `Protein` class to store protein target data.
- `disease.py`: Contains the `Disease` class for disease-related information.

## Functions

### 1. `get_tcmid(herb_name)`

Fetches the TCM formula data for a specified herb name.
- **Input**: `herb_name` (string) - the name of the herb to search for.
- **Returns**: A `Formula` instance containing `hvp_id` and `name` if successful, or `None` if no data is found.

### 2. `get_herbs(formula)`

Fetches herb details based on the `hvp_id` of the provided `Formula` object.
- **Input**: `formula` (Formula object) - a formula object with a valid `hvp_id`.
- **Returns**: A list of `Herb` objects containing herb information and ingredients.

### 3. `get_chemical_ingredients(hvm_id)`

Fetches chemical ingredients for a given herb ID (`hvm_id`).
- **Input**: `hvm_id` (string) - herb ID.
- **Returns**: A list of chemical ingredients as JSON data.

### 4. `get_protein_targets(hvc_id)`

Fetches protein targets for a given chemical compound using its `hvc_id`.
- **Input**: `hvc_id` (string) - compound ID.
- **Returns**: A list of `Protein` objects.

### 5. `get_disease_targets(disease_key)`

Fetches disease targets for a specific disease keyword.
- **Input**: `disease_key` (string) - the name of the disease to search for.
- **Returns**: A `Disease` object with the chosen disease's details.

## Usage

1. **Run the Script**: The script prompts for an herb name and a disease name.
   ```python
   formula_name = input("Enter the name of the herb: ")
   disease_name = input("Enter the name of the disease: ")