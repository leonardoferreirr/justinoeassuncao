"""Textos do site da Justino & Assunção Sociedade de Advogados (o build.py importa daqui).

Regras dos textos: Provimento 205/2021 da OAB (sem promessa de resultado, sem preço, sem oferta de
consulta sem custo, sem depoimento de cliente), linguagem simples e sem travessão. As linhas marcadas
com "# [REVISAR: prazo legal]" trazem prazo ou número da lei: o advogado confere antes de publicar.

Esquema (o build depende destes nomes e formatos exatos):

ESCRITORIO = {
    "hero_h1": str,              # até 42 caracteres, fecha em 2 linhas no celular
    "hero_p": str,               # 1 ou 2 frases
    "seletor_h": str,            # pergunta curta acima dos atalhos de situação na capa (até 34 caracteres)
    "sobre_h2": str,
    "sobre": [str, str],         # 2 parágrafos curtos
    "manifesto": str,            # 35 a 55 palavras, lido palavra a palavra na rolagem
    "diferenciais": [(titulo, texto)] * 5,   # experiência, comprometimento, dedicação, estudo constante, técnica
    "areas_h2": str,
    "como_h2": str,
    "como": [(titulo, texto)] * 4,           # do primeiro contato ao acompanhamento
    "alcance_h2": str, "alcance_p": str,     # Uberlândia e todo o Brasil por processo eletrônico
    "faq": [(pergunta, resposta)] * 6,
    "final_h2": str, "final_p": str,
}

AREAS = [  # nesta ordem: familia, inventario, desportivo, marcas, previdenciario, civel
    {
        "slug": str, "nome": str, "curto": str,
        "gatilho": str,          # atalho da capa, na voz do cliente, até 34 caracteres
        "card": str,             # 1 frase para o índice de áreas da página central
        "seo_titulo": str,       # até 60 caracteres, com Uberlândia
        "seo_descricao": str,    # até 155 caracteres
        "hero_h1": str,          # até 44 caracteres
        "hero_p": str,
        "cta": str,              # rótulo do botão, até 26 caracteres
        "msg": str,              # mensagem que já vai escrita no WhatsApp, começa com "Olá, Justino & Assunção!"
        "situacoes_h2": str, "situacoes": [(titulo, texto)] * 6,
        "atuacao_h2": str, "atuacao": [(titulo, texto)] * 4,
        "documentos_h2": str, "documentos": [str] * 5 a 8,   # ou "" e [] quando não fizer sentido
        "faq": [(pergunta, resposta)] * 5,
        "final_h2": str,
    },
]
"""

ESCRITORIO = {
    "hero_h1": "Advocacia de família, sucessões e esporte",
    "hero_p": (
        "Você conta o que está acontecendo, nós estudamos o caso e conduzimos "
        "cada etapa com você. Em Uberlândia e, por processo eletrônico, em "
        "qualquer lugar do Brasil."
    ),
    "seletor_h": "Qual destas é a sua situação?",
    "sobre_h2": "Quem cuida do seu caso",
    "sobre": [
        "A Justino & Assunção Sociedade de Advogados é um escritório de "
        "Uberlândia fundado por dois sócios. Felipe Justino Andrade é "
        "especialista em Direito de Família e Sucessões. Eduardo Oliveira "
        "Assunção é pós-graduado na mesma área e membro da Comissão de Direito "
        "de Família e Sucessões da OAB/MG, Subseção de Uberlândia.",
        "Família e sucessões são o centro do trabalho, no cartório quando a lei "
        "permite ou na Justiça. O escritório tem também um departamento de "
        "Direito Desportivo e atua no registro de marcas e nas áreas "
        "previdenciária, civil, empresarial e eleitoral. Cada passo é explicado "
        "em palavras simples, sem juridiquês.",
    ],
    "manifesto": (
        "Ninguém procura um advogado num dia comum. Procura quando um casamento "
        "acaba, quando a família perde alguém, quando o INSS nega um benefício "
        "ou quando o contrato de um atleta chega ao fim. Nessa hora, você "
        "precisa de alguém que estude o caso, fale claro e seja honesto sobre o "
        "que pode ser feito."
    ),
    "diferenciais": [
        (
            "Experiência",
            "A prática diária em família e sucessões, no direito desportivo e nas "
            "outras áreas do escritório ajuda a enxergar os próximos passos e a "
            "preparar você para cada um deles.",
        ),
        (
            "Comprometimento",
            "Quando assumimos um caso, você sabe o que está sendo feito e por "
            "quê. Cada passo é explicado em palavras simples.",
        ),
        (
            "Dedicação",
            "Cada caso é estudado de perto: cada documento e cada prova são lidos "
            "antes de decidir o próximo passo.",
        ),
        (
            "Estudo constante",
            "A lei muda e o entendimento dos tribunais também. Acompanhamos essas "
            "mudanças, das regras dos cartórios à Lei Geral do Esporte, para que "
            "o seu caso use o que vale hoje.",
        ),
        (
            "Técnica",
            "Cada peça, contrato ou pedido é escrito para o seu caso, com base na "
            "lei e nas decisões dos tribunais, sem modelo pronto.",
        ),
    ],
    "areas_h2": "Em quais casos o escritório atua",
    "como_h2": "Como o seu caso é conduzido",
    "como": [
        (
            "Você conta o que aconteceu",
            "Por mensagem ou em uma conversa marcada, você explica a situação. "
            "Entendemos o que é urgente e se é um caso que o escritório atende.",
        ),
        (
            "Proposta por escrito",
            "Explicamos como vamos atuar e quais são os honorários. Tudo fica em "
            "contrato, assinado antes de o trabalho começar.",
        ),
        (
            "Estudo e atuação",
            "Com o contrato assinado, estudamos o caso a fundo e tomamos as "
            "providências no cartório, no INPI, no INSS ou na Justiça, começando "
            "pelas mais urgentes.",
        ),
        (
            "Acompanhamento",
            "Você é informado de cada movimentação importante, explicada em "
            "palavras simples, até o encerramento do caso.",
        ),
    ],
    "alcance_h2": "De Uberlândia para todo o Brasil",
    "alcance_p": (
        "O escritório fica na Av. Sacramento, no bairro Martins, em Uberlândia. "
        "Com o processo eletrônico, atuamos em qualquer lugar do Brasil. Os "
        "pedidos no INPI e no INSS também são feitos pela internet, e a conversa "
        "com você pode ser toda a distância."
    ),
    "faq": [
        (
            "Vocês atendem fora de Uberlândia?",
            "Sim. Quando o processo é eletrônico, atuamos em qualquer lugar do "
            "Brasil, e a conversa com você pode ser toda a distância. Se algum "
            "ato exigir presença, avisamos antes de começar.",
        ),
        (
            "Dá para resolver no cartório, sem processo?",
            "Em alguns casos, sim. Divórcio e inventário podem ser feitos no "
            "cartório, por escritura, quando há acordo e a lei permite. Mesmo no "
            "cartório, é obrigatório ter advogado.",
        ),
        (
            "Como são combinados os honorários?",
            "Depois de entender o seu caso, apresentamos a proposta de honorários "
            "por escrito. Tudo fica em contrato, assinado antes de o trabalho "
            "começar.",
        ),
        (
            "Vocês prometem resultado?",
            "Não. Quem decide é o juiz ou o órgão responsável, como o INSS ou o "
            "INPI, e a ética da advocacia proíbe prometer resultado. O nosso "
            "compromisso é com o trabalho: estudo do caso, técnica e "
            "acompanhamento em cada etapa.",
        ),
        (
            "O que eu conto fica em sigilo?",
            "Sim. O sigilo entre advogado e cliente é um dever profissional. O "
            "que você conta fica entre você e o escritório.",
        ),
        (
            "O que levar para a primeira conversa?",
            "Um resumo do que aconteceu e os documentos que você tiver. Na página "
            "de cada área há uma lista do que separar.",
        ),
    ],
    "final_h2": "Conte o que está acontecendo",
    "final_p": (
        "Mande uma mensagem com um resumo da situação e retornamos para entender "
        "o seu caso. Se já chegou uma citação ou uma carta do INSS, conte logo na "
        "mensagem, porque pode haver prazo correndo."
    ),
}

AREAS = [
    # 1. FAMÍLIA -------------------------------------------------------------
    {
        "slug": "familia",
        "nome": "Direito de Família",
        "curto": "Família",
        "gatilho": "Quero me divorciar ou pedir pensão",
        "card": (
            "Divórcio em cartório ou na Justiça, pensão alimentícia, guarda e "
            "convivência com os filhos e fim da união estável."
        ),
        "seo_titulo": "Advogado de família em Uberlândia | Justino & Assunção",
        "seo_descricao": (
            "Divórcio em cartório ou na Justiça, pensão alimentícia, guarda e "
            "convivência dos filhos em Uberlândia, com atenção e sigilo. Fale com "
            "o escritório."
        ),
        "hero_h1": "Divórcio, pensão e guarda dos filhos",
        "hero_p": (
            "Cuidamos do divórcio em cartório ou na Justiça, com ou sem acordo, da "
            "pensão para pedir, revisar ou cobrar e da guarda dos filhos. Você "
            "entende cada passo antes de decidir."
        ),
        "cta": "Conversar sobre o meu caso",
        "msg": "Olá, Justino & Assunção! Preciso de ajuda com divórcio, pensão ou guarda.",
        "situacoes_h2": "Quando a vida em família muda",
        "situacoes": [
            (
                "Queremos nos divorciar em cartório",
                "Com acordo e, em regra, sem filhos menores ou incapazes, o "
                "divórcio pode ser feito por escritura, sem processo. Preparamos a "
                "minuta, que é o texto da escritura, e acompanhamos a assinatura. "
                "Vale também para o fim da união estável.",
            ),
            (
                "Temos filhos menores e estamos de acordo",
                "Montamos o acordo sobre a partilha dos bens, a guarda, a "
                "convivência e a pensão dos filhos e acompanhamos o pedido até a "
                "homologação, que é a aprovação do acordo pelo juiz.",
            ),
            (
                "A outra pessoa não aceita o divórcio",
                "Ninguém é obrigado a continuar casado. Sem acordo, conduzimos o "
                "processo na Justiça e defendemos uma partilha justa dos bens e os "
                "interesses dos filhos.",
            ),
            (
                "Preciso pedir ou rever a pensão",
                "Pedimos os alimentos, nome que a lei dá à pensão, com base no que "
                "o filho precisa e no que o outro pode pagar. Se a renda ou a "
                "necessidade mudou, pedimos a revisão do valor.",
            ),
            (
                "A pensão está atrasada",
                "Cobramos os valores em atraso na Justiça. A lei permite bloquear "
                "contas e bens de quem deve e, em alguns casos, pedir a prisão "
                "civil do devedor.",
            ),
            (
                "Preciso definir a guarda dos meus filhos",
                "Definimos a guarda e os dias de convivência com cada um dos pais, "
                "por acordo ou na Justiça, tendo como centro o interesse da "
                "criança.",
            ),
        ],
        "atuacao_h2": "Como conduzimos o seu caso de família",
        "atuacao": [
            (
                "Escuta",
                "Você conta o que está acontecendo, no seu tempo. Identificamos o "
                "que é urgente, como a pensão dos filhos, e o que pode esperar.",
            ),
            (
                "Proposta e contrato",
                "Explicamos como vamos atuar e combinamos os honorários em contrato "
                "escrito, antes de começar.",
            ),
            (
                "Acordo ou processo",
                "Avaliamos com você se há espaço para acordo, no cartório ou na "
                "Justiça, que tende a ser mais rápido e menos desgastante. Se não "
                "houver, entramos com o pedido na Justiça.",
            ),
            (
                "Acompanhamento",
                "Acompanhamos a escritura ou o processo, com audiências, prazos e "
                "decisões, e você fica sabendo de cada passo importante.",
            ),
        ],
        "documentos_h2": "O que separar antes de conversar",
        "documentos": [
            "RG e CPF",
            "Certidão de casamento ou documento da união estável",
            "Certidão de nascimento dos filhos",
            "Comprovantes da sua renda e, se souber, da renda da outra parte",
            "Comprovantes dos gastos dos filhos: escola, saúde e alimentação",
            "Documentos dos bens do casal: imóveis, veículos e contas",
            "Acordo ou decisão anterior sobre pensão ou guarda, se houver",
            "Comprovantes dos pagamentos de pensão feitos ou em atraso",
        ],
        "faq": [
            (
                "O divórcio em cartório precisa de advogado?",
                "Sim. A lei exige advogado também no cartório. Ele prepara a "
                "minuta, confere os documentos e acompanha a assinatura da "
                "escritura. O casal pode ter um advogado só, se estiver de acordo.",
            ),
            (
                "Preciso esperar o divórcio para pedir pensão?",
                "Não. A pensão dos filhos pode ser pedida a qualquer momento, "
                "antes, durante ou depois do divórcio. O juiz pode fixar um valor "
                "provisório já no início do processo.",
            ),
            (
                "Como fica a divisão dos bens?",
                "Depende do regime de bens do casamento ou da união estável. Na "
                "comunhão parcial, o regime mais comum, em regra se divide o que "
                "foi comprado durante a união. Analisamos o seu caso para defender "
                "uma partilha justa.",
            ),
            (
                "Moro em outra cidade. Vocês podem me atender?",
                "Sim. Conversamos com você a distância e, quando o processo é "
                "eletrônico, atuamos em qualquer lugar do Brasil. Se algum ato "
                "exigir presença, avisamos antes de começar.",
            ),
            (
                "Como são combinados os honorários?",
                "Depois de entender o caso, apresentamos a proposta por escrito. O "
                "contrato descreve o que está incluído, como o divórcio, a partilha "
                "dos bens ou a pensão.",
            ),
        ],
        "final_h2": "Conte o que está acontecendo na sua família",
    },
    # 2. INVENTÁRIO ----------------------------------------------------------
    {
        "slug": "inventario",
        "nome": "Inventário e Sucessões",
        "curto": "Inventário",
        "gatilho": "Preciso fazer um inventário",
        "card": (
            "Inventário em cartório ou na Justiça e partilha de bens, representando "
            "todos os herdeiros ou só uma parte deles."
        ),
        "seo_titulo": "Advogado de inventário em Uberlândia | Justino & Assunção",
        "seo_descricao": (
            "Inventário em cartório ou judicial e partilha de bens em Uberlândia, "
            "para todos os herdeiros ou só uma parte, com ou sem acordo. Fale com o "
            "escritório."
        ),
        "hero_h1": "Inventário em cartório ou na Justiça",
        "hero_p": (
            "Cuidamos do inventário e da partilha, que é a divisão dos bens de quem "
            "faleceu, com ou sem acordo entre os herdeiros. A família entende cada "
            "etapa e sabe o que falta para terminar."
        ),
        "cta": "Falar sobre o inventário",
        "msg": "Olá, Justino & Assunção! Preciso de ajuda com um inventário.",
        "situacoes_h2": "Quando a família precisa dividir os bens",
        "situacoes": [
            (
                "Um familiar faleceu e deixou bens",
                "Levantamos quem são os herdeiros e quais bens existem, e indicamos "
                "o caminho possível: inventário em cartório ou na Justiça.",
            ),
            (
                "Os herdeiros estão de acordo",
                "Se todos são maiores, capazes e estão de acordo, em regra o "
                "inventário pode ser feito em cartório, por escritura, sem processo "
                "na Justiça. Conduzimos tudo até a divisão dos bens.",
            ),
            (
                "A família não se entende sobre a divisão",
                "Sem acordo, o inventário vai para a Justiça. Representamos você no "
                "processo e defendemos a sua parte na herança, abrindo espaço para "
                "acordo quando ele for possível.",
            ),
            (
                "O inventário nunca foi aberto",
                "Abrimos inventários atrasados, mesmo de muitos anos atrás. O "
                "atraso pode gerar multa no imposto sobre a herança, então vale "
                "resolver logo.",
            ),
            (
                "Preciso vender um bem de quem faleceu",
                "Em regra, um bem que ainda está no nome de quem faleceu só pode "
                "ser vendido com autorização do juiz, chamada alvará, ou depois da "
                "partilha. Cuidamos desse pedido.",
            ),
            (
                "Quero fazer um testamento",
                "Ajudamos você a fazer o testamento dentro da lei, deixando claro "
                "como os bens serão divididos e reduzindo dúvidas para a família "
                "no futuro.",
            ),
        ],
        "atuacao_h2": "Como cuidamos do inventário",
        "atuacao": [
            (
                "Primeira conversa",
                "Você conta quem faleceu, quem são os herdeiros e quais bens "
                "existem. Com isso, vemos se o caminho é o cartório ou a Justiça.",
            ),
            (
                "Proposta e contrato",
                "Apresentamos os honorários e o que está incluído no trabalho. Tudo "
                "fica em contrato escrito, assinado antes de começar.",
            ),
            (
                "Documentos e imposto",
                "Reunimos certidões e documentos dos bens e cuidamos da declaração "
                "do ITCMD, o imposto sobre a herança, necessário para concluir o "
                "inventário.",
            ),
            (
                "Até a partilha",
                "Acompanhamos a escritura no cartório ou o processo na Justiça até "
                "a divisão dos bens, com a família informada em cada etapa.",
            ),
        ],
        "documentos_h2": "O que separar para a primeira conversa",
        "documentos": [
            "Certidão de óbito",
            "RG e CPF de quem faleceu e de cada herdeiro",
            "Certidão de casamento ou documento de união estável de quem faleceu",
            "Certidões de nascimento ou de casamento dos herdeiros",
            "Matrícula atualizada dos imóveis, que é o registro do imóvel no cartório",
            "Documentos de veículos e extratos de contas e investimentos",
            "Testamento, se existir",
            "Lista das dívidas deixadas, se houver",
        ],
        "faq": [
            (
                "Qual a diferença entre inventário em cartório e na Justiça?",
                "No cartório, o inventário é feito por escritura, quando os "
                "herdeiros são maiores, capazes e estão de acordo. Na Justiça, ele "
                "vira um processo, necessário quando não há acordo ou em outras "
                "situações previstas em lei. Nos dois casos, é obrigatório ter "
                "advogado.",
            ),
            (
                "Existe prazo para abrir o inventário?",
                "A lei prevê a abertura em até 2 meses depois do falecimento. "  # [REVISAR: prazo legal]
                "Depois disso o inventário ainda pode ser feito, mas o estado pode "
                "cobrar multa sobre o imposto.",
            ),
            (
                "Vocês representam todos os herdeiros?",
                "Depende do que a família preferir. Podemos representar todos os "
                "herdeiros juntos, quando há acordo, ou só uma parte deles, quando "
                "cada lado quer ter o próprio advogado.",
            ),
            (
                "Os herdeiros moram em cidades diferentes. Dá para fazer?",
                "Sim. Conversamos com cada herdeiro a distância e, quando o "
                "processo é eletrônico, atuamos em qualquer lugar do Brasil. Em "
                "cartório, muitas escrituras também podem ser assinadas de forma "
                "eletrônica.",
            ),
            (
                "Como são combinados os honorários?",
                "Depois de conhecer os bens e a situação da família, apresentamos a "
                "proposta por escrito. O contrato diz o que está incluído, para "
                "ninguém ter surpresa no meio do caminho.",
            ),
        ],
        "final_h2": "O inventário pode começar por uma mensagem",
    },
    # 3. DESPORTIVO ----------------------------------------------------------
    {
        "slug": "desportivo",
        "nome": "Direito Desportivo",
        "curto": "Desportivo",
        "gatilho": "Sou atleta e preciso de ajuda",
        "card": (
            "Contratos de atletas e técnicos, valores devidos pelo clube, "
            "certificação de clube formador e pedido do Bolsa Atleta."
        ),
        "seo_titulo": "Advogado desportivo em Uberlândia | Justino & Assunção",
        "seo_descricao": (
            "Direito desportivo em Uberlândia: contrato de atleta e técnico, "
            "valores devidos pelo clube, clube formador e Bolsa Atleta. Atendimento "
            "em todo o Brasil."
        ),
        "hero_h1": "Advocacia para atleta, técnico e clube",
        "hero_p": (
            "O departamento de Direito Desportivo cuida de contratos, conflitos "
            "com clubes e pedidos como o Bolsa Atleta. Atendemos atletas, técnicos, "
            "clubes e famílias de atletas da base, em todo o Brasil."
        ),
        "cta": "Falar sobre o meu caso",
        "msg": "Olá, Justino & Assunção! Preciso de ajuda com direito desportivo.",
        "situacoes_h2": "Para quem vive do esporte",
        "situacoes": [
            (
                "Vou assinar contrato com um clube",
                "Lemos o contrato antes da assinatura: prazo, salário, direito de "
                "imagem, multas e o que acontece se alguém quiser sair antes. Você "
                "assina sabendo o que foi combinado.",
            ),
            (
                "O estadual acabou e o meu contrato também",
                "Contratos curtos, que terminam junto com o campeonato, são comuns. "
                "Conferimos se o clube pagou o que deve na saída, como salário, "
                "férias, 13º e FGTS, e cobramos o que faltar.",
            ),
            (
                "Sou técnico e o clube não me pagou",
                "Cobramos salários e valores em atraso de técnicos e comissões "
                "técnicas. Em alguns casos, o dirigente que administrava o clube "
                "também pode responder pela dívida.",
            ),
            (
                "Meu filho joga na base de um clube",
                "Orientamos a família sobre o contrato de formação, a bolsa de "
                "aprendizagem e o primeiro contrato profissional, para que os "
                "direitos do atleta jovem fiquem claros desde cedo.",
            ),
            (
                "Nosso clube quer ser clube formador",
                "O certificado de clube formador dá ao clube direitos como assinar "
                "o primeiro contrato profissional do atleta e receber indenização "
                "se ele for para outra equipe. Orientamos o clube nos requisitos.",
            ),
            (
                "Quero pedir o Bolsa Atleta",
                "Orientamos atletas, responsáveis e representantes na inscrição do "
                "Bolsa Atleta, o programa de bolsas do governo federal, e na "
                "conferência dos documentos antes do envio.",
            ),
        ],
        "atuacao_h2": "Como o departamento conduz o seu caso",
        "atuacao": [
            (
                "Primeiro contato",
                "Você conta a situação e envia o que tiver: contrato, recibos, "
                "mensagens com o clube ou o edital do Bolsa Atleta. Verificamos "
                "logo se há prazo correndo.",
            ),
            (
                "Proposta e contrato",
                "Explicamos como vamos atuar e combinamos os honorários em contrato "
                "escrito, antes de começar. Se o atleta é menor de idade, o "
                "responsável participa de tudo.",
            ),
            (
                "Estudo do caso",
                "Lemos o contrato, a Lei Geral do Esporte e as regras da "
                "modalidade. Com isso, definimos o caminho: conversa com o clube, "
                "notificação ou ação na Justiça.",
            ),
            (
                "Acompanhamento",
                "Acompanhamos cada etapa e explicamos o que muda para a sua "
                "carreira ou para o seu clube, em palavras simples.",
            ),
        ],
        "documentos_h2": "O que separar para a primeira conversa",
        "documentos": [
            "RG e CPF do atleta ou do técnico e, se ele for menor de idade, do responsável",
            "Contrato com o clube, contrato de imagem e aditivos, se houver",
            "Recibos, holerites e extratos dos pagamentos recebidos",
            "Mensagens, e-mails e notificações trocados com o clube",
            "Laudos e exames médicos, em caso de lesão",
            "Comprovantes de resultados em competições, para o Bolsa Atleta",
            "Estatuto e documentos do clube, quando quem procura é o clube",
        ],
        "faq": [
            (
                "Qual a duração de um contrato de atleta profissional?",
                "O contrato é por prazo determinado. A Lei Geral do Esporte prevê "
                "duração mínima de 3 meses e máxima de 5 anos. Quando ele "  # [REVISAR: prazo legal]
                "termina, o clube precisa pagar as verbas da saída.",
            ),
            (
                "Me machuquei e o clube quer me dispensar. E agora?",
                "Durante a recuperação de uma lesão sofrida a serviço do clube, o "
                "atleta tem direitos, como tratamento e o seguro de acidentes que o "
                "clube é obrigado a contratar. Analisamos o contrato e o momento da "
                "dispensa para ver o que pode ser pedido.",
            ),
            (
                "Quem pode pedir o Bolsa Atleta?",
                "Atletas com resultados em competições do ano anterior, conforme a "  # [REVISAR: prazo legal]
                "categoria da bolsa, e que cumprem os requisitos do edital. A "
                "inscrição é feita no período aberto pelo Ministério do Esporte, e "
                "a bolsa é paga em 12 parcelas mensais.",  # [REVISAR: prazo legal]
            ),
            (
                "Vocês atendem atletas de outras cidades?",
                "Sim. Atletas e clubes mudam de cidade o tempo todo. Conversamos a "
                "distância e, quando o processo é eletrônico, atuamos em qualquer "
                "lugar do Brasil. Se algum ato exigir presença, avisamos antes.",
            ),
            (
                "Como são combinados os honorários?",
                "Depois de entender o caso, apresentamos a proposta por escrito. O "
                "contrato diz o que está incluído, como a análise do contrato, a "
                "conversa com o clube ou uma ação na Justiça.",
            ),
        ],
        "final_h2": "Atleta, técnico ou clube: conte o seu caso",
    },
    # 4. MARCAS --------------------------------------------------------------
    {
        "slug": "marcas",
        "nome": "Registro de Marca",
        "curto": "Marcas",
        "gatilho": "Quero registrar minha marca",
        "card": (
            "Estudo prévio, pedido no INPI e acompanhamento até a decisão, além de "
            "contratos e notificações sobre a marca."
        ),
        "seo_titulo": "Registro de marca no INPI em Uberlândia | Justino & Assunção",
        "seo_descricao": (
            "Registro de marca no INPI em Uberlândia e em todo o Brasil: estudo "
            "prévio, pedido e acompanhamento até a decisão, contratos e "
            "notificações."
        ),
        "hero_h1": "Registro de marca, do estudo à decisão",
        "hero_p": (
            "No Brasil, em regra, a marca pertence a quem a registra no INPI. Antes "
            "do pedido, fazemos um estudo para ver se o nome pode ser registrado e "
            "depois acompanhamos o processo até a decisão."
        ),
        "cta": "Falar sobre a minha marca",
        "msg": "Olá, Justino & Assunção! Quero registrar a minha marca.",
        "situacoes_h2": "Quando a marca precisa de proteção",
        "situacoes": [
            (
                "Vou abrir um negócio e escolhi um nome",
                "Antes de investir em fachada, site e embalagem, o estudo prévio "
                "verifica se já existe marca igual ou parecida registrada no mesmo "
                "ramo.",
            ),
            (
                "Minha empresa já usa a marca há anos",
                "Usar não é o mesmo que ter o registro. Fazemos o pedido no INPI "
                "para que a marca vire um bem da empresa, que pode ser vendido, "
                "licenciado ou usado numa franquia.",
            ),
            (
                "Alguém está copiando a minha marca",
                "Com a marca registrada, é possível agir contra a cópia e o uso "
                "indevido. Enviamos notificação a quem está usando e, se preciso, "
                "levamos o caso à Justiça.",
            ),
            (
                "Recebi uma notificação sobre a minha marca",
                "Analisamos a notificação, verificamos quem tem direito sobre o "
                "nome e respondemos. Se o caso virar processo, fazemos a sua "
                "defesa.",
            ),
            (
                "Vou fazer uma parceria com outra marca",
                "Escrevemos e revisamos contratos de licença, cessão e parceria, "
                "deixando claro quem pode usar a marca, onde e por quanto tempo.",
            ),
            (
                "Quero o selo de verificado nas redes",
                "O registro no INPI ajuda no pedido de verificação de perfis em "
                "redes sociais, porque mostra que a marca é sua.",
            ),
        ],
        "atuacao_h2": "Como cuidamos do registro",
        "atuacao": [
            (
                "Primeira conversa",
                "Você conta o nome, mostra o logotipo e explica o que a empresa "
                "faz. Com isso, definimos em quais ramos de atividade a marca "
                "precisa ser registrada.",
            ),
            (
                "Estudo prévio",
                "Pesquisamos marcas iguais ou parecidas já pedidas ou registradas. "
                "Se houver risco de conflito, você fica sabendo antes de pagar as "
                "taxas do pedido.",
            ),
            (
                "Proposta e pedido",
                "Combinamos os honorários em contrato escrito e fazemos o pedido no "
                "INPI, com os documentos e as taxas em ordem.",
            ),
            (
                "Até a decisão do INPI",
                "Acompanhamos o processo, respondemos às exigências e às oposições, "
                "que é quando outra empresa contesta o pedido, e avisamos você de "
                "cada etapa.",
            ),
        ],
        "documentos_h2": "O que separar para a primeira conversa",
        "documentos": [
            "Nome da marca, escrito exatamente como é usado",
            "Logotipo em boa resolução, se houver",
            "CNPJ e contrato social da empresa, ou RG e CPF, se o pedido for no seu nome",
            "Lista dos produtos ou serviços que levam a marca",
            "Data em que a marca começou a ser usada, se você souber",
            "Notificações ou mensagens sobre uso da marca por outras pessoas, se houver",
        ],
        "faq": [
            (
                "Por que fazer o estudo prévio?",
                "Porque o INPI pode negar o pedido se já existir marca parecida no "
                "mesmo ramo. O estudo mostra esse risco antes de você gastar com "
                "taxas e com a identidade visual.",
            ),
            (
                "Quanto tempo leva o registro?",
                "Depende da fila do INPI e de haver exigência ou oposição no "
                "caminho. Acompanhamos o processo e avisamos você de cada "
                "movimentação.",
            ),
            (
                "O registro vale para sempre?",
                "O registro vale por 10 anos e pode ser renovado por períodos "  # [REVISAR: prazo legal]
                "iguais, quantas vezes você quiser. A renovação tem prazo, e o "
                "escritório pode cuidar dela.",
            ),
            (
                "O registro vale em todo o Brasil?",
                "Sim. O registro no INPI protege a marca em todo o país, no ramo em "
                "que ela foi registrada. Como o pedido é feito pela internet, "
                "atendemos empresas de qualquer cidade.",
            ),
            (
                "Como são combinados os honorários?",
                "Depois de entender a marca e em quantos ramos ela precisa de "
                "proteção, apresentamos a proposta por escrito. O contrato explica "
                "também as taxas cobradas pelo INPI, que são pagas à parte.",
            ),
        ],
        "final_h2": "Conte qual marca você quer proteger",
    },
    # 5. PREVIDENCIÁRIO ------------------------------------------------------
    {
        "slug": "previdenciario",
        "nome": "Direito Previdenciário",
        "curto": "Previdenciário",
        "gatilho": "O INSS negou o meu benefício",
        "card": (
            "Aposentadoria, revisão, auxílio por incapacidade, BPC/LOAS e recurso "
            "quando o INSS nega o benefício."
        ),
        "seo_titulo": "Advogado previdenciário em Uberlândia | Justino & Assunção",
        "seo_descricao": (
            "Aposentadoria, revisão, auxílio por incapacidade, BPC/LOAS e benefício "
            "negado pelo INSS em Uberlândia e em todo o Brasil. Fale com o "
            "escritório."
        ),
        "hero_h1": "Aposentadoria e benefícios do INSS",
        "hero_p": (
            "Analisamos o seu histórico de contribuições, pedimos a aposentadoria "
            "ou o benefício e recorremos quando o INSS nega. Antes de qualquer "
            "pedido, você entende quais regras valem para o seu caso."
        ),
        "cta": "Falar sobre o benefício",
        "msg": "Olá, Justino & Assunção! Preciso de ajuda com um benefício do INSS.",
        "situacoes_h2": "Quando o assunto é o INSS",
        "situacoes": [
            (
                "Quero saber se já posso me aposentar",
                "Conferimos o seu histórico de contribuições e fazemos as contas "
                "pelas regras atuais e pelas regras de transição da reforma da "
                "Previdência, para mostrar quando e como pedir.",
            ),
            (
                "O INSS negou o meu benefício",
                "Lemos a carta do INSS com o motivo da negativa e avaliamos o "
                "caminho: recurso no próprio INSS ou ação na Justiça. O recurso tem "
                "prazo, então vale não deixar para depois.",
            ),
            (
                "Estou doente e não consigo trabalhar",
                "Pedimos o auxílio por incapacidade temporária, o antigo "
                "auxílio-doença, ou a aposentadoria por incapacidade permanente, "
                "com laudos e exames organizados para a perícia.",
            ),
            (
                "Preciso do BPC/LOAS",
                "O BPC paga um salário mínimo por mês à pessoa idosa ou com "  # [REVISAR: prazo legal]
                "deficiência de família de baixa renda, mesmo que ela nunca tenha "
                "contribuído. Cuidamos do pedido e do recurso, se ele for negado.",
            ),
            (
                "O valor da minha aposentadoria parece errado",
                "Conferimos o cálculo e os períodos que o INSS considerou. Se ficou "
                "de fora algum período de trabalho ou salário, pedimos a revisão do "
                "valor.",
            ),
            (
                "Um familiar faleceu e eu dependia dele",
                "Cônjuge, companheiro e filhos, nos casos previstos em lei, podem "
                "ter direito à pensão por morte. Fazemos o pedido e, se a família "
                "também precisar do inventário, cuidamos dos dois.",
            ),
        ],
        "atuacao_h2": "Como cuidamos do seu pedido no INSS",
        "atuacao": [
            (
                "Primeira conversa",
                "Você conta a sua situação e envia o que tiver: carta do INSS, "
                "carteira de trabalho, laudos. Verificamos logo se há prazo de "
                "recurso correndo.",
            ),
            (
                "Proposta e contrato",
                "Explicamos como vamos atuar e combinamos os honorários em contrato "
                "escrito, antes de começar.",
            ),
            (
                "Análise e cálculo",
                "Conferimos o histórico de contribuições, os períodos de trabalho e "
                "os documentos médicos, e definimos o pedido que faz sentido para "
                "o seu caso.",
            ),
            (
                "Pedido e acompanhamento",
                "Fazemos o pedido ou o recurso no INSS, ou a ação na Justiça, e "
                "acompanhamos perícias, exigências e decisões, explicando cada uma "
                "em palavras simples.",
            ),
        ],
        "documentos_h2": "O que separar para a primeira conversa",
        "documentos": [
            "RG e CPF",
            "Carteiras de trabalho, inclusive as antigas",
            "Extrato do CNIS, o histórico de contribuições, tirado no aplicativo ou no site Meu INSS",
            "Carnês ou guias de contribuição pagas como autônomo, se houver",
            "Carta do INSS com a decisão, se o benefício foi negado",
            "Laudos, exames e receitas, nos pedidos por doença",
            "PPP, o formulário da empresa sobre trabalho com ruído, calor ou produtos químicos, se houver",
            "Inscrição atualizada no CadÚnico e comprovantes de renda da família, no caso do BPC",
        ],
        "faq": [
            (
                "O INSS negou. Qual o prazo para recorrer?",
                "O recurso no próprio INSS tem prazo de 30 dias, contados de quando "  # [REVISAR: prazo legal]
                "você fica sabendo da decisão. Também é possível ir direto à "
                "Justiça. Por isso, procure o escritório assim que a carta chegar.",
            ),
            (
                "Quem tem direito ao BPC/LOAS?",
                "A pessoa com 65 anos ou mais, ou a pessoa com deficiência, cuja "  # [REVISAR: prazo legal]
                "família tenha renda de até 1/4 do salário mínimo por pessoa. Em "  # [REVISAR: prazo legal]
                "alguns casos, a lei e a Justiça aceitam renda maior. Não é preciso "
                "ter contribuído, mas é preciso estar inscrito no CadÚnico.",
            ),
            (
                "Posso pedir revisão de uma aposentadoria antiga?",
                "Em regra, sim, dentro de 10 anos contados do mês seguinte ao "  # [REVISAR: prazo legal]
                "primeiro pagamento. Analisamos a carta de concessão e o cálculo "
                "para ver se o pedido faz sentido.",
            ),
            (
                "Preciso ir a Uberlândia para ser atendido?",
                "Não. Conversamos a distância e, quando o processo é eletrônico, "
                "atuamos em qualquer lugar do Brasil. Se houver perícia ou "
                "audiência, avisamos antes e explicamos como ela funciona.",
            ),
            (
                "Como são combinados os honorários?",
                "Depois de entender o caso, apresentamos a proposta por escrito. O "
                "contrato diz o que está incluído, como o pedido no INSS, o recurso "
                "ou a ação na Justiça.",
            ),
        ],
        "final_h2": "Recebeu a carta do INSS? Fale conosco no prazo",
    },
    # 6. CIVIL ---------------------------------------------------------------
    {
        "slug": "civel",
        "nome": "Direito Civil",
        "curto": "Civil",
        "gatilho": "Fui processado ou quero processar",
        "card": (
            "Contratos, cobranças, indenizações e direito do consumidor, tanto na "
            "defesa quanto na ação."
        ),
        "seo_titulo": "Advogado cível em Uberlândia | Justino & Assunção",
        "seo_descricao": (
            "Contratos, cobranças, indenizações e direito do consumidor em "
            "Uberlândia, na defesa ou na ação, para pessoas e empresas. Fale com o "
            "escritório."
        ),
        "hero_h1": "Foi processado? A defesa tem prazo",
        "hero_p": (
            "Se chegou uma citação, que é o aviso oficial de um processo contra "
            "você, o prazo para se defender começa a contar. Também entramos com "
            "ações de cobrança, indenização, contratos e consumidor."
        ),
        "cta": "Falar sobre o meu caso",
        "msg": "Olá, Justino & Assunção! Preciso de ajuda com um processo ou um contrato.",
        "situacoes_h2": "Problemas do dia a dia que viram processo",
        "situacoes": [
            (
                "Chegou um processo contra mim",
                "Lemos a ação, reunimos as provas e apresentamos a defesa dentro "
                "do prazo. Quanto antes você nos procurar, mais tempo há para "
                "preparar a resposta.",
            ),
            (
                "Tenho dinheiro a receber",
                "Quando alguém deve e não paga, entramos com a cobrança. Se você "
                "tem cheque, nota promissória ou contrato assinado, pode caber a "
                "execução, um caminho mais direto para cobrar.",
            ),
            (
                "Sofri um prejuízo e quero reparação",
                "Avaliamos se houve dano material ou moral e quem é o responsável, "
                "e entramos com o pedido de indenização na Justiça.",
            ),
            (
                "O contrato não foi cumprido",
                "Analisamos o contrato e as conversas entre as partes e pedimos o "
                "cumprimento, o fim do contrato ou a reparação do prejuízo.",
            ),
            (
                "Tive problema com uma empresa",
                "Produto com defeito, cobrança indevida, nome negativado sem motivo "
                "ou serviço não prestado. Atuamos com base no Código de Defesa do "
                "Consumidor.",
            ),
            (
                "Vou assinar um contrato importante",
                "Escrevemos e revisamos contratos de compra e venda, prestação de "
                "serviço, aluguel e sociedade, para evitar dúvidas e brigas lá na "
                "frente.",
            ),
        ],
        "atuacao_h2": "Como conduzimos o seu caso",
        "atuacao": [
            (
                "Primeiro contato",
                "Você conta o que aconteceu e envia o que tiver: contrato, "
                "mensagens ou a citação. Verificamos logo se há prazo correndo.",
            ),
            (
                "Proposta e contrato",
                "Explicamos como vamos atuar e combinamos os honorários em contrato "
                "escrito, antes de começar.",
            ),
            (
                "Defesa ou ação",
                "Estudamos os documentos e a lei aplicável e escrevemos a defesa ou "
                "a ação para o seu caso, com as provas organizadas.",
            ),
            (
                "Acompanhamento",
                "Acompanhamos audiências, prazos, tentativas de acordo e recursos, "
                "e você é informado de cada decisão importante.",
            ),
        ],
        "documentos_h2": "O que separar para a primeira conversa",
        "documentos": [
            "RG e CPF, ou os documentos da empresa, se for o caso",
            "A citação ou intimação que você recebeu, se houver",
            "Contratos, recibos, notas fiscais e comprovantes de pagamento",
            "Conversas de WhatsApp, e-mails e notificações sobre o problema",
            "Fotos, laudos ou orçamentos que mostrem o prejuízo",
            "A minuta do contrato, se você ainda vai assinar",
            "Nome e dados da outra parte, se você tiver",
        ],
        "faq": [
            (
                "Qual o prazo para me defender?",
                "Na Justiça comum, em regra, são 15 dias úteis, contados conforme a "  # [REVISAR: prazo legal]
                "forma da citação. No Juizado Especial, a defesa costuma ser "
                "apresentada até a audiência. Por isso, procure o escritório assim "
                "que receber a citação.",
            ),
            (
                "O que acontece se eu não responder?",
                "O processo segue sem a sua versão, e o juiz pode considerar "
                "verdadeiros os fatos contados pela outra parte. É o que se chama "
                "de revelia.",
            ),
            (
                "Preciso de advogado no Juizado Especial?",
                "Em causas de até 20 salários mínimos, a lei não exige advogado no "  # [REVISAR: prazo legal]
                "Juizado Especial Cível. Ainda assim, a defesa técnica ajuda a não "
                "perder prazos nem provas.",
            ),
            (
                "O processo é em outra cidade. Vocês podem atuar?",
                "Sim. Quando o processo é eletrônico, atuamos em qualquer lugar do "
                "Brasil e conversamos com você a distância. Se algum ato exigir "
                "presença, avisamos antes de começar.",
            ),
            (
                "Como são combinados os honorários?",
                "Depois de entender o caso, apresentamos a proposta por escrito. O "
                "contrato descreve o que está incluído, como a defesa, as "
                "audiências e eventuais recursos.",
            ),
        ],
        "final_h2": "Conte o que aconteceu e mande o que tiver",
    },
]
