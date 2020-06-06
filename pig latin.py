a = input("Convert to pig latin: ")

def piglatin(string):
    for char in range(0, len(string)):
        b = string[char]
        if char == 0 and (b == "a" or b == "e" or b == "i" or b == "o" or b == "u"):
            string = string + "way"
            break
        elif b == "a" or b == "e" or b == "i" or b == "o" or b == "u":
            save = string[:char]
            string = string[char:] + save + "ay"
            break
    return string


print(piglatin(a))