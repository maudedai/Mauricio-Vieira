import logging

  
logging.basicConfig(level=logging.DEBUG, filename='app.log',
                    filemode='a', format='%(levelname)s - %(message)s - %(asctime)s')
try:
    email = input("Digite seu e-mail: ")
    senha = int(input("Digite a sua senha bancária: "))
    if senha == 1234:
        logging.info(f"{email} entrou em sua conta bancária")
except ValueError as erro:
    print("Favor digitar apenas números!")
    logging.warning(erro)