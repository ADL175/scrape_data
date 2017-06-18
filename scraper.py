import requests
from bs4 import BeautifulSoup
import sys
import re

INSPECTION_DOMAIN = 'http://info.kingcounty.gov'
INSPECTION_PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
INSPECTION_PARAMS = {
    'Output': 'W',
    'Business_Name': '',
    'Business_Address': '',
    'Longitude': '',
    'Latitude': '',
    'City': '',
    'Zip_Code': '',
    'Inspection_Type': 'All',
    'Inspection_Start': '',
    'Inspection_End': '',
    'Inspection_Closed_Business': 'A',
    'Violation_Points': '',
    'Violation_Red_Points': '',
    'Violation_Descr': '',
    'Fuzzy_Search': 'N',
    'Sort': 'H'
}


def get_inspection_page(**kwargs):
    url = INSPECTION_DOMAIN + INSPECTION_PATH
    params = INSPECTION_PARAMS.copy()
    for key, value in kwargs.items():
        if key in INSPECTION_PARAMS:
            params[key] = value
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.content, resp.encoding


def load_inspection_page(**kwargs):
    # url = inspection_page.html
    import pdb; pdb.set_trace()
    params = INSPECTION_PARAMS.copy()
    for key, value in kwargs.items():
        if key in INSPECTION_PARAMS:
            params[key] = value
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.content, resp.encoding


def extract_data_listings(html):
    id_finder = re.compile(r'PR[\d]+~')
    return html.find_all('div', id=id_finder)


def parse_source(html, encoding='utf-8'):
    parsed = BeautifulSoup(html, 'html5lib', from_encoding=encoding)
    return parsed


def has_two_tds(elem):
    is_tr = elem.name == 'tr'
    td_children = elem.find_all('td', recursive=False)
    has_two = len(td_children) == 2
    return is_tr and has_two


if __name__ == "__main__":
    kwargs = {
        'Inspection_Start': '2/1/2013',
        'Inspection_End': '2/1/2015',
        'Zip_Code': '98109'
    }
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        html, encoding = load_inspection_page('inspection_page.html')
    else:
        html, encoding = get_inspection_page(**kwargs)
    doc = parse_source(html, encoding)
    listings = extract_data_listings(doc)
    for listing in listings[:5]:
        metadata_rows = listing.find('tbody').find_all(
            has_two_tds, recursive=False
        )
        for row in metadata_rows:
            for td in row.find_all('td', recursive=False):
                print(td.text)
            print()
        print()
        # print(len(metadata_rows))
    # print(doc.prettify(encoding=encoding))
