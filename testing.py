readfile = open('words.txt', 'r')
writefile = open('words2.py', 'w')
for word in readfile:
    if len(word) == 6:
        writefile.write('"'+word.strip()+'", ')
