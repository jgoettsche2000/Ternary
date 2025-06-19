import re
s = "[0-9]*"
d = {"[0-9]*" : "number", "[a-zA-Z]*" : "word"}
def main():
    i = ''
    while i != 'x':
        i = input('Type a string: ')
        for key in d.keys():
            t = re.search(key, i)
            if t.group() != '':
                print(t.string)
                print(t.group())
                print(t.span())       

main()
