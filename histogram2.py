 
    
import sys #import this so there are more printing options

def histogram2 (lugia) :
    for x in range(lugia):
        sys.stdout.write('*') #use sys.stdout.write instead of print so *** are on the same line
zapdos = raw_input("enter a title for the chart: ")
moltres = raw_input("enter a list of integers: ")
articuno = map(int, moltres.split())

print " n  | %s" % zapdos
print "---+------------------"

for y in range (len(articuno)):
    sys.stdout.write( " %d | " % articuno[y]) 
    histogram2(articuno[y])
    print
