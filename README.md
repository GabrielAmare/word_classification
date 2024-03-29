# Word classification

This project goal is to provide a strict classification of the meanings that a word can take in the french language.
Ideally, each atomic meaning a word can have should have a representation in this classification.

## Categories

- `NOM` : [Nom](/semantic/nouns.py#L15)
    - `NOM-COM` : [Nom commun](/semantic/nouns.py#L21)
    - `NOM-PRO` : [Nom propre](/semantic/nouns.py#L27)
- `ART` : [Article](/semantic/articles.py#L18)
    - `ART-DEF` : [Article défini](/semantic/articles.py#L24)
    - `ART-IND` : [Article indéfini](/semantic/articles.py#L30)
    - `ART-PAR` : [Article partitif](/semantic/articles.py#L36)
    - `ART-DEM` : [Article démonstratif](/semantic/articles.py#L42)
    - `ART-DEC` : [Article défini contracté](/semantic/articles.py#L48)
- `ADJ` : [Adjectif](/semantic/adjectives.py#L20)
    - `ADJ-QUA` : [Adjectif qualificatif](/semantic/adjectives.py#L26)
    - `ADJ-REL` : [Adjectif relatif](/semantic/adjectives.py#L32)
    - `ADJ-IND` : [Adjectif indéfini](/semantic/adjectives.py#L38) ([wikipédia](https://fr.wikipedia.org/wiki/Adjectif_ind%C3%A9fini))
    - `ADJ-NUM` : [Adjectif numéral](/semantic/adjectives.py#L44)
        - `ADJ-NUM-...-CAR` : [Adjectif numéral cardinal](/semantic/adjectives.py#L49)
        - `ADJ-NUM-...-ORD` : [Adjectif numéral ordinal](/semantic/adjectives.py#L55)
    - `ADJ-POS` [Adjectif possessif](/semantic/adjectives.py#L61)
- `PRO` : [Pronom](/semantic/pronouns.py#L24)
    - `PRO-PRE` : [Pronom personnel](/semantic/pronouns.py#L29)
    - `PRO-ADV` : [Pronom adverbial](/semantic/pronouns.py#L39)
    - `PRO-REL` : [Pronom relatif](/semantic/pronouns.py#L45)
        - `PRO-REL-INV` : [Pronom relatif invariable](/semantic/pronouns.py#L50)
        - `PRO-REL-VAR` : [Pronom relatif variable](/semantic/pronouns.py#L56)
    - `PRO-INT` : [Pronom interrogatif](/semantic/pronouns.py#L65)
    - `PRO-POS` : [Pronom possessif](/semantic/pronouns.py#L71)
    - `PRO-DEM` : [Pronom démonstratif](/semantic/pronouns.py#L85)
    - `PRO-IND` : [Pronom indéfini](/semantic/pronouns.py#L94)
    - `PRO-IMP` : [Pronom impersonnel](/semantic/pronouns.py#L103)
    - `PRO-REF` : [Pronom réfléchis](/semantic/pronouns.py#L109)
- `VER` : [Verbe](/semantic/verbs.py#L16)
    - `VER-INF` : [Verbe infinitif](/semantic/verbs.py#L24)
    - `VER-CON` : [Verbe conjugué](/semantic/verbs.py#L73)
- `ADV` : [Adverbe](/semantic/adverbs.py#L18)
    - `ADV-MAN` : [Adverbe de manière](/semantic/adverbs.py#L23)
    - `ADV-LIE` : [Adverbe de lieu](/semantic/adverbs.py#L29)
    - `ADV-TEM` : [Adverbe de temps](/semantic/adverbs.py#L35)
      ([www.dictionaire.lerobert.com](https://dictionnaire.lerobert.com/guide/adverbes-de-temps-et-d-aspect))
    - `ADV-LOG` : [Adverbe logique](/semantic/adverbs.py#L41)
    - `ADV-EXP` : [Adverbe explétif](/semantic/adverbs.py#L47)
      ([www.dictionnaire.lerobert.com](https://dictionnaire.lerobert.com/guide/adverbes-expletifs))
    - `ADV-NEG` : [Adverbe de négation](/semantic/adverbs.py#L53)
- `PRE` : [Préposition](/semantic/prepositions.py#L11) (some links about prepositions
  [www.francaisfacile.com](https://www.francaisfacile.com/exercices/exercice-francais-2/exercice-francais-34101.php))
- `CON` : [Conjonction](/semantic/conjunctions.py#L14)
    - `CON-COO` : [Conjonction de coordination](/semantic/conjunctions.py#L19)
    - `CON-SUB` : [Conjonction de subordination](/semantic/conjunctions.py#L25)
- `INT` : [Interjection](/semantic/interjections.py#L15)
    - `INT-STR` : [Interjection stricto-sensu](/semantic/interjections.py#L20)
    - `INT-ONO` : [Interjection onomatopée](/semantic/interjections.py#L26)
    - `INT-EMP` : [Interjection empruntée](/semantic/interjections.py#L32)

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
