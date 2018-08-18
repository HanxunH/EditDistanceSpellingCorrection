This README describes the data files for COMP90049 2018S2, Project 1. 
This archive contains six files, of which the dictionary and Wikipedia files
form the central data sources for this Project.  These files are described in
more detail below.


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

  - README.txt: the file that you are currently reading.

A careful examination of the Wikipedia data will reveal a few particularities:
  - 62 of the truly intended spellings are not present in the dictionary. The
    methods that we discuss in this subject cannot deal with this problem -
    consequently, the prediction will simply be wrong. We consider this
    acceptable, because no dictionary is ever truly complete, and increasing the
    size of the dictionary will mean that more misspellings are also present. On
    the bright side, it only affects a few entries. One example is
    "archeologists".

  - 322 of the misspellings are present in the dictionary. Most of the methods
    that we discuss in this subject will simply return the very same token -
    consequently, the prediction will simply be wrong. There are various
    reasons why this may occur: the author has accidentally mistyped a
    legitimate word (e.g. "planed"); the dictionary has rare words that are
    strictly possible, but not used in practice (e.g. "withing"); the
    dictionary contains the misspelled token as a variant (e.g. "bellweather").
    Ultimately, any attempt to reduce the size of the dictionary will mean that
    more correctly spelled entries are missing. 

  - British and American spellings are not used consistently (e.g.
    "acclimatization") and sometimes both variants are present in the
    corrections, but not in the dictionary ("manoeuvrable").

  - Some proper nouns are not present in the dictionary, like "queensland".
