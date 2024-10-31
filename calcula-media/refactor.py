def calcular_media2(nota1, nota2, nota3):
    notas = [nota1, nota2, nota3]
    for nota in notas:
        if nota < 0 or nota > 10:
            raise ValueError("Nota deve estar entre 0 e 10")
    return sum(notas) / 3
