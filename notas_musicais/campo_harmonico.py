from notas_musicais.acordes import triade
from notas_musicais.escalas import escala


def _triade_na_escala(nota: str, notas_da_esscala):
    """
    Saber se as notas de um acorde estão na escala

    Args:
        nota: codcudnsic
        notas_da_escala: sdnisiudn

    Returns:
        daiosjdaoisjd

    Examples:
        >>> _triade_na_escala('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'C'

        >>> _triade_na_escala('D', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Dm'

        >>> _triade_na_escala('B', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'B°'
    """
    tonica, terca, quinta = triade(nota, 'maior')

    match_terca = terca in notas_da_esscala
    match_quinta = quinta in notas_da_esscala
    if match_terca and match_quinta:
        return tonica
    elif not match_terca and match_quinta:
        return f'{tonica}m'
    if not match_terca and not match_quinta:
        return f'{tonica}°'


def _converte_graus(cifra: str, grau: str) -> str:
    """
    Converte os graus relativo as cifras

    Args:
        cifra:Uma cifra de um acorde
        grau: Grau em forma maior

    Returns:
        Retorna o grau correto da cifra

    Examples:
        >>> _converte_graus('C', 'I')
        'I'

        >>> _converte_graus('Cm', 'I')
        'i'

        >>> _converte_graus('C°', 'I')
        'i°'
    """

    if 'm' in cifra:
        return grau.lower()
    elif '°' in cifra:
        return f'{grau.lower()}°'
    else:
        return grau


def campo_harmonico(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera um campo harmonico com base em uma tonica e uma tonalidade

    Args:
        tonica: Primeiro grau do campo harmonico
        tonalidade: Tonalidade para o campo. Exemplo: 'maior', 'menor' ...

    Returns:
        Um campo harmonico
    Examples:
        >>> campo_harmonico('c', 'maior')
        {'acordes': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°'], 'graus': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']}

        >>> campo_harmonico('c', 'menor')
        {'acordes': ['Cm', 'D°', 'D#', 'Fm', 'Gm', 'G#', 'A#'], 'graus': ['i', 'ii°', 'III', 'iv', 'v', 'VI', 'VII']}
    """

    notas, _graus = escala(tonica, tonalidade).values()
    acordes = [_triade_na_escala(nota, notas) for nota in notas]
    graus = [
        _converte_graus(acorde, grau) for acorde, grau in zip(acordes, _graus)
    ]

    return {'acordes': acordes, 'graus': graus}
