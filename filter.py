import sys
from processes import make_url
import webbrowser
import configs

filters = []
for i in range(1,len(sys.argv)):
    filters.append(sys.argv[i])

def process_file():
    output = {}
    f = open(configs.FILE_TO_SAVE_SEAT_NAME_PAIR)
    for line in f:
        values = line.split("-")
        if len(values) > 1:
            name = str(values[0]).strip()
            seat = str(values[1]).strip()
            output[name] = seat
    f.close()
    return output

def do_filter(input, token):
    output = {}
    for name,seat in input.items():
        if token.upper() in name:
            output[name] = seat
    return output

if __name__ == "__main__":
    output = process_file()
    for token in filters:
        output = do_filter(output, token)
        print("\n\n-----------------------------------------\n\n")
        print("Filter string - " + token + " - " + str(len(output)) + " Results")
        print("\n\n-----------------------------------------\n\n")
        for k in output.keys():
            print(k + " - " + output[k])
    print("\n\n------------------Final-----------------------\n\n")
    url = ""
    for k in output.keys():
        url = make_url(output[k])
        print(k + " - " + output[k] + " - " + url)
    if len(output) == 1:
        webbrowser.open(url)
