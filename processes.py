import requests
from bs4 import BeautifulSoup
import configs
import sys

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
        print('May you press it or May The Internet Connection has broken... Bye Bye...')
        f.close()
        sys.exit()

    if 'Name' in data:
        save_basic_data(seat, data['Name'])
        print(seat + "  -   " + 'Success')
        return True
    else:
        print(seat + "  -   " + 'Not exists 404 !')
        return False

def save_basic_data(seat, name):
    f.write("\n" + name + " - " + seat)

def add_triling_zeros(num):
    return (configs.SEAT_NUMBER_DIGITS - len(str(num))) * '0' + str(num)

def digit_up(num, d):
    num = add_triling_zeros(num)
    print('\nMaking Juuuump !!!\n')
    if d <= 1:
        return int(num)+1
    if d > configs.MAX_NUM_CAN_BE_JUMPED:
        d = configs.MAX_NUM_CAN_BE_JUMPED
    try:
        return int(str(int(num[:-(d-1)]) + 1) + (d-1) * '0')
    except:
        print(num)
        print(d)
        print("Exception in Jump !!!")
        return -1

f = open(configs.FILE_TO_SAVE_SEAT_NAME_PAIR, "a")
