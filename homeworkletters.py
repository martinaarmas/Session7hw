s= "acebdfz"

long = ""
solution = ""
previous = "a"
for character in s:
    if character >= previous:
        solution= solution+character
    else:
        if len(solution) > len(long):##is our chain bigger than the one we have?
            long = solution
        solution = character
        ##this breaks the chain
    previous = character ##if the chain is broken, the character becomes previous and keeps on reading the next one

print(long)
