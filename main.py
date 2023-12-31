import requests
from .scrape import fetch_html, parse_html, select_elements, xpath_elements

cookies = {
    'LocationIP': '99.235.82.251',
    'Location': '%7b%22LocationID%22%3a-1%2c%22City%22%3a%22Brampton%22%2c%22State%22%3a%22Ontario%22%2c%22Country%22%3a%22Canada%22%2c%22IsDefaultedToUS%22%3afalse%2c%22Latitude%22%3a43.6445%2c%22Longitude%22%3a-79.7755%2c%22LocationName%22%3a%22Brampton%2c+ON%22%2c%22LocationOverride%22%3afalse%7d',
    'BBHChatLocation': 'forumLocation=Brampton%2c+Ontario%2c+Canada&forumCrumb=Brampton%2c+Ontario%2c+Canada',
    '_gcl_au': '1.1.433965438.1703982064',
    '_gid': 'GA1.2.1147889787.1703982064',
    '_gat_UA-226381-7': '1',
    '__adroll_fpc': '4b9153e88bffe17cb84d9f4ca60f1b12-1703982064359',
    '_fbp': 'fb.1.1703982064387.1105526362',
    'filterValue': '{%22z%22:12%2C%22c%22:{%22lat%22:43.688478%2C%22lng%22:-79.761638}%2C%22s%22:%22feat%22%2C%22f%22:{%22s%22:[%22Selling%22%2C%22Registration%22]%2C%22ss%22:%22For%20Sale%22%2C%22ht%22:[]%2C%22pmin%22:%22%22%2C%22pmax%22:%22%22%2C%22bd%22:[]%2C%22c%22:[]%2C%22o%22:[%22All%22%2C%22Condo%22%2C%22Condop%22%2C%22Co-op%22%2C%22Freehold%22]%2C%22g%22:null%2C%22q%22:false}}',
    '_ga': 'GA1.1.760002224.1703982064',
    '_ga_YWL5PQTNXN': 'GS1.1.1703982064.1.1.1703982069.55.0.0',
    '__ar_v4': 'PUJDS5YEQNEIDCLXKBDXJS%3A20240030%3A2%7C3IQLEBVAZVCHFHXJMPMFR2%3A20240030%3A2%7CIAOCJYV6VJB4HK5OANHDZQ%3A20240030%3A2',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Cookie': 'LocationIP=99.235.82.251; Location=%7b%22LocationID%22%3a-1%2c%22City%22%3a%22Brampton%22%2c%22State%22%3a%22Ontario%22%2c%22Country%22%3a%22Canada%22%2c%22IsDefaultedToUS%22%3afalse%2c%22Latitude%22%3a43.6445%2c%22Longitude%22%3a-79.7755%2c%22LocationName%22%3a%22Brampton%2c+ON%22%2c%22LocationOverride%22%3afalse%7d; BBHChatLocation=forumLocation=Brampton%2c+Ontario%2c+Canada&forumCrumb=Brampton%2c+Ontario%2c+Canada; _gcl_au=1.1.433965438.1703982064; _gid=GA1.2.1147889787.1703982064; _gat_UA-226381-7=1; __adroll_fpc=4b9153e88bffe17cb84d9f4ca60f1b12-1703982064359; _fbp=fb.1.1703982064387.1105526362; filterValue={%22z%22:12%2C%22c%22:{%22lat%22:43.688478%2C%22lng%22:-79.761638}%2C%22s%22:%22feat%22%2C%22f%22:{%22s%22:[%22Selling%22%2C%22Registration%22]%2C%22ss%22:%22For%20Sale%22%2C%22ht%22:[]%2C%22pmin%22:%22%22%2C%22pmax%22:%22%22%2C%22bd%22:[]%2C%22c%22:[]%2C%22o%22:[%22All%22%2C%22Condo%22%2C%22Condop%22%2C%22Co-op%22%2C%22Freehold%22]%2C%22g%22:null%2C%22q%22:false}}; _ga=GA1.1.760002224.1703982064; _ga_YWL5PQTNXN=GS1.1.1703982064.1.1.1703982069.55.0.0; __ar_v4=PUJDS5YEQNEIDCLXKBDXJS%3A20240030%3A2%7C3IQLEBVAZVCHFHXJMPMFR2%3A20240030%3A2%7CIAOCJYV6VJB4HK5OANHDZQ%3A20240030%3A2',
    'Origin': 'https://www.livabl.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.livabl.com/map',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'X-NewRelic-ID': 'UgcBWFFbGwcAUVJXAQQ=',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

json_data = {
    'sellStatus': 'fs',
    'homeType': [],
    'priceMin': 0,
    'priceMax': 0,
    'bdRmCount': [],
    'conStatus': [],
    'sqFtMin': 0,
    'sqFtMax': None,
    'bathRmCount': None,
    'compltYear': None,
    'ownership': [],
    'sellStatusType': [
        'fs',
        'ir',
    ],
    'keywords': None,
    'garageCount': None,
    'isQuickMoveIn': False,
    'topLeft': '43.73079118386156,-79.88798077343752',
    'btmRight': '43.64613494539997,-79.63529522656252',
    'requestId': 2,
    'bId': 0,
    'bTypeId': 0,
}

import json
from pprint import pprint

# Example usage of the scrape.py functions
url = 'http://example.com'  # Replace with the actual URL
html_content = fetch_html(url)
soup = parse_html(html_content)
# Replace '.css-selector' with the actual CSS selector
# Replace '/xpath/expression' with the actual XPath expression
elements_by_css = select_elements(soup, '.css-selector')
elements_by_xpath = xpath_elements(soup, '/xpath/expression')

# Print the elements to the console
pprint(elements_by_css)
pprint(elements_by_xpath)

# Alternatively, write the elements to a file
with open('extracted_data.txt', 'w') as file:
    for element in elements_by_css:
        file.write(str(element))
    for element in elements_by_xpath:
        file.write(str(element))

# def fetch_api_data(api_url, request_data):
#     response = requests.post(api_url, cookies=cookies, headers=headers, json=request_data)
    # Parse the response JSON
    response_json = response.json()
    # Organize the data in a specific format
    organized_data = organize_data(response_json)
    return organized_data

def organize_data(data):
    # Implement this function to organize the data in a specific format
    organized = {} # Placeholder for organized data structure
    # TODO: Add code to organize the data as required
    pprint(organized) # Use pprint to output the organized data
    return organized

response = fetch_api_data('https://www.livabl.com/api/map/GetPins', json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"sellStatus":"fs","homeType":[],"priceMin":0,"priceMax":0,"bdRmCount":[],"conStatus":[],"sqFtMin":0,"sqFtMax":null,"bathRmCount":null,"compltYear":null,"ownership":[],"sellStatusType":["fs","ir"],"keywords":null,"garageCount":null,"isQuickMoveIn":false,"topLeft":"43.73079118386156,-79.88798077343752","btmRight":"43.64613494539997,-79.63529522656252","requestId":2,"bId":0,"bTypeId":0}'
#response = requests.post('https://www.livabl.com/api/map/GetPins', cookies=cookies, headers=headers, data=data)

# Make the GET request
# response = requests.get(url, headers=headers)

# Check if the request was successful
# if response.status_code != 200:
#     raise Exception(f'Request failed with status code: {response.status_code}')
# if response.status_code == 200:
#     print("Request successful!")
    # Write response content to output.json
    import json
    with open('output.json', 'w') as file:  # 'w' mode will overwrite the file if it exists
        json.dump(response.json(), file)
# else:
#     print("Request failed with status code:", response.status_code)
