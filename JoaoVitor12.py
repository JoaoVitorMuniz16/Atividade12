ano = int(input("digitar o ano"))
if ano % 100 != 0 and ano % 4 == 0 % 400 == 0:
    print("o ano bisexto:")
else:
    print("não é bisexto")