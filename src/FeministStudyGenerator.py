##################################################
## {Generates bullshit research titles}
##################################################
## {Form Manne Only}
##################################################
## Author: {Manne Laukkanen}
## Copyright: Copyright {2023}, {Journals in pointless waste of tax-money to academic insanity}
## License: {GNU 3.0}
## Status: {prod}
##################################################
# -*- coding: utf-8 -*-

"""
Generates bullshit research titles

Usage:
$ python3 FeministStudyGenerator.py > FeministStudiesByTheHundredsOfThousands.txt

"""
# In case of overflow on Jupyter notebook.
# jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10

# imports...
import itertools
import random
import math
import sys

# List of words
wordlist1 = [
 'Imagining'
,'Visioning'
,'Envisioning'
,'Describing'
,'Queering'
,'Exploring'
,'Investigating'
,'Developing'
,'Deconstructing'
,'Imaging'
,'Reproducing'
,'Breaking down'
,'Building'
,'Unveiling'
,'Expressing'
,'Constructing'
,'Analyzing'
,'Shaping'
,'Discussing'
,'Juxtaposing'
,'Normalizing'
,'Revisiting'
,'Rethinking'
,'Reimagining'
,'Re-envisioning'
]

wordlist2 = [
 ' queerness:'
,' the family:'
,' bodies:'
,' homosexuality:'
,' the home:'
,' binaries:'
,' systems:'
,' oppression:'
,' tenderness:'
,' conflict:'
,' justice:'
,' feminisms:'
,' barriers:'
,' sexualities:'
,' motherhood:'
,' emotional labor:'
,' the voice:'
,' the woman:'
,' gender:'
,' violence:'
,' dichotomies:'
,' masculinities:'
,' femininities:'
,' sex:'
,' race:'
,' culture:'
]

wordlist3 = [
 ' towards a'
,' critiquing the'
,' building the'
,' creating a'
,' examining a'
,' analyzing the'
,' queering the'
,' dreaming a'
,' constructing the'
,' (de)constructing the'
,' imag(in)ing a'
,' shaping the'
]

wordlist4 = [
 ' new'
,' radical'
,' feminist'
,' political'
,' feminine'
,' subversive'
,' gendered'
,' sexual'
,' queer'
]

wordlist5 = [
 ' future'
,' sensuality'
,' sexuality'
,' politic'
,' society'
,' state'
,' identity'
,' experience'
,' critique'
,' homosexuality'
,' queerness'
,' agenda'
,' binary'
]

endings = [
 '','?',' (a manifesto)',' (an unfinished project)',
 ' (towards liberation)',' (notes from the field)',' (in crisis)',
 ' (and its discontents)',' (with apologies)',' (redux)'
]

# Cartesian product of all wordlists
the_products = itertools.product(wordlist1, wordlist2, wordlist3, wordlist4, wordlist5)

# Print them all with random absurd endings
for element in the_products:
    print("".join(element).strip() + random.choice(endings))

