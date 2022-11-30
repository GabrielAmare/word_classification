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
