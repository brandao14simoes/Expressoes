# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação

import re

# texto = '''
# <p> Frase </p> <p>Eita</p> <p>Fome</p> <div></div>
# '''

# print(re.findall(r'(<([dpiv]{1,3})>.+?<\/\1>)', texto))

# texto = '''
# <p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
# '''

# # cpf = 'a 147.852.963-12 a'
# # print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# # tags = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto)
# # tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', texto)
# # pprint(tags)

#print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', texto))

# # for tag in tags:
# #     um, dois, tres = tag
# #     print(tres)

cpf2 = '055.634.543-63'
cpf = '147.852.963-12'

print('CPF:', cpf2 if len(re.findall(r'[0-9]', cpf)) == 11 else f'{len(re.findall(r"[0-9]", cpf))} digitos')
print('CPF:', cpf if len(re.findall(r'[0-9]', cpf)) == 11 else f'{len(re.findall(r"[0-9]", cpf))} digitos')

print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf2 ))
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9a-zA-Z.-]+', cpf))
