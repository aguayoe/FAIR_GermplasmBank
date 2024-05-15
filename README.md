# Libraries and Support Tooling for FAIRification of Germplasm Databases
This repository contanins the underlying tools, vocabularies, and models that will be used to execute the FLAIR-GG Network, which is part of the FLAIR-GG Project, a collaborative project between the César Gómez-Campo Germplasm Bank of the Universidad Politécnica de Madrid (BGV-UPM) and CBGP-INIA-CSIC: FLAIR-GG-TED2021-130788B-I00. It is funded by MCIN/AEI /10.13039/501100011033 and by European Union Next Generation EU/ PRTR. This project aims to create a FAIR - Findable, Accessible, Interoperable, Reusable - way to represent seedbank data and improve the public metadata describing all participating seedbanks. All germplasm resources will be linked through a shared portal called the "Virtual Platform", enabling combined searches across all participants within the FLAIR-GG Network. This is also thanks to Universidad Autónoma de Madrid.

## File Structure
MAP concepts into ontologies/
├── Semantic Models/
├── CSV/
│   ├── germplasm.csv
│   ├── administrative.csv
│   └── location.csv
├── Images/
│   ├── Administration model.png
│   ├── Germplasm model.png
│   └── Location model.png
├── YARRRML mapping models/
│   ├── admin_model.py
│   ├── administrative.yaml
│   ├── administrative_yarrrml.pre-yaml
│   ├── germplasm_model.py
│   ├── location.yaml
│   ├── location_model.py
│   ├── location_yarrrml.pre-yaml
│   ├── test2_yarrrml.pre-yaml
│   ├── test_yarrrml.pre-yaml
├── Standardized CSV file/
│   └── Date_format.py
├── LICENSE
└── README.md

## Description

- 'Semantic Models/': Contains the conceptual models used as input for the mapping process.
- 'CSV/': Contains the CSV files used as data sources for the mapping process.
- 'Images/': Contains visual representations (PNG files) of the conceptual models.
- 'YARRRML mapping models/': Contains the YARRRML mapping rules (YAML and Python files) used to transform the conceptual models into ontologies.
- 'Standardized CSV file/': Contains a Python script for standardizing the date format in the CSV files.

## Usage

1. Ensure you have the necessary dependencies installed (e.g., Python, YARRRML, EMbuilder, etc.). See 'requirements.txt'.
2. Run the mapping process using the provided scripts or tools.

This repository contains the code and resources for mapping conceptual models into ontologies using YARRRML mapping rules.

## File Structure
MAP concepts into ontologies/
├── Semantic Models/
├── CSV/
│   ├── README.md
│   ├── administrative.csv
│   └── location.csv
├── Images/
│   ├── Administration_model.png
│   ├── Germplasm model.png
│   └── Location model.png
├── YARRRML mapping models/
│   ├── admin_model.py
│   ├── administrative.yaml
│   ├── administrative_yarrrml.pre-yaml
│   ├── germplasm_model.py
│   ├── location.yaml
│   ├── location_model.py
│   ├── location_yarrrml.pre-yaml
│   ├── test2_yarrrml.pre-yaml
│   ├── test_yarrrml.pre-yaml
│   ├── Administration_model.drawio
│   ├── Diagrama sin titulo.drawio
│   ├── Germplasm model.drawio
│   └── Location model.drawio
├── Standardized CSV file/
│   └── Date_format.py
├── LICENSE
└── README.md

## Description

- `Semantic Models/`: Contains the conceptual models used as input for the mapping process.
- `CSV/`: Contains the CSV files used as data sources for the mapping process.
- `Images/`: Contains visual representations (PNG files) of the conceptual models.
- `YARRRML mapping models/`: Contains the YARRRML mapping rules (YAML and Python files) used to transform the conceptual models into ontologies.
- `Standardized CSV file/`: Contains a Python script for standardizing the date format in the CSV files.
- `LICENSE`: The license file for the project.
- `README.md`: This file, providing an overview of the project and its file structure.

## Usage

1. Ensure you have the necessary dependencies installed (e.g., Python, YARRRML, etc.).
2. Modify the YARRRML mapping rules in the `YARRRML mapping models/` directory as needed.
3. Run the mapping process using the provided scripts or tools.
4. The resulting ontologies will be generated based on the mapping rules and the input data sources.

## Contact
If you encounter any issues or have suggestions for improvements, please contact me: elena.aguayo@estudiante.uam.es, elena.aguayo@protonmail.com
