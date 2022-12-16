# Upustva za izradu izvještaja


## Preduvjeti

Instalirani Python verzije 3+.
Preporuka: koristiti [Conda](https://docs.conda.io/en/latest/) okruženje za instalaciju. Nakon toga je potrebno instalirati pakete čiji se popis i verzije nalaze u dokumentu `requirements.txt` u ovom direktoriju.

Dodatni linkovi:
- Conda instalacija: https://docs.conda.io/en/latest/miniconda.html
- matplotlib, paket za statičke vizualizacije, dokumentacija: https://matplotlib.org/
- numpy, paket za numeričku manipulaciju, dokumentacija: https://numpy.org/
- PyYAML, YAML sučelje, dokumentacija: https://pyyaml.org/
- scipy, set modula za znanstveno i tehničko računanje, dokumentacija: https://scipy.org/


## [Opcionalno] Instalacija Conda okruženja na Win OS

1. Skini odgovarajuću verziju Miniconda installer-a: https://docs.conda.io/en/latest/miniconda.html#windows-installers
2. Pokreni instalaciju i prati upute
3. Nakon što je Miniconda instalirana, možete koristiti naredbu `conda` za instaliranje bilo kojih drugih paketa i stvaranje okruženja, na primjer:
```shell
$ conda install numpy
...
$ conda create -n py3k anaconda python=3
...
```

## Korištenje
1. Napraviti adekvatne izmjene i nadopune `set_input.yaml` skriptu i spremiti. Pohraniti izmjenjenu verziju.
2. Pokrenuti `propagation_constant.py` skriptu
```shell
$ python propagation_constant.py
```
3. Pokrenuti `signal_distribution.py` skriptu
```shell
$ python signal_distribution.py
```
4. Pripadni vizuali `propagation_constant.py` i `signal_distribution.py` će biti pohranjeni u direktoriju `output` koji se nalazi unutar ovog direktorija.


## Izvještaj
Izvještaj mora sadržavati:
- opis mjerne opreme i postupka mjerenja
- tablicu mjerenja
- vizuale uz pripadne komentare
- kratki zaključak koji se odnosi na aproksimaciju i samu vrijednost propagacijske konstante


## Kontakt

Za sve nejasnoće i upite mailto:alojic00@fesb.hr.


## Licenca

[MIT](https://spdx.org/licenses/MIT.html)