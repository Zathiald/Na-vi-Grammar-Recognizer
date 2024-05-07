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

We need to see how this code works, first we will use the Natural Language Toolkit (NLTK) which, according to the python documentation is a " field that focuses on making natural human language usable by computer programs." (Python, 2023), so we can use this in order to detect the Na'vi language and have python recognize it.

Then in this section

```python
from nltk import CFG
```

We make use of the CFG class from NLTK which lets us create the context free grammar, then we will implement our CFG that we created before

```python
# Define a context-free grammar for Na'vi language
na_vi_grammar = CFG.fromstring("""
    S -> NP VP
    NP -> N | Num N | N N
    VP -> V
    Num -> 'me' | 'pxe' | 'ay'
    N -> 'nantang' | 'tute' | 'ikran' | 'tsam' | 'kxetse' | 'atokirina_' | 'eywa' | 'na_vi' | 'kifkey' | 'palulukan' | 'toruk' | 'vitrautral' | 'skxawng' | 'tsmukan' | 'tsmuke'
    V -> 'hahaw' | 'yom' | 'taron' | 'tìng' | 'ean' | 'tìftia' | 'tìrol'
""")
```

Then we create a parse which we will use in order to separate the words in the sentence and identify if they are valid

```python
# Create a parser with the defined grammar
na_vi_parser = nltk.ChartParser(na_vi_grammar)
```

Because of the nature of the Na'vi language we need to first set all the word in a lower case setting, separate the words from the number and convert the words with apostrophe such as Na'vi to a recognized word

```python
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
```

Now after we input the sentences we iterate through each of them and print the tree corresponding to it
```python
# Tokenize and parse each sentence using the custom tokenizer
for sentence in sentences:
    tokens = na_vi_tokenize(sentence)
    for tree in na_vi_parser.parse(tokens):
        tree.pretty_print()
```

Because this code is going through a lot of word in a table, the complexity would need to be analyzed as follows

1. **Tokenization:**

    a. **Iterating Through Words:** Tokenization involves going through each word in the sentence. With \( n \) words in the sentence, this step's time complexity is \( O(n) \).

    b. **Replacements:** For each word, replacements are made based on a dictionary. If there are \( m \) replacements, the time complexity for this step is \( O(m) \) per word.

    c. **Overall Tokenization Complexity:** Combining the complexities of iterating through words and replacements, tokenization's overall time complexity per sentence is \( O(n \cdot m) \).

2. **Parsing:**

    a. **Tokenized Sentence Length:** Parsing time depends on the length of the tokenized sentence, \( l \).

    b. **Grammar Complexity:** Parsing time also depends on the grammar's complexity, \( g \).

    c. **NLTK Parsing Algorithm:** NLTK's parsing algorithm typically runs in cubic time (\( O(l^3 \cdot g) \)). This includes building parsing tables and performing table-driven parsing.

    d. **Overall Parsing Complexity:** Therefore, parsing's overall time complexity per sentence is \( O(l^3 \cdot g) \).

So the overall complexity would be O(n⋅m)+O(l^3⋅g).

## Testing

As previously stated we used the 10 different sentences and after running the programm, we would get the following trees:

![Grammar2](https://github.com/Zathiald/Na-vi-Grammar-Recognizer/assets/111139805/16a0d828-7dc3-4563-a260-8c95afeb440e)

![Grammar 2_2](https://github.com/Zathiald/Na-vi-Grammar-Recognizer/assets/111139805/ebcb83a3-0f48-415e-a8e8-9583916c3883)

In order to test all this cases, there is a document labeled as Test_cases.py in which each sentence separately shows it's expected result

```python
sentence = ["Nantang hahaw"]

# Expected result
#          S       
#     _____|____    
#    NP         VP 
#    |          |   
#    N          V  
#    |          |   
# nantang     hahaw

sentence = ["Menantang hahaw"]

# Expected result

#            S
#       _____|______    
#      NP           VP 
#   ___|_____       |   
# Num        N      V  
#  |         |      |   
#  me     nantang hahaw

sentence = ["Pxenantang hahaw"]

# Expected result

#            S
#       _____|______    
#      NP           VP
#   ___|_____       |
# Num        N      V
#  |         |      |
# pxe     nantang hahaw

sentence = ["Aynantang hahaw"]

# Expected result

#           S
#       _____|______
#      NP           VP
#   ___|_____       |
# Num        N      V
#  |         |      |
#  ay     nantang hahaw


sentence = ["Tute yom"]

# Expected result

#       S
#   ____|___
#  NP       VP
#  |        |
#  N        V
#  |        |
# tute     yom

sentence = ["Ikran taron"]

# Expected result

#        S
#    ____|____
#   NP        VP
#   |         |
#   N         V
#   |         |
# ikran     taron

sentence = ["Tsam kxetse tìng"]

# Expected result

#            S
#        ____|_____
#       NP         VP
#   ____|____      |
#  N         N     V
#  |         |     |
# tsam     kxetse tìng

sentence = ["Atokirina' ean"]

# Expected result

#             S
#      _______|___
#     NP          VP
#     |           |
#     N           V
#     |           |
# atokirina_     ean

sentence = ["Eywa vitrautral tìftia"]

# Expected result

#              S
#        ______|________
#       NP              VP
#   ____|______         |
#  N           N        V
#  |           |        |
# eywa     vitrautral tìftia

sentence = ["Na'vi tìrol"]

# Expected result

#        S
#    ____|____
#   NP        VP
#   |         |
#   N         V
#   |         |
# na_vi     tìrol
```

## Other implementations

Another way that this CFG grammar could be implement could be through Nearley, Nearley is a " streaming parser with support for catching errors gracefully and providing all parsings for ambiguous grammars."(Npmjs) in the nearly packet in order to determine de gramar you would first need to determine an id in order to recognize it

```js
// Grammar in Nearley syntax (na_vi.ne)
@{%
const id = x => x[0];
%}
```

Then in order to implement the rules it would be similar to the python format but with an id in it, for example:

```js
# Define the rules
S -> NP VP {% id %}
NP -> N {% id %} | Num N {% id %} | N N {% id %}
VP -> V {% id %}
Num -> "me" {% id %} | "pxe" {% id %} | "ay" {% id %}
N -> "nantang" {% id %} | "tute" {% id %} | "ikran" {% id %} | "tsam" {% id %} | "kxetse" {% id %} | "atokirina_" {% id %} | "eywa" {% id %} | "na_vi" {% id %} | "kifkey" {% id %} | "palulukan" {% id %} | "toruk" {% id %} | "vitrautral" {% id %} | "skxawng" {% id %} | "tsmukan" {% id %} | "tsmuke" {% id %}
V -> "hahaw" {% id %} | "yom" {% id %} | "taron" {% id %} | "tìng" {% id %} | "ean" {% id %} | "tìftia" {% id %} | "tìrol" {% id %}
```

With this javascript the complexity of the code would't change, it would remain the same as in python, this because both require tokenization and parsing, the analysis would be similar to the one in the python code, so the complexity still is O(n⋅m)+O(l^3⋅g).


## References

npm: nearley. (n.d.). Npm. https://www.npmjs.com/package/nearley

Learn Na’vi. (2022, January 26). Na’vi Grammar | Learn na’Vi. Learn Na’vi | Learn the Na’vi Language. https://learnnavi.org/navi-grammar/

Python, R. (2023, October 21). Natural language processing with Python’s NLTK package. https://realpython.com/nltk-nlp-python/
