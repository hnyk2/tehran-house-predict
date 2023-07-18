from time import sleep

import requests
import csv


def crawl_api(page):
    url = "https://www.melkana.com/v3/home/load-more"

    payload = f"filters%5Bsort%5D%5Btitle%5D=%D8%AC%D8%AF%DB%8C%D8%AF+%D8%AA%D8%B1%DB%8C%D9%86+%D9%87%D8%A7&filters%5Bsort%5D%5Bmodel%5D=approve_time&filters%5Bsort%5D%5Border%5D=desc&filters%5Bdeal_type%5D=0&filters%5Bdeal_type_mobile%5D=0&filters%5Bhas_tour%5D=2&filters%5Bestate_type%5D=2&filters%5Bestate_document%5D=2&filters%5Bprice_analyse%5D=0&filters%5Bfeatures%5D%5B0%5D%5Bid%5D=1&filters%5Bfeatures%5D%5B0%5D%5Bname%5D=%D9%BE%D8%A7%D8%B1%DA%A9%DB%8C%D9%86%DA%AF&filters%5Bfeatures%5D%5B0%5D%5Btitle%5D=parking&filters%5Bfeatures%5D%5B0%5D%5Bstatus%5D=false&filters%5Bfeatures%5D%5B1%5D%5Bid%5D=2&filters%5Bfeatures%5D%5B1%5D%5Bname%5D=%D8%A7%D9%86%D8%A8%D8%A7%D8%B1%DB%8C&filters%5Bfeatures%5D%5B1%5D%5Btitle%5D=warehouse&filters%5Bfeatures%5D%5B1%5D%5Bstatus%5D=false&filters%5Bfeatures%5D%5B2%5D%5Bid%5D=3&filters%5Bfeatures%5D%5B2%5D%5Bname%5D=%D8%A2%D8%B3%D8%A7%D9%86%D8%B3%D9%88%D8%B1&filters%5Bfeatures%5D%5B2%5D%5Btitle%5D=elevator&filters%5Bfeatures%5D%5B2%5D%5Bstatus%5D=false&filters%5Bfeatures%5D%5B3%5D%5Bid%5D=4&filters%5Bfeatures%5D%5B3%5D%5Bname%5D=%D8%A8%D8%A7%D9%84%DA%A9%D9%86&filters%5Bfeatures%5D%5B3%5D%5Btitle%5D=balcony&filters%5Bfeatures%5D%5B3%5D%5Bstatus%5D=false&filters%5Bcenter%5D%5Blat%5D=35.705262263265745&filters%5Bcenter%5D%5Blng%5D=51.43936157226563&filters%5Bzoom%5D=11&filters%5Bfoundation%5D%5Bmin%5D=&filters%5Bfoundation%5D%5Bmax%5D=&filters%5Bfoundation%5D%5BminRange%5D=&filters%5Bfoundation%5D%5BmaxRange%5D=&filters%5Bprice_rent%5D%5Bmin%5D=&filters%5Bprice_rent%5D%5Bmax%5D=&filters%5Bprice_rent%5D%5BminRange%5D=&filters%5Bprice_rent%5D%5BmaxRange%5D=&filters%5Brahn%5D%5Bmin%5D=&filters%5Brahn%5D%5Bmax%5D=&filters%5Brahn%5D%5BminRange%5D=&filters%5Brahn%5D%5BmaxRange%5D=&filters%5Bprice%5D%5Bmin%5D=&filters%5Bprice%5D%5Bmax%5D=&filters%5Bprice%5D%5BminRange%5D=&filters%5Bprice%5D%5BmaxRange%5D=&filters%5Bestate_age%5D%5Bmin%5D=0&filters%5Bestate_age%5D%5Bmax%5D=40&filters%5Bestate_age%5D%5BminRange%5D=0&filters%5Bestate_age%5D%5BmaxRange%5D=40&filters%5Brooms%5D%5Bmin%5D=0&filters%5Brooms%5D%5Bmax%5D=5&filters%5Brooms%5D%5BminRange%5D=0&filters%5Brooms%5D%5BmaxRange%5D=5&filters%5Bestate_floor%5D%5Bmin%5D=-1&filters%5Bestate_floor%5D%5Bmax%5D=20&filters%5Bestate_floor%5D%5BminRange%5D=-1&filters%5Bestate_floor%5D%5BmaxRange%5D=20&filters%5Bbuilding_floors%5D%5Bmin%5D=1&filters%5Bbuilding_floors%5D%5Bmax%5D=20&filters%5Bbuilding_floors%5D%5BminRange%5D=1&filters%5Bbuilding_floors%5D%5BmaxRange%5D=20&filters%5Bfloor_units%5D%5Bmin%5D=1&filters%5Bfloor_units%5D%5Bmax%5D=10&filters%5Bfloor_units%5D%5BminRange%5D=1&filters%5Bfloor_units%5D%5BmaxRange%5D=10&filters%5BleftBottom%5D%5Blat%5D=35.63107008009772&filters%5BleftBottom%5D%5Blng%5D=51.04248046875001&filters%5BrightTop%5D%5Blat%5D=35.779385463030465&filters%5BrightTop%5D%5Blng%5D=51.83624267578126&filters%5Bpolygon%5D=&filters%5BeasyFilters%5D=&page={page}"
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; _ga=GA1.2.215446283.1687630495; _gid=GA1.2.150769836.1687630495; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjJ1SWpJVnBucFkzMWVPRjRNN2ZsMWc9PSIsInZhbHVlIjoiaVMxcUlNMU5MWXZcL3VhVGV0TVwvN014bGRwN2t0dFRXVGVQRkRzRlpPcFBOZEVzXC9LZXppXC90MHg2WlhWMkhISkFrVHZYY0RLN25FZnBBU0xTSTNjVng1OGVyZXNzVjM4THBENU96d0dyKzFzPSIsIm1hYyI6ImZmMDNkNGI4NDk3Mzk4NzFiYTFjZmNmYjE2MjhiMWY3MjRmNDVkMGM3MzFhOWIyYjMzN2FjNTU0NDhhNWRiNzAifQ%3D%3D; bertinaAdvertiseCookie320=Sat Jun 24 2023 23:02:00 GMT+0430 (Iran Daylight Time); laravel_session=eyJpdiI6IjZKNXFOZHFWYzVaWFFaMmVXZmJxbXc9PSIsInZhbHVlIjoiWU5vNnNLV0N2RzFXTmRwUjBVb0U4TWJxeDFaZ3BldmRObzBEdFB3Q0pXSjhtamdTNEI4M2M2OVhHOGdGTDd2VCIsIm1hYyI6IjZhOGU1MGQ3YzAwZjVjOGNiMGU0NGU3NDA5OGRmN2UyMGMyYTkwYTVhNjliZDIzYTdjNTJjYzFkZWZhY2VlYTkifQ%3D%3D; laravel_session=eyJpdiI6IldyVXMzYU9SZkNjK1pFUlZNN3E2akE9PSIsInZhbHVlIjoiZmNJWlpITmZKK1RoUkdaNXhCMllPOHZEc250WWVVVkpYWmdSNExBVWswaVBEYXNsbHNCdTQ1ZFNsVGJLVDMxbCIsIm1hYyI6ImVkMTVjYWU2YmVkNGRiMGUwYTJkNmMxZWIyNTQ5NjQ3MGNjM2JlNmIyZGNjNzM0YzY5M2U2NDFkNzk4N2M2OTAifQ%3D%3D',
        'Origin': 'https://www.melkana.com',
        'Referer': 'https://www.melkana.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    response.raise_for_status()

    data = response.json()
    estate_list = data['estate_list']
    total_count = data['total_count']

    # Store data in CSV file
    with open('estates.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(estate_list[0].keys())
        for estate in estate_list:
            writer.writerow(estate.values())

    return total_count


if __name__ == '__main__':

    page = 1
    while True:
        total_estates = crawl_api(page)
        print(f"Total estates crawled: {total_estates} for page {page}")
        page += 1
        sleep(3)
        if total_estates == 0:
            break
