# loging - é um histórico do que aconteceu na aplicação

import logging
'''
NÍVEIS DE LOGGING:

debug - só estou informando informações para desenvolvedores:

info - só quero informar algo que está acontecendo no programa,
mas que não é um erro.

warnig - Quero relatar sobre algo que está acontecendo, 
possivelmente fora do esperado, porém ainda não é um erro, 
mas pode gerar um futuramente.

error - Um erro aconteceu na aplicação

critical - um erro com consequências graves acaba de ocororrer na aplicação
'''
logging.basicConfig(level=logging.DEBUG, filename='app.log',
                    filemode='a', format='%(levelname)s - %(message)s') # Setar o nível
logging.debug("logging no nível debug")
logging.info("logging no nível info")
logging.warning("loging no nível warning")
logging.error("loggin no nível error")
logging.critical("loggin no nível crítico")