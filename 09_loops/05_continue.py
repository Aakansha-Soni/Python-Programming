for i in range(1, 20):
    if i == 10:
       continue #continue the loop for the next iteration here itself
    print(i) 

    # Output of this code will be 1 to 9, then 11 to 19.


#telling python interpreter that, actually want to continue this particular iteration of the loop 

    '''Ideally, when loop is running, it will run for all the iterations one, two, three....
    but continue says that instead of going back to the loop here, you go back to the loop now.

    So it's basically saying that whenever you encounter me, do not execute 
    whatever is below me just for this iteration. '''

'''EXPLAINATION: When the value of i is 10, you just go to the next iteration,
which is 11, and skip this statement or any statement which is below continue.

So Continue basically says continue the loop from here itself.'''
