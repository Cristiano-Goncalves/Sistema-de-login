#Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.


login="PEdro86"
senha="Drope68@"

tentativas=3

print("\n🎬 ❤️  😢 ✨ DORAMA LOVERS✨ 😢 ❤️  🎬")
while tentativas>=0:
    try:
        login_tentativa=input("\nDigite seu login: ")
        senha_tentativa=input("Dgite sua senha: ")

        if login_tentativa==login and senha_tentativa==senha:
            print("\n😊 Seja bem-vindo(a) 😊\n\n❤️  É um prazer tê-lo(a) aqui conosco ❤️\n")
            break
        else:
            if tentativas==1:
                print(f"\n⚠️  Login ou senha divergentes ⚠️\n\nVocê tem apenas {tentativas} tentativa")
            elif tentativas==0:
                print(" ")
            else:
                print(f"\n⚠️  Login ou senha divergentes ⚠️\n\nVocê tem {tentativas} tentativas")
            tentativas-=1
        
        if tentativas<0:
            for _ in range(1):
                print("🚫 ACESSO BLOQUEADO 🚫\n\nNúmero máximo de tentativas alcançado\n")
    except Exception as e:
        print(f"Ocorreu um erro: {e}. Tente novamente")