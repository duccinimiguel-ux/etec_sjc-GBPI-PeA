f = open(r'c:\Users\alunos\Desktop\teste.txt')

for linha in f.readlines():
    print(linha.strip())

f.close()
