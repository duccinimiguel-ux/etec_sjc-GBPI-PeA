f = open(r'c:\Users\alunos\Desktop\mensagem.txt')
o = open(r'c:\Users\alunos\Desktop\cripto.txt', 'w')

for linha in f.readlines():
    for letra in linha:
        if letra in 'aeiou':
            o.write('*')
        else:
            o.write(letra)
f.close()
o.close()