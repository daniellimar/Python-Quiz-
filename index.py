print("Seja muito bem vindo ao Sistema de Quiz")

answer_user = input("Quer começar? (S/N)")

if answer_user.lower() != "s":
    print("Até a próxima!")
    quit()

print("Começando...")

# Objeto contendo perguntas e respostas sobre linguagem de programação
quiz_questions = [
    {
        "pergunta": "Qual é a linguagem de programação mais popular atualmente?",
        "opcoes_resposta": {
            "1": "Python",
            "2": "Java",
            "3": "JavaScript",
            "4": "C"
        },
        "resposta_correta": "1"
    },
    {
        "pergunta": "Qual destes não é um tipo de dado em Python?",
        "opcoes_resposta": {
            "1": "Integer",
            "2": "String",
            "3": "Boolean",
            "4": "Float"
        },
        "resposta_correta": "4"
    },
    {
        "pergunta": "Qual é o símbolo usado para comentários em Python?",
        "opcoes_resposta": {
            "1": "//",
            "2": "#",
            "3": "/* */",
            "4": "--"
        },
        "resposta_correta": "2"
    },
    {
        "pergunta": "O que é um loop 'for' em Python?",
        "opcoes_resposta": {
            "1": "Uma estrutura de controle de fluxo",
            "2": "Um tipo de função",
            "3": "Uma lista de números aleatórios",
            "4": "Nenhuma das opções anteriores"
        },
        "resposta_correta": "1"
    }
]

# Inicializa o score do usuário
score = 0

# Exibindo as perguntas e recebendo respostas do usuário
for index, question in enumerate(quiz_questions, start=1):
    print(f"Pergunta {index}: {question['pergunta']}")
    print("Opções:")
    for option_num, option_text in question["opcoes_resposta"].items():
        print(f"{option_num}: {option_text}")
    resposta_usuario = input("Sua resposta (digite o número correspondente à opção): ")
    if resposta_usuario == question["resposta_correta"]:
        print("Resposta correta!")
        score += 1
    else:
        print("Resposta incorreta.")
    print()  # Adiciona uma linha em branco entre as perguntas

# Exibe o score final do usuário
print(f"Seu score final é: {score} de {len(quiz_questions)}")

