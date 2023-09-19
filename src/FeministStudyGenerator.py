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
$ python FeministStudyGenerator.py > FeministStudyGenerator.txt

"""
# In case of overflow on Jupyter notebook.
# jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10

# imports...
import itertools

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
,'Building'
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
,' queer'
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

# imports...
import itertools

# Create the products of all list items 
the_products = list(itertools.product(wordlist1, wordlist2, wordlist3, wordlist4, wordlist5))

# Print them out on separate lines
for element in the_products:
    print(element)
