def modus_ponens(P_implica_Q, P):
    if P_implica_Q and P:
        return True
    else:
        return False

premisa_1 = input("Si llueve la calle se moja (True/False): ").lower() == 'true'
premisa_2 = input("¿Está lloviendo? (True/False): ").lower() == 'true'

conclusion = modus_ponens(premisa_1, premisa_2)

print("\nPremisa 1: ¿Si llueve la calle se moja?:", premisa_1)
print("Premisa 2: ¿Está lloviendo?:", premisa_2)
print("Conclusión: La calle está mojada:", conclusion)
