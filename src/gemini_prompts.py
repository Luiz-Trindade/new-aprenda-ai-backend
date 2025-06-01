topic_text_prompt = """
    Você é um gerador de textos educativos.
    Você gera textos com base em tópicos.

    Exemplo de texto com base no tópico "Direito Civil" de dificuldade "média":
    #####
        O Direito Civil é um dos principais ramos do direito privado, responsável por regular as relações jurídicas entre indivíduos, abrangendo direitos e obrigações nas esferas pessoais, familiares, patrimoniais e sucessórias. Ele está estruturado em vários tópicos, conforme o Código Civil brasileiro (Lei nº 10.406/2002), sendo os principais:

        **1. Parte Geral**

        Trata dos princípios e normas aplicáveis a todo o Direito Civil, incluindo:

        Pessoas (físicas e jurídicas): Capacidade civil, direitos da personalidade e extinção (como morte ou dissolução de empresas).

        Bens: Classificação (móveis, imóveis, tangíveis, intangíveis).

        Fatos jurídicos: Atores lícitos e ilícitos, negócios jurídicos (contratos, testamentos).

        **2. Direito das Obrigações**

        Disciplina os vínculos que geram deveres entre as partes, como:

        Contratos: Acordos entre particulares (compra e venda, locação, empréstimo).

        Responsabilidade civil: Indenização por danos (material ou moral).

        Pagamento e inadimplemento: Cumprimento ou descumprimento de obrigações.

        **3. Direito das Coisas (Direito Real)**

        Regula as relações sobre propriedade e posse de bens:

        Propriedade: Direito de usar, gozar e dispor de um bem.

        Posse: Detenção de um bem (com ou sem direito de propriedade).

        Direitos reais sobre coisas alheias: Usufruto, penhor, hipoteca.

        **4. Direito de Família**

        Normatiza as relações familiares e suas consequências jurídicas:

        Casamento, união estável e divórcio: Efeitos patrimoniais e pessoais.

        Filiação e alimentos: Vínculos parentais e dever de sustento.

        Guarda e tutela: Proteção de menores e incapazes.

        **5. Direito das Sucessões**

        Cuida da transmissão de bens e direitos após a morte:

        Herança: Partilha entre herdeiros legítimos ou testamentários.

        Testamento: Vontade do falecido na distribuição dos bens.

        Inventário e partilha: Processo judicial ou extrajudicial de divisão.

        **Conclusão**

        O Direito Civil é essencial para a organização da vida em sociedade, pois estabelece normas que regem desde o nascimento (personalidade jurídica) até a morte (sucessões), passando por relações patrimoniais, familiares e obrigacionais. Seus princípios visam equilibrar direitos individuais e coletivos, garantindo segurança jurídica e justiça nas relações privadas.

    #####

    Tópico:
    #####
        {topic}
    #####
        
    Dificuldade:
    #####
        {dificult}
    #####

    Gere apenas o texto.
""".strip()

topic_quiz_prompt = """
    Você é um gerador de questões educativas em formato JSON.

    Você deve gerar questões de objetivas com base em um tema e nível de dificuldade indicados.

    As questões serão dos tipos: 
    #####
        Múltipla escolha,
        Verdadeiro ou falso,
        Associação ou correspondência,
        Somatória de assertivas
    #####
    
    Cada questão deve seguir **exatamente** o seguinte formato:
    {{
        "text": "Pergunta aqui",
        "options": [
            {{ "text": "Alternativa 1", "correct": false }},
            {{ "text": "Alternativa 2", "correct": true }},
            {{ "text": "Alternativa 3", "correct": false }},
            {{ "text": "Alternativa 4", "correct": false }}
        ],
        "explanation": "Justificativa curta sobre por que a resposta correta está correta."
    }}

    Gere 10 questões nesse formato. Apenas uma das opções deve ser correta.

    ### Exemplo (tema: Inteligência Artificial, dificuldade: fácil):

    [
        {{
            "text": "O que é Inteligência Artificial?",
            "options": [
                {{ "text": "Um tipo de hardware especializado", "correct": false }},
                {{ "text": "Sistemas que imitam inteligência humana", "correct": true }},
                {{ "text": "Uma linguagem de programação", "correct": false }},
                {{ "text": "Um sistema operacional", "correct": false }}
            ],
            "explanation": "IA refere-se a sistemas que imitam funções cognitivas humanas."
        }},
        {{
            "text": "Qual é um exemplo de uso de IA no cotidiano?",
            "options": [
                {{ "text": "Chaves de fenda automáticas", "correct": false }},
                {{ "text": "Assistentes virtuais como Siri ou Alexa", "correct": true }},
                {{ "text": "Motores a combustão", "correct": false }},
                {{ "text": "Régua de cálculo", "correct": false }}
            ],
            "explanation": "Assistentes virtuais usam IA para compreender e responder comandos."
        }}
    ]

    ---

    Tema:
    #####
        {topic}
    #####

    Dificuldade:
    #####
        {dificult}
    #####

    Agora gere 10 questões em formato JSON com base nisso.
""".strip()
