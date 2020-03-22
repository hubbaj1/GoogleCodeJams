def parse_input():
    x = input()
    if x == -1:
        exit()
    return x

def flush_print(content):
    print(content, flush=True)

def generate_test(power, num_workers, trial):
    testcase = []*num_workers
    for i in range(num_workers):
        testcase.append((i%(power)>>trial)&1)
    return testcase

def broken_workers(working, num_workers, power):
    # temp = [0]*num_workers
    # for index in working:
    #     temp[index] = 1

    # result = ""
    # for i in range(num_workers):
    #     if(temp[i]==0):
    #         result+=str(i)+" "

    temp = 0
    result=""
    for i in range(num_workers):
        if(workers[temp] != i % power):
            result+=str(i)+" "
        elif(temp<len(workers)-1):
            temp += 1

    return result


for test_cases in range(int(input())):
    num_workers, num_broken, num_calls = map(int, input().strip().split())

    bitlength = num_broken.bit_length()
    power = 2**bitlength
    num_working = num_workers - num_broken
    workers = [0]*(num_working)

    for i in range(bitlength):

        testcase = "".join(map(str,generate_test(power, num_workers, i)))
        flush_print(testcase)

        response = list(map(int,input()))
        
        for j in range(num_working):
            workers[j] |= response[j]<<i

    #if workers[num_working -1 ] == 0:
    #    workers[num_working - 1] = num_workers-1

    result = broken_workers(workers, num_workers, power)
    flush_print(result)
    result = input()
    if(result == -1):
        exit(-1)

        








