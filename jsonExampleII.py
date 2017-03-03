import requests

def get_jason_data():
	#url = "http://api.geonames.org/citiesJSON?north=44.1&south=-9.9&east=-22.4&west=55.2&lang=de&username=demo"
	url = "http://api.geonames.org/postalCodeLookupJSON?postalcode=6600&country=AT&username=demo"
	try:
		request = requests.get(url)

		fetch_data = request.json()

		print(request.status_code)

#		print (request.content)

		for item in fetch_data['postalcodes']:

			write_output = []
			write_output = (item['placeName'],item['countryCode'])
			print(write_output)

	except:
		print("Unexpected error:", sys.exc_info()[0]) 			



def main():
	print("Inside Main Function")
	get_jason_data()


main()
