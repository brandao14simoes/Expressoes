# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+
# \d = dígito decimal
# | OU 
# [] - conjunto de carateres
# [^] - conjunto negado
# . Qualquer caracter, padrão dele não seleciona quebra de linha

import re

texto = '''
Felipe trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Catherine era o nome dela.


Foi um ano excelente na vida de Felipe. Teve 5 filhos, todos adultos atualmente.
maria, felipe hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Catherine, Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
Jã
'''

print(re.findall(r'Felipe|Cathe|Foi|ad..tos|o..ir', texto))
print(re.findall(r'Felipe|Cathe', texto))
print(re.findall(r'[Ff]elipe|[Cc]athe', texto))

# Expressão Range
print(re.findall(r'[a-z]elipe' ,texto))
print(re.findall(r'[A-Z]therine' ,texto))
print(re.findall(r'[A-Z]aria' ,texto))
print(re.findall(r'[a-zA-Z0-9]elipe|[a-zA-Z0-9]lipe' ,texto))
print(re.findall(r'FElipe|CaTHeRine' ,texto, flags=re.I))
