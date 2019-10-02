

word = "hello"
subsets = []
for i in range(1, 2**len(word)): 
    binary = bin(i)[2:].zfill(len(word))
    subset = [] 
    for j in range(len(binary)): 
        if binary[j] == "1": 
           subset.append(word[j]) 
    subsets.append(subset) 
