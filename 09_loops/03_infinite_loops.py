i = 1
while i<6:
    print(i)
    i + 1 

'''this program will run, but this will never update i,
which means that the value of i will always be one,
which in turn means that the loop keeps on executing,
the value of 111111 will keep on printing on the screen,
and this will keep on happening until my system crashes
or until something wrong goes...'''

'''hese types of mistakes can end up in infinite loops.
but sometimes infinite loops are very, very useful.


You can deliberately create an infinite loop by writing while true.'''
i = 1
while True:
    print(i)
    i = i + 1 # This will keep on printing 123456789 

#this is a infinite loop
#NOTE: DON'T CREATE INFINITE LOOPS BECAUSE EVENTUALLY YOUR SYSTEM WILL CRASH AND YOU DON'T WANT THAT.

