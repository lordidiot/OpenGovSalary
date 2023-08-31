#!/usr/bin/env python3

import json
import requests
import numpy as np
from bs4 import BeautifulSoup
from dataclasses import dataclass

PRODUCT_LISTING_URL = 'https://www.open.gov.sg/products/'
PEOPLE_URL_PREFIX = 'https://www.open.gov.sg/people/'

@dataclass
class ProductInfo:
    people: dict[str, float]
    quarterly_manpower: int

def get_product_info(url: str) -> ProductInfo:
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    script = None
    quarterly_manpower = None

    for script_tag in soup.find_all('script'):
        if 'manpower' in script_tag.text:
            script = script_tag.text
            break

    people = {}
    quarterly_manpower = int(script.split('\\"manpower\\":')[1].split('}')[0])
    members = json.loads(script.split('\\"members\\":')[1].split('\\"values\\":')[1].split(']')[0].replace('\\"', '"') + ']')
    for member in members:
        if 'involvement' in member:
            people[member['id']] = eval(member['involvement']) # TODO: secoority
        else:
            people[member['id']] = 1

    return ProductInfo(people, quarterly_manpower)


def get_product_urls() -> list[str]:
    resp = requests.get(PRODUCT_LISTING_URL)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return list(map(lambda x: x['href'], soup.find_all('a', class_='product')))

def main():
    product_urls = get_product_urls()
    product_infos = list(map(get_product_info, product_urls))

    temp_people = set()
    for product_info in product_infos:
        temp_people.update(product_info.people.keys())
    people = list(temp_people)

    A = []
    Y = []
    for product_info in product_infos:
        _ = [0] * len(people)
        product_members = product_info.people
        for i, person in enumerate(people):
            if person in product_members:
                _[i] = product_members[person]
            
        Y.append(product_info.quarterly_manpower)
        A.append(_)
    
    # Coefficient matrix A
    A = np.array(A)

    # Right-hand side vector
    Y = np.array(Y)

    # Solve using least squares
    solution, residuals, rank, singular_values = np.linalg.lstsq(A, Y, rcond=None)

    if residuals.size == 0:
        print("Found exact solution:")
    else:
        print("Found least-squares solution:")
    print()
    
    for name, quarter_salary in sorted(zip(people, solution), key=lambda x: x[1], reverse=True):
        print("{}: ${:,}/year".format(name, int(quarter_salary * 4)))
 
if __name__ == '__main__':
    main()
