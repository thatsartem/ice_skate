import requests
from time import sleep
from notify import notify

url = 'https://mf.technolab.com.ru/v1/place/dates-list?place_id=5e418445266a1d00198e4eee'

headers = {
    'Accept': 'application/json, text/plain, */*',
    'X-app-token': 'fd31f6e0-ddd7-44c4-bac2-3095a47ff1eb'
}
minutes = 0
while True:
    data_n = requests.get(
        url=url,
        headers=headers
    )    

    data = data_n.json()
    try:
        time_slot = data['rows'][0]['dates'][0]['time_slots']['2023-01-24T14:45:00.000Z']
        if time_slot<70:
            break
        print(time_slot, minutes)
        sleep(60)
        minutes+=1
    except Exception as e:
        notify("ALERT", e.__cause__)
        break

notify("TICKETS!!!", f'tickets left:{70-time_slot}')
