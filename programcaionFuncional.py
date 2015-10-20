__author__ = 'aferreiradominguez'


def saudar(ling):
    def saudar_es():
        print("Hola")

    def saudar_gl():
        print("Ola")

    def saudar_en():
        print("Hello")

    def saudar_fr():
        print("Bon jour")

    ling_func = {"es": saudar_es,
                 "gl": saudar_gl,
                 "en": saudar_en,
                 "fr": saudar_fr
                 }
    return ling_func[ling]


f = saudar("es")
f()
saudar("fr")()


# Iteraciones sobre listas de orden superior
def cuadrado(n):
    return n ** 2


def incrementa(n):
    return n + 1


lista = [2, 3, 4, 6, 8, 9]
lista2 = map(cuadrado, lista)
lista3 = map(incrementa, lista)

for elemento in lista2:
    print(elemento)

for elemento in lista3:
    print(elemento)


def e_par(n):
    return (n % 2.0 == 0)


lista4 = filter(e_par, lista)
for elemento in lista4:
    print(elemento)

lista5=filter(lambda n:n%2.0==0,lista)

for elemento in lista5:
    print(elemento)