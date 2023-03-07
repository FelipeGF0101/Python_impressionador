"""
Blocos e identação
if dentro de if

Sempre que  usarmos o if ou qualquer outra estrutura no Python, devemos usar a identação para dizer para o programa onde a estrutura começa e onde ela termina.

Exemplo:
Digamos que você precisa criar um programa para um fundo de investimentos conseguir avalisar o resultado de uma carteira de ação e o quanto de taxa deverá ser pago.

A regra desse fundo de investimentos é:

* O fundo se compromete a entregar no mínimo 5% de retorno ao ano.
* Caso o fundo não consiga entregar os 5% de retorno, ele não pode cobrar taxa dos seus investidores.
* Caso o fundo consiga entregar mais de 5% de retorno, ele irá cobrar 2% de taxa de seus investidores.
* Caso o fundo consiga mais de 20% de retorno, ele irá cobrar 4% de taxa de seus investidores.


"""
meta = 0.05
taxa = 0
rendimento = 0.10

if rendimento > meta:
    if rendimento > 0.20:
        taxa = 0.04
        print(f"A taxa foi de {taxa}%")
    else:
        taxa = 0.02
        print(f"A taxa foi de {taxa}%")
else:
    taxa = 0
    print(f"A taxa foi de {taxa}%")