def ExceptionSimNao(msg):
    while True:
        try:
            res = int(input(msg))

            if res in [1, 2]:
                break
            else:
                print("\nDigite Valores Válidos\n")
        except:
            print("\nDigite Valores Válidos\n")

    return res


