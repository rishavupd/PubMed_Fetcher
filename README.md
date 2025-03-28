# PubMed Fetcher

## Overview
The **PubMed Fetcher** is a Python-based command-line tool that retrieves research papers from PubMed based on user-defined queries. It filters papers that have at least one author affiliated with a pharmaceutical or biotech company and exports the results as a CSV file.

## Features
- Fetches PubMed research papers based on a given search query.
- Filters papers where at least one author has a non-academic affiliation.
- Outputs results in a structured CSV format.
- Supports command-line options for user-defined queries, result limits, and debug mode.
- Implements error handling and logging for debugging purposes.

## Installation
This project uses **Python 3.12** and **Poetry** for dependency management. To set up the project, follow these steps:

### Prerequisites
1. Ensure you have **Python 3.12** installed.
2. Install Poetry (if not already installed):
   ```sh
   pip install poetry
   ```

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/pubmed-fetcher.git
   cd pubmed-fetcher
   ```
2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

## Usage
The program is executed through the command line. The available options are:

```sh
poetry run python src/cli.py --query "cancer[Title/Abstract]" --max-results 5 --output output.csv
```

### Command-line Arguments
| Argument         | Description                                         | Example |
|-----------------|-----------------------------------------------------|---------|
| `--query`       | Search query for PubMed.                          | "cancer[Title]" |
| `--max-results` | Limit the number of results (default: 10).        | `--max-results 5` |
| `--output`      | Output CSV file name (default: results.csv).      | `--output results.csv` |
| `--debug`       | Enable debug mode for troubleshooting.            | `--debug` |

## Example Output
A sample CSV file generated by the tool:
```csv
PubmedID,Title,Publication Date,Non-academic Author(s),Company Affiliation(s),Corresponding Author Email
12345678,Advances in Cancer Immunotherapy,2025-01-15,John Doe,Genentech Inc.,john.doe@genentech.com
23456789,Novel Drug Delivery Systems for Oncology,2024-12-10,Alice Johnson,Moderna,alice.johnson@moderna.com
```

## Project Structure
```
pubmed_fetcher/
├── src/
│   ├── __init__.py
│   ├── cli.py              # Command-line interface implementation
│   ├── pubmed_fetcher.py   # Core logic for fetching and filtering papers
│   └── tests/
│       ├── __init__.py
│       └── test_pubmed_fetcher.py   # Unit tests
├── README.md               # Project documentation
├── .gitignore              # Git ignore file
├── pyproject.toml          # Poetry dependency management file
├── poetry.lock             # Poetry lock file
```

## Development & Contribution
### Running Tests
To run the test suite:
```sh
poetry run pytest
```

### Contributing
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

## Future Improvements
- Implement additional filters (publication date, journal, specific authors).
- Improve performance using asynchronous requests.
- Cache API responses for efficiency.
- Publish as a PyPI package.

## References
- [PubMed API Documentation](https://www.ncbi.nlm.nih.gov/books/NBK25500/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## License
This project is licensed under the MIT License.

