a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You won a charger")
    case 3:
            print("You won $3")
    case 6:
            print("You won a camera")
    case _:
            print("Better luck next time")

 '''Why do we have match case ? when we already had if else statements ?
in the versions of Python we didn't had this match case.
But this is a new edition since python 3.10, because it really adds convenience.
And python is all about convenience.'''


'''A lot of people use Python because it's a convenient 
programming language, and to  make it even more convenient,
they added match case because for some of the use cases, 
match case because for some of the use cases, match is really
very convenient.  '''