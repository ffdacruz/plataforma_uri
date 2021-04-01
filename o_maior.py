a,b,c = input().split()

a,b,c = int(a), int(b), int(c)

MaiorAB = int((a + b + abs(a - b)) / 2)
MaiorABC = int((MaiorAB + c + abs(MaiorAB - c)) / 2)

print('{0} eh o maior'.format(MaiorABC))