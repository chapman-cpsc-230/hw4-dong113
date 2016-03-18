

def count_pairs (dna, pair):
    return dna.count(pair)    
       

deoxys= raw_input("enter dna strand")    
doduo= raw_input("enter a pair")

print count_pairs(deoxys, doduo)
