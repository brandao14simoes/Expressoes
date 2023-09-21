# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto
import re

# Funções
# findall search sub
# compile

# if re.search (r'teste', string):
#     print('Encontrado')
# else:
#     print('você escreveu')


string  = 'Este é um teste de expressões regulares'

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste','testa de ferro', string))


regexp = re.compile(r'Este')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('ABCD', string))