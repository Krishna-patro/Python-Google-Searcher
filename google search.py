from googlesearch import search

def search_google(query, num_results=10):
    """
    Performs a Google search and prints the URLs of the results.
    """
    try:
        print(f"Searching for: '{query}'...")
        for url in search(query, num_results=num_results, stop=num_results, pause=2):
            print(url)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    search_term = "What is Python"
    search_google(search_term)
