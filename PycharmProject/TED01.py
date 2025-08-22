alturas = []
altura_homens = []
contador_mulheres = 0

for i in range(1, 16):
    print(f"\nPessoa {i}:")

    while True:
        entrada = input("Digite a altura (ex: 1,65): ").strip()
        entrada = entrada.replace(',', '.')  # Substitui vírgula por ponto

        try:
            altura = float(entrada)
            if altura <= 0:
                print("A altura deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Formato inválido. Digite no formato correto (ex: 1,65).")

    while True:
        genero = input("Digite o gênero (M para masculino, F para feminino): ").strip().upper()
        if genero not in ('M', 'F'):
            print("Entrada inválida. Digite apenas 'M' ou 'F'.")
        else:
            break

    alturas.append(altura)

    if genero == 'M':
        altura_homens.append(altura)
    elif genero == 'F':
        contador_mulheres += 1

maior_altura = max(alturas)
menor_altura = min(alturas)
media_altura_homens = sum(altura_homens) / len(altura_homens) if altura_homens else 0

print("\n--- Resultados ---")
print(f"Maior altura do grupo: {maior_altura:.2f} m")
print(f"Menor altura do grupo: {menor_altura:.2f} m")
print(f"Média de altura dos homens: {media_altura_homens:.2f} m")
print(f"Número de mulheres: {contador_mulheres}")
