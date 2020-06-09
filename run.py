from processes import process_seat_number, add_triling_zeros, digit_up
import configs
import sys

start = int('1' * configs.SEAT_NUMBER_DIGITS)
endC = int('9' * configs.SEAT_NUMBER_DIGITS)

array = []
for i in range(1,len(sys.argv)):
    array.append(sys.argv[i])

def smart_bruit_force():
    for prefix in array:
        counter = start
        faliCaount = 0
        digitToUp = 1
        while counter >= start and counter <= endC:
            seat = prefix + add_triling_zeros(counter)
            if process_seat_number(seat):
                counter = counter + 1
                faliCaount = 0
                digitToUp = 1
            else:
                faliCaount = faliCaount + 1
                counter = counter + 1
                if faliCaount > configs.JUMP_AFTER_FAULUERES_NUMBER:
                    faliCaount = 0
                    digitToUp = digitToUp + 1
                    counter = digit_up(counter, digitToUp)

if __name__ == "__main__":
    smart_bruit_force()

    
