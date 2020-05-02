
# Encontrar o valor mais próximo de uma variavel
ints = [-9, 8, 2, -5, 7]
 
def closest_to_zero(ints, n):
    closest = n
    diffs = {value: abs(value - closest) for value in ints}

    return min(diffs.values())

print(closest_to_zero(ints, 0))
