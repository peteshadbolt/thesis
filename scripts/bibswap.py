#!/usr/bin/python
import sys, os, anydbm, re

class bibentry:
    def __init__(self, index, raw):
        ''' an entry in the bitex bibliography '''
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

    def __str__(self): return '[%d] %s' % (self.index, self.tag)


class bibliography:
    def __init__(self, filename):
        ''' a bibliography'''
        self.filename=filename
        source=open(filename, 'r')
        self.entries=[]
        biblines=[]
        for line in source:
            biblines.append(line.strip())
            if line.strip()=='':
                self.entries.append(bibentry(len(self.entries), biblines))
                biblines=[]

    def lookup(self, tag):
        ''' check whether a tag is in the db'''
        for entry in self.entries:
            if tag==entry.tag: return True
        return False

    def __str__(self): return '\n'.join([entry.tag for entry in self.entries])


def extract_cites(filename):
    ''' parse a text file and extract citations '''
    target=open(filename).read()
    used=re.findall(r'\\cite{[^}]+}', target)
    used=map(lambda x: x[x.find('{')+1 : -1].split(','), used)
    used=reduce(lambda a,b: a+b, used)
    used=map(lambda x: x.strip(), used)
    return used


def load_database():
    root=os.path.split(__file__)[0]
    database_filename=os.path.join(root, 'bibswap.db')
    return anydbm.open(database_filename, 'c')

if __name__=='__main__':
    match_db=load_database()

    # if no arguments are provided, just print out the current database
    if len(sys.argv)==1: 
        print 'Current database:'
        mx=max([len(x) for x in match_db.keys()])
        for key, value in match_db.items():
            if key==value: 
                print 'Removing identity', key
                del match_db[key]
            print '%s %s -> %s' % (key, ' '*(mx-len(key)), value)

    # if only one argument is provided, treat it as a tex file which needs its tags replacing
    if len(sys.argv)==2: 
        texfile=sys.argv[1]
        texfile_source=open(texfile, 'r').read()
        for key, value in match_db.items():
            if key in texfile_source: print 'Found [%s], replacing with [%s]' % (key, value)
            texfile_source=texfile_source.replace(key, value)
        new_filename=texfile+'.cited'
        f=open(new_filename, 'w')
        f.write(texfile_source); f.close()
        print 'Wrote %s' % new_filename

    # if two arguments are provided, compare the two files and build new database entries
    if len(sys.argv)==3: 
        source, target=sys.argv[2], sys.argv[1]
        main_bibliography=bibliography(source)
        citations=extract_cites(target)

        # search for matches and ask the user where to put them in the database
        for citation in citations:
            print '\nARTICLE: ', citation

            # give option to skip
            if citation in match_db:
                question='[%s] is matched to [%s]. ' % (citation, match_db[citation])
                question+='Do you want to skip it [Y/n] ? ' 
                skip=raw_input(question)
                if not skip.startswith('n'): continue

            # if the citation is in the bibliography, always skip
            if main_bibliography.lookup(citation): 
                print '[%s] is already in the bibliography, ingnored.' % citation
                continue

            # choose sensible search terms
            search_terms=citation.split('-')
            search_terms=[search_terms[0], search_terms[-1]]
            best_bib=None
            most_matches=0

            # get all the matches
            for bib in main_bibliography.entries:
                matches=reduce(lambda a,b: a+b, map(bib.get_matches, search_terms))
                if len(matches)>0:
                    print str(bib)+'\n'+('\n'.join(map(lambda x: '\t'+x, matches)))
                if len(matches)>most_matches:
                    best_bib=bib
                    most_matches=len(matches)
            
            # ask the user which one to use
            user_choice=raw_input('Choose match [%s]: ' % best_bib.index)
            if user_choice=='': user_choice=best_bib.index
            match_db[citation]=main_bibliography.entries[int(user_choice)].tag
