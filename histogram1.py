import sys

def histogram (staryu) :
    for x in range(staryu):
        sys.stdout.write('*')

x = raw_input("enter a list of positive integers")

pokemon = map(int, x.split())

for y in range(len(pokemon)):
    histogram(pokemon[y])
    print
