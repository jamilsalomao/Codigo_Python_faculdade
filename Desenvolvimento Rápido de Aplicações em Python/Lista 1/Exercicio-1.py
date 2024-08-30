def mensagem_boas_vindas():

    nome_usuario = input("Por favor, digite seu nome: ")
    if nome_usuario:
      print("Bem-vindo(a),", nome_usuario, "! boa aula!")
    else:
      print("Seu nome não foi digitado!")
    return




mensagem_boas_vindas()