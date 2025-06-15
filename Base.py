import requests
import pickle
import time
import numpy as np
import datetime


tab_dict = {'Brand' : [],
            'Model' : [],
            'Variant' : [],
            'Year' : [],
            'Fuel' : [],
            'Transmission' : [],
            'KM driven' : [],
            'No. of Owners' : [],
            'Location' : [],
            'Price' : [],
            'Posted on' : []}



#-------------------------------------Headers Start----------------------------------------
payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'origin': 'https://www.olx.in',
  'priority': 'u=1, i',
  'referer': 'https://www.olx.in/en-in/maharashtra_g2001163/cars_c84?filter=make_eq_maruti-suzuki%2Cmodel_eq_maruti-suzuki-wagon-r',
  'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
  'x-panamera-fingerprint': 'e38488bd6d4525fb8445f78f27a4fe75#1749649865668'
}

#------------------------------------Headers End--------------------------------------------

for k in range(1,54):
  print(f"------------Page {k} Stared!-----------------")
  # url = "https://api.olx.in/relevance/v4/search?category=84&facet_limit=1000&location=2001163&location_facet_limit=40&make=maruti-suzuki&model=maruti-suzuki-wagon-r&nested-filters=%7B%22make%22%3A%5B%7B%22maruti-suzuki%22%3A%7B%22model%22%3A%5B%22maruti-suzuki-wagon-r%22%5D%7D%7D%5D%7D&platform=web-desktop&pttEnabled=true&relaxedFilters=true&size=40&user=016728549787647196&lang=en-IN"
  url = f"https://api.olx.in/relevance/v4/search?facet_limit=1000&nested-filters=%7B%22make%22%3A%5B%7B%22maruti-suzuki%22%3A%7B%22model%22%3A%5B%22maruti-suzuki-wagon-r%22%5D%7D%7D%5D%7D&pttEnabled=true&platform=web-desktop&size=40&location_facet_limit=40&relaxedFilters=true&location=2001163&model=maruti-suzuki-wagon-r&page={k}&category=84&lang=en-IN&make=maruti-suzuki&user=016728549787647196"

  response = requests.request("GET", url, headers=headers, data=payload)


  info_dict = response.json()
  # print(info_dict['data'][1]['title'])
  # print(info_dict['data'][1]['car_body_type'])
  # print(info_dict['data'][1]['price']['value']['display'])


  for n1,j in enumerate(info_dict['data']):
    price = j['price']['value']['raw']
    district = j['locations_resolved']['ADMIN_LEVEL_3_name']
    posted_on = j['created_at'].split('T')[0]

    # nxt_page_url = info_dict['metadata']['next_page_url']

    # print(info_dict['data'][1]['parameters'][0]['key_name'])

    d = {}
    for i in j['parameters']:
        param = i['key_name']
        value = i['value']

        d[param] = value

    d['Location'] = district
    d['Price'] = price
    d['Posted on'] = posted_on

    std_params = ['Brand','Model','Variant','Year','Fuel','Transmission','KM driven','No. of Owners','Location','Price']
    for i in tab_dict.keys():
      tab_dict[i].append(d.get(i,np.nan))
    print(f"Page {k} | Item no {n1+1} done!")

  print(f"------------Page {k} Completed!-----------------")





  waiting_period = np.random.randint(10,20)
  print(f"Waiting for {waiting_period} seconds before next request.")
  time.sleep(waiting_period)
print("Finished!")



with open (rf"Codes/database/tab_dict1.pkl" , "wb") as file:
   pickle.dump(obj=tab_dict,file=file)

print("File saved in <Codes/database/tab_dict.pkl>")



