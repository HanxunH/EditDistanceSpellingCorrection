A simple spelling correction system base on edit distance.   
This is project 1 of [Knowledge Technologies (COMP90049) Semester 2, 2018](https://handbook.unimelb.edu.au/subjects/comp90049), University of Melbourne.

### Environment
Python Verison: 2.7.10
External Packages
* [python-Levenshtein 0.12.0](https://github.com/ztane/python-Levenshtein)
pip install python-levenshtein
* [pyxDamerauLevenshtein 1.5](https://github.com/gfairchild/pyxDamerauLevenshtein)
pip install pyxDamerauLevenshtein
* [ngram 3.3.2](https://github.com/gpoulter/python-ngram)
pip install ngram
4. [UC Berkeley Pacman Project](http://ai.berkeley.edu/search.html) util.py
Included in this project.

### How to Use?
python coconutOrca.py

* Arguments
- Interactive Mode
-i
- Compare files Mode
-f follow by path of misspelled file and correct file
- Threshold
  -t follow by threshold integer
* Edit Distance
- -l Levenshtein
- -d Damerau-Levenshtein
- -ged Global Edit Distance
- -led Local Edit Distance
- -ngram N-Gram Distance
- -pynGram N-Gram Distance(ngram 3.3.2)
- -n follow by a number (For N-Gram Distance)

* Example
For sample_test_misspell.txt and sample_test_correct.txt using Levenshtein and Threshold equal to 1.
```sh
$ python coconutOrca.py -l -f 2018S2-90049P1-data/sample_test_misspell.txt 2018S2-90049P1-data/sample_test_correct.txt -t 1
```

### Data Set
- dict.txt: This is a list of approximately 370K English entries, which should
  comprise the dictionary for your approximate string search method(s). This
  dictionary is a slightly-altered version of the data from:
  https://github.com/dwyl/english-words
  The format of this file is one entry per line, in alphabetical order.
  You may use a different dictionary if you wish; if so, you should state
  the data source and justification in your report.

- wiki_misspell.txt: This is a list of 4453 tokens that have been identified
  as common errors made by Wikipedia editors. It has been scraped from the
  following page:
  https://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings
  The format of this file is one misspelling per line, in alphabetical
  order.
- wiki_correct.txt: This is a list of the truly intended spellings of the
  corresponding misspelled tokens from wiki_misspell.txt - again, one item
  per line.

- birkbeck_misspell.txt: This is a list of 34683 misspellings, comprising
  the "Birkbeck spelling error corpus". This is a machine-readable
  transcription of (hand-written) spelling mistakes made by schoolchildren,
  university students, and adult literacy students. The nature of these
  errors will probably be quite different to the typographical errors from
  Wikipedia.
  The corpus can be accessed through the Oxford Text Archive:
  http://ota.ox.ac.uk/
  This particular dataset is a slightly-altered version of the one hosted by
  Roger Mitton:
  https://www.dcs.bbk.ac.uk/~ROGER/corpora.html
- birkbeck_correct.txt: These are the corresponding corrections from
  birkbeck_misspell.txt - the format of these files is the same as the
  Wikipedia files; only the textual source is different.
