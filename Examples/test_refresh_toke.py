'''import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YXM6YXNwYXNz',
    'X-Device-Id': '{{SALEXEEU5P2223801}}',
    'Connection': 'close',
}

json_data = {
    'grant_type': 'refresh_token',
    'refresh_token': '{{refresh_token}}',
}

response = requests.post(
    'https://ifas.prod-row.jlrmotor.com/ifas/jlr/tokens', headers=headers, json=json_data)

print(response)
'''


import requests

headers = {
    'Accept': 'application/vnd.wirelesscar.ngtp.if9.User-v3+json',
    'Content-Type': 'application/json',
    'X-Device-Id': '{{SALEXEEU5P2223801}}',
}

response = requests.get(
    'https://if9.prod-row.jlrmotor.com/if9/jlr/users?loginName={{sjpbailey@comcast.net}}', headers=headers)


print(response)
