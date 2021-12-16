
import requests

def print_xml():
    url = "https://httpbin.org/anything"
    condition = requests.get(url)
    if condition.status_code == 200:
        headers = condition.headers
    for key in headers:
        line = f'<{key}>{headers[key]}</{key}>'
        print (line)
print_xml()
print("*****************")
import json

def print_json():
    url = "https://httpbin.org/anything"
    condition = requests.get(url)
    if condition.status_code == 200:
        body = json.loads(condition.text)
    for key in body:
        if key != 'headers':
            line = f'<{key}>{body[key]}</{key}>'
            print (line)
        else:
            for inner_key in body[key]:
                line = f'\t<{inner_key}>{body[key][inner_key]}</{inner_key}>'
                print (line)
print_json()


format = input()
if format == 'xml':
    print_json()
if format == 'html':
    print('<html>')
    print('<headers>')
    print_xml()
    print('</headers>')
    print('<body>')
    print_json()
    print('</body>')
    print('</html>')