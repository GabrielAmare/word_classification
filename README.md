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
- `VER` : [Verbe](/semantic/verbs.py#L16)
    - `VER-INF` : [Verbe infinitif](/semantic/verbs.py#L24)
    - `VER-CON` : [Verbe conjugué](/semantic/verbs.py#L73)
- `ADV` : [Adverbe](/semantic/adverbs.py#L20)
    - `ADV-MAN` : [Adverbe de manière](/semantic/adverbs.py#L25)
    - `ADV-LIE` : [Adverbe de lieu](/semantic/adverbs.py#L31)
    - `ADV-TEM` : [Adverbe de temps](/semantic/adverbs.py#L37)
    - `ADV-ASP` : [Adverbe d'aspect](/semantic/adverbs.py#L43)
    - `ADV-LOG` : [Adverbe logique](/semantic/adverbs.py#L49)
    - `ADV-EXP` : [Adverbe explétif](/semantic/adverbs.py#L55)
    - `ADV-ANA` : [Adverbe anaphorique](/semantic/adverbs.py#L61)
    - `ADV-NEG` : [Adverbe de négation](/semantic/adverbs.py#L67)
- `PRE` : [Préposition](/semantic/prepositions.py#L11)
- `CON` : [Conjonction](/semantic/conjunctions.py#L14)
    - `CON-COO` : [Conjonction de coordination](/semantic/conjunctions.py#L19)
    - `CON-SUB` : [Conjonction de subordination](/semantic/conjunctions.py#L24)

## Times

- `IND` : [Indicatif](/semantic/times.py#L15)
    - `IND-PR` : [Indicatif présent](/semantic/times.py#L54)
    - `IND-PC` : [Indicatif passé composé](/semantic/times.py#L55)
    - `IND-IM` : [Indicatif imparfait](/semantic/times.py#L56)
    - `IND-PP` : [Indicatif plus-que-parfait](/semantic/times.py#L57)
    - `IND-PS` : [Indicatif passé simple](/semantic/times.py#L58)
    - `IND-PA` : [Indicatif passé antérieur](/semantic/times.py#L59)
    - `IND-FS` : [Indicatif futur simple](/semantic/times.py#L60)
    - `IND-FA` : [Indicatif futur antérieur](/semantic/times.py#L61)
- `SUB` : [Subjonctif](/semantic/times.py#L16)
    - `SUB-PR` : [Subjonctif présent](/semantic/times.py#L63)
    - `SUB-PA` : [Subjonctif passé](/semantic/times.py#L64)
    - `SUB-IM` : [Subjonctif imparfait](/semantic/times.py#L65)
    - `SUB-PP` : [Subjonctif plus-que-parfait](/semantic/times.py#L66)
- `CON` : [Conditionnel](/semantic/times.py#L17)
    - `CON-PR` : [Conditionnel présent](/semantic/times.py#L68)
    - `CON-P1` : [Conditionnel passé (1ère forme)](/semantic/times.py#L69)
    - `CON-P2` : [Conditionnel passé (2ème forme)](/semantic/times.py#L70)
- `IMP` : [Impératif](/semantic/times.py#L18)
    - `IMP-PR` : [Impératif présent](/semantic/times.py#L72)
    - `IMP-PA` : [Impératif passé](/semantic/times.py#L73)
- `PAR` : [Participe](/semantic/times.py#L19)
    - `PAR-PR` : [Participe présent](/semantic/times.py#L75)
    - `PAR-PA` : [Participe passé](/semantic/times.py#L76)
- `INF` : [Infinitif](/semantic/times.py#L20)
    - `INF-PR` : [Infinitif présent](/semantic/times.py#L78)
    - `INF-PA` : [Infinitif passé](/semantic/times.py#L79)
- `GER` : [Gérondif](/semantic/times.py#L21)
    - `GER-PR` : [Gérondif présent](/semantic/times.py#L81)
    - `GER-PA` : [Gérondif passé](/semantic/times.py#L82)
