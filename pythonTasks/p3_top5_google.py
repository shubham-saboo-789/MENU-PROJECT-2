from googlesearch import search



def search_query():
	query = input("Enter your query : ")

	# Perform a Google search and retrieve the top 5 results
	for url in search(query, num_results=6):
		print(url)
	
	

def search_query_api(query):
    urls = []

    # Perform a Google search and retrieve the top 5 results
    for url in search(query, num_results=6):
        urls.append(url)
    
    return urls
