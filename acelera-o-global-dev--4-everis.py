import sys

N = int(sys.stdin.readline())
for _ in range(N) :
    qtd_senhas = int(sys.stdin.readline())
    senhas = list(map(int, input().split(" ")))
    senhas_ordenadas = sorted(senhas, reverse=True)
    ok = 0
    for i in range(len(senhas)):
        if (senhas[i] == senhas_ordenadas[i]):
            ok+=1
    print(ok)
