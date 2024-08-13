# PDF Data Extractor and Oracle Database Filler

## Overview

This Python project is designed to automate the process of extracting data from PDF documents and inserting that data into an Oracle database. The project streamlines data handling by parsing PDFs, transforming the extracted data into a suitable format, and efficiently storing it in a relational database.

## Features

- **PDF Parsing**: Automatically reads and extracts data from PDF files, handling various PDF formats and layouts.
- **Data Transformation**: Cleans and transforms the extracted data into a structured format suitable for database storage.
- **Oracle Database Integration**: Connects to an Oracle database to insert the extracted and transformed data into predefined tables.
- **Error Handling**: Robust error handling for common issues such as database connectivity problems, data inconsistencies, and PDF parsing errors.
- **Batch Processing**: Supports batch processing of multiple PDFs, ensuring efficient handling of large datasets.

## Requirements

- Python 3.7+
- Oracle Database 12c or later
- Required Python Packages:
  - `PyPDF2` or `pdfminer.six` (for PDF extraction)
  - `cx_Oracle` (for Oracle database interaction)
  - `pandas` (for data manipulation)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/info424/pdf-oracle-extractor.git
    cd pdf-oracle-extractor
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure your Oracle database connection in the `config.py` file:

    ```python
    oracle_config = {
        'user': 'your_username',
        'password': 'your_password',
        'dsn': 'your_oracle_dsn',
        'encoding': 'UTF-8'
    }
    ```

## Usage

1. Place your PDF files in the `pdfs/` directory.

2. Run the script to extract data and insert it into the Oracle database:

    ```bash
    python pdf_to_oracle.py
    ```

3. Monitor the console output for success messages or errors.

## Project Structure

```
pdf-oracle-extractor/
│
├── pdfs/                # Directory containing PDF files
├── extracted_data/      # Directory for storing intermediate extracted data (optional)
├── config.py            # Oracle database configuration file
├── pdf_to_oracle.py     # Main script for PDF extraction and database insertion
├── utils/               # Utility functions and modules
├── requirements.txt     # Python package dependencies
└── README.md            # Project documentation
```

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to all the contributors and open-source libraries that made this project possible.

---

This README description should give users a clear understanding of your project, its purpose, and how to use it. You can customize it further based on your project's specific needs and structure.