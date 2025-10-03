#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
##################################################
##  Generates bullshit research titles
##################################################
##  Thus goeth the Academic tenure Satan ballistic
##################################################
##  Author: Manne Laukkanen
##  Copyright (c) 2025,
##      Journals in pointless waste of tax-money to academic insanity
##  License: GNU 3.0
##  Status: prod
##################################################

Abstract:
    This study-generator operationalizes the interstitial nexus between
    discursive queerings of the algorithmic imaginary and the brute-force
    performativity of machinic textuality. By foregrounding repetition
    as both praxis and critique, the generator decenters authorial
    intentionality, thereby rendering visible the hidden structures of
    epistemic violence and playful semiotic collapse. The resulting
    10.8 million titles constitute a radical archive of counter-hegemonic
    futures — simultaneously stunning, brave, and stunning.

Usage:
    $ python3 FeministStudyGenerator.py
        Output is written to: FeministStudiesByTheMillions.txt
    $ No mousing. But if mousing, 666 entries:
        python3 FeministStudyGenerator.py --sample 666

    In case of overflow on Jupyter notebook:
        jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10

Citation:
    MLA:
        Laukkanen, Manne. *Feminist Study Generator: A Brute-Force Machine of Tenure Satan Gone Academic*. 
        Journal of Pointless Waste of Tax-Money to Academic Insanity, 2025.

    APA:
        Laukkanen, M. (2025). *Feminist Study Generator: Thus Goeth the Academic Tenure Satan Ballistic*. 
        Journal of Pointless Waste of Tax-Money to Academic Insanity. GNU Public License 3.0.

    Chicago:
        Laukkanen, Manne. “Feminist Study Generator: Thus Goeth the Academic Tenure Satan Ballistic.” 
        Journal of Pointless Waste of Tax-Money to Academic Insanity, 2025.

    IEEE:
        M. Laukkanen, *Feminist Study Generator: Thus Goeth the Academic Tenure Satan Ballistic*, 
        Journal of Pointless Waste of Tax-Money to Academic Insanity, 2025.

    BibTeX:
        @article{laukkanen2025feminist,
          author  = {Laukkanen, Manne},
          title   = {Feminist Study Generator: Thus Goeth the Academic Tenure Satan Ballistic},
          journal = {Journal of Pointless Waste of Tax-Money to Academic Insanity},
          year    = {2025},
          note    = {GNU 3.0 License. Stunning. And brave.}
        }
"""

# imports...
import itertools, sys, random

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
 ''
,'?'
,' (a manifesto)'
,' (an unfinished project)'
,' (towards liberation)'
,' (notes from the field)'
,' (in crisis)'
,' (and its discontents)'
,' (with apologies)'
,' (redux)'
]

# --- helper function(s) ---
def sample_titles(n=10):
    """Generate n random bullshit research titles."""
    samples = []
    for _ in range(n):
        base = "".join([
            random.choice(wordlist1),
            random.choice(wordlist2),
            random.choice(wordlist3),
            random.choice(wordlist4),
            random.choice(wordlist5)
        ]).strip()
        ending = random.choice(endings)
        samples.append(base + ending)
    return samples


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate millions of bullshit research titles, or just a few samples."
    )
    parser.add_argument(
        "--sample",
        type=int,
        default=0,
        help="If set, generate N random sample titles instead of the full brute-force run."
    )
    args = parser.parse_args()

    if args.sample > 0:
        # --- sample-only mode ---
        print(f"\n--- {args.sample} SAMPLE TITLES ---\n")
        for title in sample_titles(args.sample):
            print(" ", title)
    else:
        # --- full brute force run ---
        the_products = itertools.product(wordlist1, wordlist2, wordlist3, wordlist4, wordlist5)
        outfile = "FeministStudiesByTheMillions.txt"
        count = 0

        with open(outfile, "w", encoding="utf-8") as f:
            for element in the_products:
                base_title = "".join(element).strip()
                for e in endings:
                    f.write(base_title + e + "\n")
                    count += 1
                    if count % 100000 == 0:
                        print(f"{count:,} titles written...", file=sys.stderr)

        print(f"✅ Done! Wrote {count:,} titles to {outfile} 🚀. Stunning. And brave.", file=sys.stderr)
