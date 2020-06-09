import requests
from bs4 import BeautifulSoup

   
def make_url(seat):
    return "http://gseb.org/522lacigam/sci/" + seat[0:3] + "/" + seat[3:5] + "/" + seat + ".html"

def get_student_data(url):
    r = requests.get(url = url)
    soup = BeautifulSoup(r.text, 'html.parser')
    match = soup.find_all("tr")
    data = {}
    for m in match:
        t = m.find_all("span")
        isP = False
        for tt in t:
            ttt = tt.get_text()
            if(":" in ttt):
                sp = ttt.split(":")
                data[sp[0]] = sp[1]
                # print(ttt)
            else:
                isP = True
                break
    return data

def process_data(seat, f, fe):
    data = get_student_data(make_url(seat))
    f.write("\n" + data["Name"] + " - " + data['Seat No'])
    for k,v in data.items():
        fe.write("  " + k + "-" + v)
    fe.write("\n")

if __name__ == "__main__":
    f = open("output.txt", "a")
    fe = open("extra_output", "a")

    start = 111111
    end = 999999

    num = start
    while num <= end:
        x = "{:0>6d}".format(num)
        seat = "B" + x
        try:
            process_data(seat, f, fe)
            print(seat + " Done")
        except:
            print(seat + " Failed")
        num = num + 1
    f.close()
    fe.close()
    print("That's The End !")