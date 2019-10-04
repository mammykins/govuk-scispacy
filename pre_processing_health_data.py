"""
    NLPre is a text (pre)-processing library that helps smooth some of the inconsistencies found in real-world data.
    Correcting for issues like random capitalization patterns, strange hyphenations,
    and abbreviations are essential parts of wrangling textual data but are often left to the user.

    This is derived from this repo: https://github.com/NIHOPA/NLPre

    This script has an example text taken from:
    https://www.gov.uk/drug-safety-update/vivaglobin-solution-for-subcutaneous-injection-rare-risk-of-thromboembolic-events

    Have the option to use custom dictionary:

    https://github.com/NIHOPA/NLPre/blob/master/nlpre/replace_from_dictionary.py
"""


from nlpre import titlecaps, dedash, identify_parenthetical_phrases
from nlpre import replace_acronyms, replace_from_dictionary
import nlpre
import logging
nlpre.logger.setLevel(logging.INFO)

text = """
    Vivaglobin 160 mg/mL (human normal immunoglobin solution for subcutaneous injection) is licensed as replacement
    therapy for adults and children with primary immunodeficiency syndromes, myeloma, or chronic lymphatic leukaemia.
    """
prefix = 'MeSH_'

print("The original text: ", {text})

ABBR = identify_parenthetical_phrases()(text)
parsers = [dedash(), titlecaps(), replace_acronyms(ABBR),
        replace_from_dictionary(prefix=prefix)]
for f in parsers:
    text = f(text)
logging.info(f"--- The words in the chosen dictionary are now prefixed with {prefix}")
print("The processed text: ", {text})

