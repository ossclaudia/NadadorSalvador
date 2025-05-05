import random
from capitulos import capitulo1, capitulo2, capitulo3, capitulo4, capitulo5, capitulo6, capitulo7, capitulo8, capitulo9

def iniciar_teste(perguntas, total_perguntas):
    random.shuffle(perguntas)  # Embaralha as perguntas
    acertos = 0

    for i in range(total_perguntas):
        print(perguntas[i]["pergunta"])
        for opcao in perguntas[i]["opcoes"]:
            print(opcao)

        resposta = input("Escolha uma opção (A, B, C ou D): ").strip().upper()

        if resposta == perguntas[i]["resposta_certa"]:
            print("Correto!\n")
            acertos += 1
        else:
            print(f"Errado! A resposta certa era: {perguntas[i]['resposta_certa']}\n")

    percentual_acertos = (acertos / total_perguntas) * 100
    print(f"Você acertou {acertos} de {total_perguntas} perguntas.")
    print(f"Sua percentagem de acertos é: {percentual_acertos:.2f}%\n")


def menu():
    while True:
        print("Bem-vindo ao teste!")
        print("1. Iniciar teste geral")
        print("2. Iniciar teste do capítulo 1")
        print("3. Iniciar teste do capítulo 2")
        print("4. Iniciar teste do capítulo 3")
        print("5. Iniciar teste do capítulo 4")
        print("6. Iniciar teste do capítulo 5")
        print("7. Iniciar teste do capítulo 6")
        print("8. Iniciar teste do capítulo 7")
        print("9. Iniciar teste do capítulo 8")
        print("10. Iniciar teste do capítulo 9")
        print("11. Sair")

        opcao = input("Escolhe uma opção: ").strip()

        if opcao in ["1", "2", "3", "4", "5", "6", "7", "8", "9","10"]:
            if opcao == "1":
                max_perguntas = len(capitulo1) + len(capitulo2) + len(capitulo3) + len(capitulo4) + len(capitulo5) + len(capitulo6) + len(capitulo7) + len(capitulo8) + len(capitulo9)
                print(f"Podes responder até {max_perguntas} perguntas no teste geral.")
                total_perguntas = int(input("Quantas perguntas queres responder?: "))
            elif opcao == "2":
                max_perguntas = len(capitulo1)
                print(f"Podes responder até {max_perguntas} perguntas no teste do capítulo 1.")
                total_perguntas = int(input("Quantas perguntas queres responder?: "))
            elif opcao == "3":
                max_perguntas = len(capitulo2)
                print(f"Podes responder até {max_perguntas} perguntas no teste do capítulo 2.")
                total_perguntas = int(input("Quantas perguntas queres responder?: "))
            elif opcao == "4":
                max_perguntas = len(capitulo3)
                print(f"Podes responder até {max_perguntas} perguntas no teste do capítulo 3.")
                total_perguntas = int(input("Quantas perguntas queres responder?: "))
            elif opcao == "5":
                max_perguntas = len(capitulo4)
                print(f"Podes responder até {max_perguntas} perguntas no teste do capítulo 4.")
                total_perguntas = int(input("Quantas perguntas queres responder?: "))
            elif opcao == "6":
                max_perguntas = len(capitulo5)
                print(f"Podes responder até {max_perguntas} perguntas no teste do capítulo 5.")
                total_perguntas = int(input("Quantas perguntas queres responder?: "))
            elif opcao == "7":  # Capítulo 6
                max_perguntas = len(capitulo6)
                print(f"Podes responder até {max_perguntas} perguntas no teste do capítulo 6.")
                total_perguntas = int(input("Quantas perguntas queres responder?: "))
            elif opcao == "8":  # Capítulo 7
                max_perguntas = len(capitulo7)
                print(f"Podes responder até {max_perguntas} perguntas no teste do capítulo 7.")
                total_perguntas = int(input("Quantas perguntas queres responder?: "))
            elif opcao == "9":  # Capítulo 8
                max_perguntas = len(capitulo8)
                print(f"Podes responder até {max_perguntas} perguntas no teste do capítulo 8.")
                total_perguntas = int(input("Quantas perguntas queres responder?: "))
            elif opcao == "10":  # Capítulo 9
                max_perguntas = len(capitulo9)
                print(f"Podes responder até {max_perguntas} perguntas no teste do capítulo 9.")
                total_perguntas = int(input("Quantas perguntas queres responder?: "))

            # Verifica se o número de perguntas solicitadas é válido
            if total_perguntas > max_perguntas:
                print(f"O número máximo de perguntas disponíveis é {max_perguntas}. Tenta novamente.")
                continue

            # Inicia o teste com as perguntas selecionadas
            if opcao == "1":
                todas_as_perguntas = capitulo1 + capitulo2 + capitulo3 + capitulo4 + capitulo5 + capitulo6 + capitulo7 + capitulo8 + capitulo9
                iniciar_teste(todas_as_perguntas, total_perguntas)
            elif opcao == "2":
                iniciar_teste(capitulo1, total_perguntas)
            elif opcao == "3":
                iniciar_teste(capitulo2, total_perguntas)
            elif opcao == "4":
                iniciar_teste(capitulo3, total_perguntas)
            elif opcao == "5":
                iniciar_teste(capitulo4, total_perguntas)
            elif opcao == "6":
                iniciar_teste(capitulo5, total_perguntas)
            elif opcao == "7":
                iniciar_teste(capitulo6, total_perguntas)
            elif opcao == "8":
                iniciar_teste(capitulo7, total_perguntas)
            elif opcao == "9":
                iniciar_teste(capitulo8, total_perguntas)
            elif opcao == "10":
                iniciar_teste(capitulo9, total_perguntas)
        elif opcao == "11":
            print("Saindo do programa. Até amanhã!")
            break
        else:
            print("Opção inválida. Tenta novamente.\n")

# Executa o menu
menu()