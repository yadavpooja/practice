def clinic():
    print "You have just entered the clinic"
    print "Do u take lft or right"
    answer = raw_input("type left or right and hit 'enter'.").lower()
    if answer == "left" or answer == "l":
        print "this is emergency ward"
    elif answer == "right" or answer == "r":
        print "this is common room"
    elif answer == "o":
        print "you may move out"
    else:
        print "get out of here"
        clinic()

clinic()
