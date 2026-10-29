f = open(r'c:\Users\alunos\Desktop\teste.txt','w')

for linha in range(1, 101):
    f.write(f'{linha}\n')

f.close()
