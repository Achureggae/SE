def modus_tollens(P_implica_Q, no_Q):
    if P_implica_Q and not no_Q:
        return True
    else:
        return False

premisa_1 = input("Si llueve, ¿la calle estará mojada? (True/False): ").lower() == 'true'
premisa_2 = input("¿La calle está mojada?(True/False): ").lower() == 'true'

conclusion = modus_tollens(premisa_1, premisa_2)

print("\nPremisa 1: Si P entonces Q:", premisa_1)
print("Premisa 2: La negación de Q es verdadera:", premisa_2)
print("Conclusión: No está lloviendo:", conclusion)
