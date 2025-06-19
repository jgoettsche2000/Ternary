
import sys
import re

yyfile = ''
yylineno = 0
yycolno = 0
yytext = ''
memes = set()
tokens = dict()

def setup():
    id = 256
    def getid():
        global id
        yield id
        id += 1
 
    tokens['True'] = ('TRUE', getid())
    tokens['False'] = ('FALSE', getid())
    tokens['Unknown'] = ('UNKNOWN', getid())
    # keywords
    tokens['when'] = ('WHEN', getid())
    # operators

    for key in tokens.keys():
        memes.add(key)

class Token():
    def __init__(self):
        global yytext, yycolno, yylineno, yyfile, tokens
        self.text = yytext
        self.lineno = yylineno
        self.colno = yycolno
        self.file = yyfile
        self.id = tokens[self.text]
        print('Token(' + yytext + ', ' + str(yylineno) + ', ' + str(yycolno) + ', ' + str(yyfile) + ')')

class DAO():
    def __init__(self, filename):
        self.filename = filename
        try:
            self.file = open(filename, 'r')
        except:
            quit("File error " + filename)

    def readfile(self):
        return self.file.read()
    
    def close(self):
        self.file.close()

class Lex():
    def __new__(self, *args): # Singleton
        if not hasattr(self, 'instance'):
            self.instance = super(Lex, self).__new__(self)
        return self.instance

    def __init__(self, *args):
#        self.file = None
        self.files = dict()
        self.contents = dict()
        self.filenames = args

#    def __call__(self, *args, **kwds):
#        if not hasattr(self, 'instance'):
#            self.instance = super(Lex, self).__new__(self)
#        return self.instance

    def openfiles(self):
        for filename in self.filenames:
            self.files[filename] = DAO(filename)

    def readContentsYYFile(self): # use a dictionary
        for f in self.files.keys():
            self.contents[f] = f.read()
            f.close()

    def yylex(self):
        global yycolno, yyfile, yylineno, yytext
        print(len(self.contents))
        input('##')
        for k in self.contents.keys():
            yyfile = 'file'
            pos = 0
            print(len(self.contents[k]))
            while pos < len(self.contents[k]):
                for t in tokens.keys():
                    m = re.search(t, inp[pos:])
                    if m.group() != '':
                        pos = m.span()[1]
                        yytext = m.group()
                        yycolno = m.span()[0]
                        yield Token()
                print(pos)
        exit(0)



def main():
    setup()
    lex = Lex(sys.argv)
    print(str(lex.filenames))
    print(len(lex.contents))
    input('...')
    t = lex.yylex()
    while t is not None:
        print('--')
        t = lex.yylex()

if __name__ == '__main__':
    main()