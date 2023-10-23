#Desafio -Crie um programa que:
# Pede por um nome de usuário e uma senha.
# Se ambos forem corretos, exibe uma mensagem de sucesso.
# Caso contrário , exibe uma mensagem de erro. A mensagem é diferente quando o usuário está incorreto, e quando a senha está incorreta
# O usuário / senha "corretos" podem ser definidos como variáveis dentro do próprio código.


usuario_certo = 'Anderson'
senha_certa = 123456

usuario= input('Digite um usuário: ')
senha= input('Digite uma senha: ')

if usuario == usuario_certo and senha == senha_certa:
  print('Usuário e Senha Correto! ')

if usuario != usuario_certo or senha != senha_certa:
  print('Usuário ou senha incorreto  !')  