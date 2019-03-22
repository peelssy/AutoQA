import requests
base = "http://pulse-rest-testing.herokuapp.com/"
roles_url = base + 'roles/'
role = {
    "name": "Frodo123",
    "type": "hobit",
    "level": 10,
    "book": 104
}
resp = requests.post(roles_url, data=role)

req_dict = resp.json()

print(req_dict)

resp = requests.get(roles_url + str(req_dict['id']))
print(resp)

resp = requests.put(roles_url + str(req_dict['id']), data={"name": "Frodo1234"})

req_dict = resp.json()

print(req_dict)

resp = requests.delete(roles_url + str(req_dict['id']))

# req_dict = resp.json()

print(resp)

