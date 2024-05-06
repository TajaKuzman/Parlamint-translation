/home/tajak/miniconda3/envs/conda_env_python_9/lib/python3.9/site-packages/transformers/models/marian/tokenization_marian.py:197: UserWarning: Recommended: pip install sacremoses.
  warnings.warn("Recommended: pip install sacremoses.")
Extraction of the notes and translation started.
No. of files: 947.
Statistics before droping duplicates:



|        | tag   | type       | content   | xml:lang   |
|:-------|:------|:-----------|:----------|:-----------|
| count  | 28604 | 28604      | 28604     | 28604      |
| unique | 2     | 2          | 24275     | 1          |
| top    | note  | agendaItem | Punkt 0   | da         |
| freq   | 14302 | 14302      | 2026      | 28604      |


|    | tag   | type       | content      | xml:lang   |
|---:|:------|:-----------|:-------------|:-----------|
|  0 | note  | agendaItem | 2017-12-05-0 | da         |
|  1 | note  | agendaItem | 2017-12-05-1 | da         |
|  2 | note  | agendaItem | 2017-12-05-2 | da         |
|  3 | note  | agendaItem | 2017-12-05-3 | da         |
|  4 | note  | agendaItem | 2017-12-05-4 | da         |


Statistics for tags:

| tag   |   count |
|:------|--------:|
| note  |   14302 |
| head  |   14302 |


|                        |   count |
|:-----------------------|--------:|
| ('head', '')           |   14302 |
| ('note', 'agendaItem') |   14302 |
Most common notes:

| content                                                                  |   count |
|:-------------------------------------------------------------------------|--------:|
| Punkt 0                                                                  |    2026 |
| Besvarelse af oversendte spørgsmål til ministrene (spørgetid).           |     186 |
| Indstilling fra Udvalget til Valgs Prøvelse                              |      81 |
| Spørgetime med statsministeren.                                          |      36 |
| Spørgsmål om meddelelse af orlov til og indkaldelse af stedfortræder for |      35 |
| Udvidet spørgetime med statsministeren.                                  |      20 |
| Meddelelser fra formanden                                                |      13 |
| Forhandling af R 1: Om statsministerens åbningsredegørelse.              |      11 |
| Valg af stående udvalg m.v.                                              |      10 |
| Valg af formand.                                                         |      10 |
| Valg af 4 næstformænd.                                                   |      10 |
| Valg af 4 tingsekretærer.                                                |      10 |
| Spm.nr. US 15                                                            |       8 |
| Spm.nr. US 16                                                            |       8 |
| Spm.nr. US 7                                                             |       8 |
| Spm.nr. US 10                                                            |       8 |
| Spm.nr. US 13                                                            |       8 |
| Spm.nr. US 23                                                            |       8 |
| 2020-03-12-0                                                             |       8 |
| 2016-05-03-0                                                             |       8 |
Statistics after deduplication:

Number of words in the notes: 157883

|        | tag   | type       | content      | xml:lang   |      length |
|:-------|:------|:-----------|:-------------|:-----------|------------:|
| count  | 24275 | 24275      | 24275        | 24275      | 24275       |
| unique | 2     | 2          | 24275        | 1          |   nan       |
| top    | note  | agendaItem | 2017-12-05-0 | da         |   nan       |
| freq   | 12950 | 12950      | 1            | 24275      |   nan       |
| mean   | nan   | nan        | nan          | nan        |     6.50393 |
| std    | nan   | nan        | nan          | nan        |     6.59231 |
| min    | nan   | nan        | nan          | nan        |     1       |
| 25%    | nan   | nan        | nan          | nan        |     1       |
| 50%    | nan   | nan        | nan          | nan        |     1       |
| 75%    | nan   | nan        | nan          | nan        |    12       |
| max    | nan   | nan        | nan          | nan        |    27       |


|    | tag   | type       | content      | xml:lang   |   length |
|---:|:------|:-----------|:-------------|:-----------|---------:|
|  0 | note  | agendaItem | 2017-12-05-0 | da         |        1 |
|  1 | note  | agendaItem | 2017-12-05-1 | da         |        1 |
|  2 | note  | agendaItem | 2017-12-05-2 | da         |        1 |
|  3 | note  | agendaItem | 2017-12-05-3 | da         |        1 |
|  4 | note  | agendaItem | 2017-12-05-4 | da         |        1 |


Statistics for tags:

| tag   |   count |
|:------|--------:|
| note  |   12950 |
| head  |   11325 |


|                        |   count |
|:-----------------------|--------:|
| ('head', '')           |   11325 |
| ('note', 'agendaItem') |   12950 |
Translation started.
Translation completed. It took 77.99 minutes for 24275 instances for the entire process of extraction and translation.
|    | tag   | type       | content      | xml:lang   |   length | translation                 | corpus   |
|---:|:------|:-----------|:-------------|:-----------|---------:|:----------------------------|:---------|
|  0 | note  | agendaItem | 2017-12-05-0 | da         |        1 | This Regulation shall be    | DK       |
|  1 | note  | agendaItem | 2017-12-05-1 | da         |        1 | This Regulation shall enter | DK       |
|  2 | note  | agendaItem | 2017-12-05-2 | da         |        1 | This Regulation shall enter | DK       |
|  3 | note  | agendaItem | 2017-12-05-3 | da         |        1 | This Regulation shall enter | DK       |
|  4 | note  | agendaItem | 2017-12-05-4 | da         |        1 | This Regulation shall enter | DK       |




The file is saved as /home/tajak/Parlamint-translation/Note-translation/Final-data-CSV/ParlaMint-DK.notes.translated.ana.tsv
