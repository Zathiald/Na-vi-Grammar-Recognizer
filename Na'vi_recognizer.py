import nltk
from nltk import CFG


def na_vi_tokenize(sentence):
    """Define a custom tokenizer for Na'vi language."""
    # Convert the sentence to lowercase
    sentence = sentence.lower()

    replacements = {
        'menantang': 'me nantang',
        'pxenantang': 'pxe nantang',
        'aynantang': 'ay nantang',
        'atokirina\'': 'atokirina_',
        'na\'vi': 'na_vi'
    }
    for word, replacement in replacements.items():
        sentence = sentence.replace(word, replacement)
    return sentence.split()


# Define a context-free grammar for Na'vi language
na_vi_grammar = CFG.fromstring("""
    S -> NP VP
    NP -> N | Num N | N N
    VP -> V
    Num -> 'me' | 'pxe' | 'ay'
    N -> 'nantang' | 'tute' | 'ikran' | 'tsam' | 'kxetse' | 'atokirina_' | 'eywa' | 'na_vi' | 'kifkey' | 'palulukan' | 'toruk' | 'vitrautral' | 'skxawng' | 'tsmukan' | 'tsmuke'
    V -> 'hahaw' | 'yom' | 'taron' | 'tìng' | 'ean' | 'tìftia' | 'tìrol'
""")

# Create a parser with the defined grammar
na_vi_parser = nltk.ChartParser(na_vi_grammar)

# Input sentences to be parsed
sentences = [
    "Nantang hahaw", "Menantang hahaw", "Pxenantang hahaw", "Aynantang hahaw",
    "Tute yom", "Ikran taron", "Tsam kxetse tìng", "Atokirina' ean",
    "Eywa vitrautral tìftia", "Na'vi tìrol"
]

# Tokenize and parse each sentence using the custom tokenizer
for sentence in sentences:
    tokens = na_vi_tokenize(sentence)
    for tree in na_vi_parser.parse(tokens):
        tree.pretty_print()
