
def h (unown):
    if unown < 0:
        return 0
    elif unown>= 0:
        return 1
def testh ():
    if h(-10) == 0:
        print "correct, h(-10) = 0"
    if h(-10**-15)== 0:
        print "correct, h(-10**-15) = 0"
    if h(0) == 1:
        print "correct, h(0) = 1"
    if h(10**-15):
        print "correct, h(10**-15) = 1"
    if h(10) == 1:
        print "correct, h(10) = 1"
    else:
        print "error"

testh()
