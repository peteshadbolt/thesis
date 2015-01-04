#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Attempt to convert Unicode accents to LaTeX """
import sys
from glob import glob

latexAccents = [
  [ u"à", "\\`a" ], # Grave accent
  [ u"è", "\\`e" ], [ u"ì", "\\`\\i" ], [ u"ò", "\\`o" ], [ u"ù", "\\`u" ], [ u"ỳ", "\\`y" ], [ u"À", "\\`A" ], [ u"È", "\\`E" ], [ u"Ì", "\\`\\I" ], [ u"Ò", "\\`O" ], [ u"Ù", "\\`U" ], [ u"Ỳ", "\\`Y" ], [ u"á", "\\'a" ], 
  [ u"é", "\\'e" ], [ u"í", "\\'\\i" ], [ u"ó", "\\'o" ], [ u"ú", "\\'u" ], [ u"ý", "\\'y" ], [ u"Á", "\\'A" ], [ u"É", "\\'E" ], [ u"Í", "\\'\\I" ], [ u"Ó", "\\'O" ], [ u"Ú", "\\'U" ], [ u"Ý", "\\'Y" ],
  [ u"â", "\\^a" ], # Circumflex
  [ u"ê", "\\^e" ], [ u"î", "\\^\\i" ], [ u"ô", "\\^o" ], [ u"û", "\\^u" ], [ u"ŷ", "\\^y" ], [ u"Â", "\\^A" ], [ u"Ê", "\\^E" ], [ u"Î", "\\^\\I" ], [ u"Ô", "\\^O" ], [ u"Û", "\\^U" ], [ u"Ŷ", "\\^Y" ],
  [ u"ä", "\\\"a" ],    # Umlaut or dieresis
  [ u"ë", "\\\"e" ], [ u"ï", "\\\"\\i" ], [ u"ö", "\\\"o" ], [ u"ü", "\\\"u" ], [ u"ÿ", "\\\"y" ], [ u"Ä", "\\\"A" ], [ u"Ë", "\\\"E" ], [ u"Ï", "\\\"\\I" ], [ u"Ö", "\\\"O" ], [ u"Ü", "\\\"U" ], [ u"Ÿ", "\\\"Y" ],
  [ u"ç", "\\c{c}" ],   # Cedilla
  [ u"Ç", "\\c{C}" ],
  [ u"œ", "{\\oe}" ],   # Ligatures
  [ u"Œ", "{\\OE}" ], [ u"æ", "{\\ae}" ], [ u"Æ", "{\\AE}" ], [ u"å", "{\\aa}" ], [ u"Å", "{\\AA}" ],
  [ u"‘", "`" ],    #Quotes
  [ u"’", "'" ], [ u"“", "``" ], [ u"”", "''" ], [ u"‚", "," ], [ u"„", ",," ],
]

infile=glob(sys.argv[1])[0]
outfile=sys.argv[2]
source=open(infile, 'ru')
output=open(outfile, 'w')
nfinds = 0 
finds=[]
for line in source:
    line=line
    for key, value in latexAccents:
        key=key.encode('utf-8')
        if key in line: 
            line=line.replace(key, value)
            nfinds+=1
            print 'Found a dodgy character:   %s' % key
    output.write(line)
output.close()
print 'Wrote %s (%d lines modified)' % (outfile, nfinds)
