import requests
import pandas as pd
from typing import List, Dict, Optional

def fetch_pubmed_data(query: str, max_results: int = 10) -> List[str]:
    """
    Fetch PubMed IDs for papers matching the query.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results  # Limit the number of results
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])

def get_paper_details(pubmed_id: str) -> Optional[Dict]:
    """
    Fetch details for a specific PubMed ID.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": pubmed_id,
        "retmode": "json"
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("result", {}).get(pubmed_id, {})

def is_non_academic_affiliation(affiliation: str) -> bool:
    """
    Check if an affiliation is non-academic (pharma/biotech).
    """
    non_academic_keywords = ["pharma", "biotech", "inc.", "ltd", "company"]
    return any(keyword in affiliation.lower() for keyword in non_academic_keywords)

def filter_non_academic_authors(paper_details: Dict) -> List[Dict]:
    """
    Filter authors with non-academic affiliations.
    """
    authors = paper_details.get("authors", [])
    non_academic_authors = []
    for author in authors:
        affiliations = author.get("affiliations", [])
        if any(is_non_academic_affiliation(aff) for aff in affiliations):
            non_academic_authors.append(author)
    return non_academic_authors

def fetch_and_filter_papers(query: str, max_results: int = 10) -> pd.DataFrame:
    """
    Fetch and filter papers based on the query.
    """
    pubmed_ids = fetch_pubmed_data(query, max_results)
    results = []
    for pubmed_id in pubmed_ids:
        details = get_paper_details(pubmed_id)
        if details:
            non_academic_authors = filter_non_academic_authors(details)
            if non_academic_authors:
                results.append({
                    "PubmedID": pubmed_id,
                    "Title": details.get("title", ""),
                    "Publication Date": details.get("pubdate", ""),
                    "Non-academic Author(s)": ", ".join([author.get("name", "") for author in non_academic_authors]),
                    "Company Affiliation(s)": ", ".join([aff for author in non_academic_authors for aff in author.get("affiliations", [])]),
                    "Corresponding Author Email": details.get("correspondingauthor", {}).get("email", "")
                })
    return pd.DataFrame(results)