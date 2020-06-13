from processes import process_seat_number, add_triling_zeros, digit_up, get_batch_test_values, generate_one_random_number
import configs
import sys

start = int('1' * configs.SEAT_NUMBER_DIGITS)
endC = int('9' * configs.SEAT_NUMBER_DIGITS)
batch_marked = set()

array = []
for i in range(1,len(sys.argv)):
    array.append(sys.argv[i])

def process_batch(prefix, batch_4_num):
    batch = prefix + add_triling_zeros(batch_4_num, 4)
    print('Trying for batch ' + batch + '...')
    isSuccess = False
    for num in get_batch_test_values(configs.BATCH_SIZE):
        seat = batch + add_triling_zeros(num, 3)
        if process_seat_number(seat):
            isSuccess = True
            success_batch(batch, num)
            break
    print('End of batch ' + batch)      
    return isSuccess

def success_batch(batch, success_num):
    counter = success_num + 1
    failedCount = 0
    while counter < configs.BATCH_SIZE:
        seat = batch + add_triling_zeros(counter, 3)
        isSuccess = process_seat_number(seat)
        if not isSuccess:
            failedCount = failedCount + 1
        else:
            failedCount = 0
        if failedCount > configs.JUMP_AFTER_FAULUERES_NUMBER:
            break
        counter = counter + 1
    
    counter = success_num - 1
    failedCount = 0
    while counter >= 0:
        seat = batch + add_triling_zeros(counter, 3)
        isSuccess = process_seat_number(seat)
        if not isSuccess:
            failedCount = failedCount + 1
        else:
            failedCount = 0
        if failedCount > configs.JUMP_AFTER_FAULUERES_NUMBER:
            break
        counter = counter - 1

def process_whole_batch(prefix, batch_num):
    if batch_num in batch_marked:
        return 'exist'
    batch_marked.add(batch_num)
    isSuccess = process_batch(prefix, batch_num)
    if isSuccess:
        return 'success'
    else:
        return 'fail'

def run_call_batch(prefix):
    print('Procesing  prefix --- ' + prefix)
    for i in range(0, configs.NUM_OF_BATCHES):
        configs.batch_data[i] = False
    ###

    batch_num = configs.INITIAL_BATCH_NUMBER
    while True:

        if len(batch_marked) > 8000:
            break
        else:
            print('Done for ' + str(len(batch_marked)) + ' batches')

        output = process_whole_batch(prefix, batch_num)
        if output != 'success':
            batch_num = generate_one_random_number(1000, 9999)
        else:
            batch_num = batch_num + 1
            if batch_num > 9999:
                batch_num = 0

    
    ### Printing
    for i in configs.batch_data:
        if configs.batch_data[i]:
            print(str(i))
    print('End of Procesing  prefix --- ' + prefix)


if __name__ == "__main__":
    for prefix in array:
        run_call_batch(prefix)
# # #
