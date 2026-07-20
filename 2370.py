n, t = map(int, input().split())
alunos = []

for _ in range(n):
    nome, h = input().split()
    alunos.append((int(h), nome))

# Ordena por habilidade decrescente
alunos.sort(reverse=True)

times = [[] for _ in range(t)]

# Distribui em rodízio
for i, (h, nome) in enumerate(alunos):
    times[i % t].append(nome)

# Imprime
for i in range(t):
    print(f"Time {i+1}")
    for nome in sorted(times[i]): # ordem alfabética
        print(nome)
    print() # linha em branco