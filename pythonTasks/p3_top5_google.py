from googlesearch import search


def search_query():
	query = input("Enter your query : ")

	# Perform a Google search and retrieve the top 5 results
	for url in search(query, num_results=6):
		print(url)


search_query()
