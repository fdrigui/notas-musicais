NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e de uma tonalidade.

    Args:
        tonica: Nota que será a tonica da escala
        tonalidade: Tonalidade da escala

    Returns:
        Um dicionário com as notas da escala e os graus

    Raises:
        ValueError: Caso a Tônica não seja uma nota válida

        KeyError: Caso Tonalidade não seja um valor válido

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'menor')
        {'notas': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()

    try:
        tonica_pos = NOTAS.index(tonica)
        intervalos = ESCALAS[tonalidade]
    except ValueError:
        raise ValueError(f'Essa nota não existe, tente uma dessas: {NOTAS}')
    except KeyError:
        raise KeyError(
            (
                'Essa escala não existe ou ainda não foi implementada. '
                f'Tente uma dessas: {list(ESCALAS.keys())}'
            )
        )

    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

    return {
        'notas': temp,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
