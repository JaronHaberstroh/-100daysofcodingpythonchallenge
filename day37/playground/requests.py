import requests

# Get request: to get info from endpoint
results = requests.get(API_ENDPOINT, PARAMS)

# Post request: to post new info to endpoint
results = requests.post(API_ENDPOINT, PARAMS)

# Put requests: to edit new info to endpoint
results = requests.put(API_ENDPOINT, PARAMS)

# Delete requests: to delete info at enpoint
results = requests.delete(API_ENDPOINT, PARAMS)
