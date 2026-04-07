<div align="center">

# FAIR_GermplasmBank
### Libraries & Support Tooling for FAIRification of Germplasm Databases (FLAIR-GG)

Tools, vocabularies, semantic models, and mappings to support the **FAIRification** of germplasm databases within the **FLAIR-GG Network** (FLAIR-GG Project).

<p>
  <img alt="Status" src="https://img.shields.io/badge/Status-Work%20in%20progress-f59e0b?style=for-the-badge" />
  <img alt="Focus" src="https://img.shields.io/badge/Focus-FAIR%20Data-2563eb?style=for-the-badge" />
  <img alt="Mappings" src="https://img.shields.io/badge/Mappings-YARRRML-111827?style=for-the-badge" />
  <img alt="License" src="https://img.shields.io/badge/License-MIT-16a34a?style=for-the-badge" />
</p>

<p>
  <a href="https://github.com/aguayoe" target="_blank">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-aguayoe-111827?style=for-the-badge&logo=github" />
  </a>
</p>

</div>

---

## Overview
This repository contains the underlying resources used to support the **FAIRification** workflow for germplasm databases:
- **Conceptual/Semantic models** used as inputs for mapping
- **Source CSV templates/data** used in the mapping process
- **YARRRML mapping rules** used to transform structured data into RDF/ontologies
- Supporting scripts to standardize data and assist the mapping pipeline

## Repository structure
- `Semantic Models/` — conceptual/semantic models used as input for the mapping process
- `CSV/` — CSV files used as data sources for the mapping process
- `Images/` — PNG visual representations of the conceptual models
- `YARRRML mapping models/` — YARRRML mapping rules (YAML and helper Python files)
- `Standardized CSV file/` — scripts to standardize/normalize CSV contents (e.g., date formats)
- `requirements.txt` — Python dependencies required by some tooling/scripts

> Tip: The folder `Semantic Models/CSV/` includes CDE template documentation (see its README).

## Getting started

### Prerequisites
- Python (recommended: 3.10+)
- Tools depending on your workflow (e.g., **YARRRML**, EMBuilder, etc.)

### Install Python dependencies (if needed)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage (high level)
1. Review the conceptual model(s) in `Semantic Models/` and/or `Images/`.
2. Prepare/validate your input data using the CSV templates in `CSV/` (or `Semantic Models/CSV/`).
3. Apply the **YARRRML mapping rules** in `YARRRML mapping models/` to generate RDF aligned with the target ontology.
4. (Optional) Run the scripts in `Standardized CSV file/` to normalize inputs (e.g., date formats) before mapping.

## Notes on templates (CDEs)
Template documentation is available under:
- `Semantic Models/CSV/README.md`

It describes expected fields and datatypes for:
- Location templates (e.g., lat/long, country codes, ISO dates)
- Germplasm templates
- Administrative templates (org identifiers, roles, etc.)

## Contributing
Issues and suggestions are welcome. If you contribute mappings or templates:
- keep identifiers stable
- document required fields + datatypes
- avoid embedding private/sensitive data in example files

## Contact
For questions or suggestions:
- elena.aguayo@cchs.csic.es
- elena.aguayo@protonmail.com

## License
MIT License. See `LICENSE`.
