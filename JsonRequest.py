import requests
from urllib2 import Request, urlopen, URLError 


url = "https://status.github.com/api/status.json"
try:  
	request = requests.get(url)

	fetch_data_json = request.json()

print(request.headers(''))
	print(request.status_code)
	print(request.content)
	print(request.headers)
	#print(response.headers['content-type'])
	print('########################################################')
	print(fetch_data_json['status'] + ' - '+ fetch_data_json['last_updated']  )
	print('########################################################')

except URLError, e:
	print ("Can't Get Data")

