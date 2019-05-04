from lib.google_search_results import GoogleSearchResults

params = {
    "q" : "playoffs",
    "location" : "Austin, Texas, United States",
    "hl" : "en",
    "gl" : "us",
    "google_domain" : "google.com",
}

GoogleSearchResults.SERP_API_KEY = 'demo'

query = GoogleSearchResults(params)
dictionary_results = query.get_dictionary()

print(dictionary_results)