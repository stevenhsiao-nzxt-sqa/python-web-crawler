import requests 
 
url = "https://api.sgx.com/derivatives/v1.0/contract-code/CN?order=asc&orderby=delivery-month&category=futures&session=-1&t=1669876044693"
r = requests.get(url)
print(r.text)
