import re

class bibentry:
    def __init__(self, index, raw):
        self.full=raw
        self.index=index
        self.tag=raw[0][raw[0].find('{')+1:]
        self.tag=self.tag.replace(',', '')
        self.tag=self.tag.strip()

    def get_matches(self, search):
        matches=[]
        for line in self.full:
            if search in line: 
                matches.append(line)
        return matches

    def __str__(self):
        s='[%d] %s' % (self.index, self.tag)
        return s

class bibliography:
    def __init__(self, filename):
        ''' load a bibliography'''
        self.filename=filename
        source=open(filename, 'r')
        self.entries=[]
        biblines=[]
        for line in source:
            biblines.append(line.strip())
            if line.strip()=='':
                self.entries.append(bibentry(len(self.entries), biblines))
                biblines=[]

    def __str__(self):
        s=''
        for entry in self.entries:
            s+=entry.tag+'\n'
        return s

def extract_cites(filename):
    ''' parse a text file and extract citations '''
    target=open(filename).read()
    used=re.findall(r'\\cite{[^}]+}', target)
    used=map(lambda x: x[x.find('{')+1 : -1].split(','), used)
    used=reduce(lambda a,b: a+b, used)
    used=map(lambda x: x.strip(), used)
    return used

