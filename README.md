# Na-vi-Grammar-Recognizer
Evidence 2 of the course Implementation of Computational methods

## Language Context
The Na'vi language is a language created by USC Professor Paul Frommer. This is a constructed language, created for the 2009 film Avatar, produced by James Cameron.

The Na'vi language has been expanding ever since the film's release with it even having a hand sing version. This language is spoken by the Na'vi people who live on the moon of Pandora, the Na'vi language was designed to emulate the general aural feel and flavor of Polynesian languages, such as Maori, one of the three official languages of New Zealand.

## Language structure
In the Na'vi language the structure for the sentences follow a certain structure, unlike English in which word order marks the role of the noun. Na'vi uses noun cases, which means that the role of a noun or pronoun is marked by changing the ending of the word, for example:

- “Nantangìl frìp tutet”
- “Frìp tutet nantangìl”
- “Tutet nantangìl frìp” 

all mean the same thing: "a viperwolf bites the person"

Another rule to take into account is the fact that in order to distinguish between singular, dual, trial and plural, the number must be defined in the prefix, using the words

- Me : Two
- Pxe : Three
- Ay : Four or more

An example would be:

- Nantang hahaw. : One viperwolf are sleeping.
- Menantang hahaw. : Two viperwolves are sleeping.
- Pxenantang hahaw. : Three viperwolves are sleeping.
- Aynantang hahaw. : Four or more viperwolves are sleeping.

In which is the same sentence but the prefix determines the number.


## Context Free Grammar
Now that we understand the rules for the Na'vi grammar we need to create a tree rule for it, the word we are going to use for the grammar are:

# Nouns

- `nantang`: Viperwolf
- `tute`: Person
- `ikran`: Banshee, a type of flying creature
- `tsam`: War
- `kxetse`: Tail
- `atokirina'`: Wood sprite, a seed of the sacred tree
- `eywa`: The guiding force and deity of Pandora
- `na_vi`: The Na'vi people
- `kifkey`: Land or world
- `palulukan`: Thanator, a large, powerful animal
- `toruk`: Last Shadow, a giant flying predator
- `vitrautral`: Tree of Souls, a sacred place for the Na'vi
- `skxawng`: Moron
- `tsmukan`: Brother
- `tsmuke`: Sister

# Verbs

- `hahaw`: Laugh
- `yom`: Eat
- `taron`: Hunt
- `tìng`: Feel
- `ean`: Fly
- `tìftia`: Learn
- `tìrol`: Sing

So now that we have our nouns and verbs defined we can create the context free grammar, which will be as follows

```python
S -> NP VP
NP -> N | Num N | N N
VP -> V
Num -> 'me' | 'pxe' | 'ay'
N -> 'nantang' | 'tute' | 'ikran' | 'tsam' | 'kxetse' | 'atokirina_' | 'eywa' | 'na_vi' | 'kifkey' | 'palulukan' | 'toruk' | 'vitrautral' | 'skxawng' | 'tsmukan' | 'tsmuke'
V -> 'hahaw' | 'yom' | 'taron' | 'tìng' | 'ean' | 'tìftia' | 'tìrol'
```

Now let's explain section by section

1. S -> NP VP: This rule states that a sentence S consists of a noun phrase NP followed by a verb phrase VP.

2. NP -> N | Num N | N N: This rule defines a noun phrase NP. A noun phrase can be a single noun N, a number Num followed by a noun N, or two nouns N N.

3. VP -> V: This rule defines a verb phrase VP. In this grammar, a verb phrase consists of a single verb V.

4. Num -> 'me' | 'pxe' | 'ay': This rule defines the numbers Num in the Na’vi language.

5. N -> 'nantang' | 'tute' | 'ikran' | 'tsam' | 'kxetse' | 'atokirina_' | 'eywa' | 'na_vi' | 'kifkey' | 'palulukan' | 'toruk' | 'vitrautral' | 'skxawng' | 'tsmukan' | 'tsmuke': This rule defines the nouns N.

6. V -> 'hahaw' | 'yom' | 'taron' | 'tìng' | 'ean' | 'tìftia' | 'tìrol': This rule defines the verbs V.


## Implmentation 

In order to test this grammar we are going to try with this 10 different sentences

- Nantang hahaw. : One viperwolf are sleeping.
- Menantang hahaw. : Two viperwolves are sleeping.
- Pxenantang hahaw. : Three viperwolves are sleeping.
- Aynantang hahaw. : Four or more viperwolves are sleeping.
- Tute yom. : A person eats.
- Ikran taron. : A banshee hunts.
- Tsam kxetse tìng. : The enemy makes a tail.
- Atokirina' ean. : The woodsprite is blue.
- Eywa vitrautral tìftia. : Eywa learns from the tree of souls.
- Na'vi tìrol. : The Na’vi sing.

So now that we have our context free grammar, our words and sentences we are going to implement it in a python code

``` python
import nltk
from nltk import CFG

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

# Define a custom tokenizer for Na'vi language
def na_vi_tokenize(sentence):
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

# Input sentences to be parsed
sentences = ["Nantang hahaw", "Menantang hahaw", "Pxenantang hahaw", "Aynantang hahaw", "Tute yom", "Ikran taron", "Tsam kxetse tìng", "Atokirina' ean", "Eywa vitrautral tìftia", "Na'vi tìrol"]

# Tokenize and parse each sentence using the custom tokenizer
for sentence in sentences:
    tokens = na_vi_tokenize(sentence)
    for tree in na_vi_parser.parse(tokens):
        tree.pretty_print()
```

