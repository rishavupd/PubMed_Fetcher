import argparse
from pubmed_fetcher import fetch_and_filter_papers

def main():
    """
    Command-line interface for fetching and filtering PubMed papers.
    """
    parser = argparse.ArgumentParser(description="Fetch PubMed papers based on a query.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file name.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    parser.add_argument("-m", "--max-results", type=int, default=10, help="Maximum number of results to fetch.")
    args = parser.parse_args()

    df = fetch_and_filter_papers(args.query, args.max_results)
    if args.file:
        df.to_csv(args.file, index=False)
        print(f"Results saved to {args.file}")
    else:
        print(df.to_string(index=False))

if __name__ == "__main__":
    main()