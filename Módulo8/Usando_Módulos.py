# Quando usar módulos
# 1º - separar funcionalidades relacionadas
# 2º - Não acoplar o seu código
# 3º - Não ter um arquivo gigante

from banco_de_dados import buscar_usuario
from configuracoes import senha

buscar_usuario()
print(senha)