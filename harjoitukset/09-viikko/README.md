# BandAPI - Harkkasofta

## Resurssit

- Bands
- Publications

## Endpointit

### Band

- Kaikki bändit GET /bands
    - kyselyparametri ?band_name=nimi, saadaan nimen bändi
- tietty bändi GET /bands/{id}
- luoda POST /bands
    - nimi (, perustamisvuosi)

### Publications

- Luominen POST /publications
    - nimi, bändi, julkaisuvuosi
- Kaikki julkaisut /publications
- Yksittäinen julkaisu /publications/{id}
- Poistaminen /publications/{id}


## Ajaminen

Tämä projekti käyttää [uv:ta](https://github.com/astral-sh/uv) ajamiseen.
