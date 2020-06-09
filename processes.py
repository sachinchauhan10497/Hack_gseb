import requests
from bs4 import BeautifulSoup
import configs

def get_student_data(url):
    response = requests.get(url = url)
    soup = BeautifulSoup(response.text, 'html.parser')
    match = soup.find_all("tr")
    data = {}
    for m in match:
        t = m.find_all("span")
        for tt in t:
            ttt = tt.get_text()
            if(":" in ttt):
                sp = ttt.split(":")
                data['extra'] = []
                if sp[0] == 'Name':
                    data['Name'] = sp[1].strip()
                else:
                    data['extra'].append({sp[0]:sp[1]})
    return data

def make_url(seat):
    return configs.GSEB_PREFIX + configs.EXAM_CODE + '/' + configs.STD_CODE + '/' + seat[0:3] + '/' + seat[3:5] + '/' + seat + '.html'

def get_data_from_seat(seat):
    return get_student_data(make_url(seat))

def process_seat_number(seat):
    try:
        data = get_data_from_seat(seat)
    except:
        print('May The Internet Connection has broken...')
        return False
    if 'Name' in data:
        save_basic_data(seat, data['Name'])
        return True
    else:
        return False

def save_basic_data(seat, name):
    f.write("\n" + name + " - " + seat)

f = open(configs.FILE_TO_SAVE_SEAT_NAME_PAIR, "a")
