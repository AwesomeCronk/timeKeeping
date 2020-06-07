from clock import clock

def event():
    print('clock event with count {}'.format(t.count))

with clock(1, event, 5) as t:       #clock(frequency, event, count)     frequency is in hertz. event is any function with no paramaters. count is how many iterations to undergo. if count is None than cycle indefinitely.
    print('clock running')
    input('waiting for input. will exit after input is given.\n')       #hang the main thread in order to see the clock events