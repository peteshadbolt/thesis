#!/bin/bash
# Using pdftk to cut out pages
echo 'cutting pages'
pdftk A=thesis.pdf cat A144-150 output ~/Desktop/cut.pdf
