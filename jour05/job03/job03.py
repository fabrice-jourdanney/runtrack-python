def afficher_tapis(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                print('\\', end='')
            elif i+j == n:
                print('/', end='')
            else:
                print('*', end='')
        print()
