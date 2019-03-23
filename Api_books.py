import requests
base = 'http://pulse-rest-testing.herokuapp.com/'
books_url = base + 'books/'

book = {
    "title": "Green mile",
    "author": "Steven King"
}

resp = requests.post(books_url, data=book)

req_dict = resp.json()

print(req_dict)

resp = requests.get(books_url + str(req_dict["id"]))

print(resp)

resp = requests.put(books_url + str(req_dict["id"]), data={"title": "Green mile1234"})

req_dict = resp.json()

print(req_dict)

resp = requests.delete(books_url + str(req_dict["id"]))

print(resp)