n1,n2,n3,n4 = input().split()
n1,n2,n3,n4 = float(n1), float(n2), float(n3), float(n4)
p1,p2,p3,p4 = 2,3,4,1

media = ((p1 * n1) + (p2 * n2) + (p3 * n3) + (p4 * n4)) / (p1+p2+p3+p4)

print('Media: {0:.1f}'.format(media))

if media >= 7.0:
    print('Aluno aprovado.')
elif media >= 5.0:
    print('Aluno em exame.')
    n_exame = float(input())
    print('Nota do exame: {0:.1f}'.format(n_exame))
    media_final = (n_exame + media) / 2.0
    if media_final > 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {0:.1f}'.format(media_final))
else:
    print('Aluno reprovado.')

