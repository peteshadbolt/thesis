#!/usr/bin/python
""" Find duplicates in a bibtex file """
from bibtexparser.bparser import BibTexParser
import re

def get_bib(filename):
    f=open(filename, 'r')
    bib=BibTexParser(f)
    cutoff=100
    return bib.get_entry_dict()

def get_citations(filename):
    f=open(filename, 'r')
    full=f.read()
    citations=re.findall(r'\\cite{[^}]*}', full)
    citations=map(lambda x: x[6:-1].split(','), citations)
    if len(citations)==0:
        print 'eh'
        return set()
    citations=reduce(lambda a,b:a+b, citations)
    citations=map(lambda x: x.strip(), citations)
    return set(citations)

def find_dupes(texfile, bibfile):
    citations=get_citations(texfile)
    bibliography=get_bib(bibfile)
    existing={}
    all_titles=[]
    skipped=[]
    for citation in citations:
        if not citation in bibliography: 
            continue

        bibentry=bibliography[citation]

        if not 'title' in bibentry:
            skipped.append(citation)
            continue

        title=bibentry['title'].replace('\n', ' ')
        all_titles.append(title)
        compressed_title=title.lower().strip().replace(' ', '_')

        if compressed_title in existing:
            print '### (%s, %s) looks like a duplicate\n %s' % (citation, existing[compressed_title], title)

        existing[compressed_title]=citation


    if len(skipped)>0: print 'Skipped the following keys:',  (', '.join(skipped))
    #print '\nFull list:'  #for x in sorted(all_titles): #print x

from glob import glob
bib_file='../../main.bib'
files=glob('../../**/*.tex')
#for file
#target_file='../../chapter7/walks.tex'

for target_file in files:
    print target_file
    find_dupes(target_file, bib_file)

