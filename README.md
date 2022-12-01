# Word classification

This project goal is to provide a strict classification of the meanings that a word can take in the french language.
Ideally, each atomic meaning a word can have should have a representation in this classification.

## Categories

- `NOM` : [Nom](/semantic/nouns.py#L15)
    - `NOM-COM` : [Nom commun](/semantic/nouns.py#L20)
    - `NOM-PRO` : [Nom propre](/semantic/nouns.py#L36)
- `ART` : [Article](/semantic/articles.py#L18)
    - `ART-DEF` : [Article défini](/semantic/articles.py#L23)
    - `ART-IND` : [Article indéfini](/semantic/articles.py#L39)
    - `ART-PAR` : [Article partitif](/semantic/articles.py#L54)
    - `ART-DEM` : [Article démonstratif](/semantic/articles.py#L70)
    - `ART-DEC` : [Article défini contracté](/semantic/articles.py#L86)
- `ADJ` : [Adjectif](/semantic/adjectives.py#L20)
    - `ADJ-QUA` : [Adjectif qualificatif](/semantic/adjectives.py#L25)
    - `ADJ-REL` : [Adjectif relatif](/semantic/adjectives.py#L41)
    - `ADJ-IND` : [Adjectif indéfini](/semantic/adjectives.py#L57)
    - `ADJ-NUM` : [Adjectif numéral](/semantic/adjectives.py#L74)
        - `ADJ-NUM-CAR` : [Adjectif numéral cardinal](/semantic/adjectives.py#L79)
        - `ADJ-NUM-ORD` : [Adjectif numéral ordinal](/semantic/adjectives.py#L102)
    - `ADJ-POS` [Adjectif possessif](/semantic/adjectives.py#L122)
- `PRO` : [Pronom](/semantic/pronouns.py#L22)
    - `PRO-PRE` : [Pronom personnel](/semantic/pronouns.py#L27)
    - `PRO-ADV` : [Pronom adverbial](/semantic/pronouns.py#L50)
    - `PRO-REL` : [Pronom relatif](/semantic/pronouns.py#L61)
      - `PRO-REL-INV` : [Pronom relatif invariable](/semantic/pronouns.py#L66)
      - `PRO-REL-VAR` : [Pronom relatif variable](/semantic/pronouns.py#L77)
    - `PRO-INT` : [Pronom interrogatif](/semantic/pronouns.py#L95)
    - `PRO-POS` : [Pronom possessif](/semantic/pronouns.py#L106)
    - `PRO-DEM` : [Pronom démonstratif](/semantic/pronouns.py#L122)
    - `PRO-IND` : [Pronom indéfini](/semantic/pronouns.py#L131)
    - `PRO-IMP` : [Pronom impersonnel](/semantic/pronouns.py#L140)
    - `PRO-REF` : [Pronom réfléchis](/semantic/pronouns.py#L150)
