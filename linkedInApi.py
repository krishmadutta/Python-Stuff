import requests
url ="https://www.linkedin.com/profile/view?id=AAoAAALgwO0BW9ChfaWonbtO3NQQrUlnh-NNqd8&authType=name&authToken=jvFn&trk=api*a3227641*s3301901*"
request = requests.get(url)
data = request.json()
print (data)