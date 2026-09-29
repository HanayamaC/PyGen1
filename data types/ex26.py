a, b = float(input()), float(input())

arith_mean = (a + b) / 2
geom_mean = (a * b) ** 0.5
harmonic_mean = (2 * a * b) / (a + b)
square_mean = ((a**2 + b**2) / 2) ** 0.5

print(arith_mean, geom_mean, harmonic_mean, square_mean, sep='\n')