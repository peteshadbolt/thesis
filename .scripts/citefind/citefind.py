#!/usr/bin/python

import sys
import anydbm
import bibtex

# load everything
database_filename='./citefind.db'
source='/home/pete/physics/thesis/main.bib'
target='/home/pete/physics/thesis/chapter2/chapter2.tex'
main_bibliography=bibtex.bibliography(source)
match_db=anydbm.open(database_filename, 'c')
citations=bibtex.extract_cites(target)

# print out the match db
print 'Current database:'
for key, value in match_db.items():
    print '%s \t -> \t %s' % (key, value)

# search for matches
for citation in citations:
    print '\nARTICLE: ', citation

    # give option to skip
    if citation in match_db:
        question='[%s] is matched to [%s]. ' % (citation, match_db[citation])
        question+='Do you want to skip it [Y/n] ? ' 
        skip=raw_input(question)
        if not skip.startswith('n'): continue

    default=citation.split('-')
    default=[default[0], default[-1]]
    #search_terms=raw_input('Enter comma-separated search terms %s: ' % default).split(',')
    #if search_terms==['']: search_terms=default
    search_terms=default

    best_bib=None
    most_matches=0
    for bib in main_bibliography.entries:
        matches=[]
        for search in search_terms:
            matches+=bib.get_matches(search)
        if len(matches)>0:
            print bib
            print '\n'.join(map(lambda x: '\t'+x, matches))
        if len(matches)>most_matches:
            best_bib=bib
            most_matches=len(matches)
    
    user_choice=raw_input('Choose match [%s]: ' % best_bib.index)
    if user_choice=='': user_choice=best_bib.index
    try: 
        user_choice=int(user_choice)
        match_db[citation]=main_bibliography.entries[user_choice].tag
    except ValueError:
        print 'skipped'

