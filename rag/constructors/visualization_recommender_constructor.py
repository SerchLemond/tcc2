from rag.services.llm_service import LLM_service
import json

class VisualizationRecommenderConstructor:
    _INSTRUCTION = """ 
    Você é um agente responsável por sugerir tipos de visualizações de dados e gerar os dados transformados para cada gráfico.

    Será fornecida uma query SQL e a resposta correspondente em formato textual. Sua tarefa é analisar os dados retornados e gerar um JSON que contenha todas as visualizações possíveis, usando apenas os dados da resposta fornecida.

    Regras:

    1- As saídas devem ser consistentes: todos os gráficos devem usar os mesmos dados de entrada. Não crie gráficos de assuntos diferentes na mesma resposta.

    2- As opções de gráficos são: grafico_barras, grafico_linhas, mapas_coropleticos, graficos_com_proporcao.

    3- Para cada opção, forneça um score entre 0 e 1 indicando a relevância do gráfico para os dados.

    4- Cada visualização deve conter:
    4.1- tipo: nome do gráfico.

    4.2- score: peso de relevância.

    4.3- titulo: string contendo o título do gráfico.

    4.4- dados: array de objetos com:

    4.5- dimensoes: objeto com chaves representando dimensões.

    4.5.1- A primeira dimensão deve ser usada em um dos eixos do gráfico (x ou y) e ser a dimensão principal.

    4.5.2- A segunda dimensão deve indicar proporção/empilhamento nos gráficos de proporção ou cor/agrupamento nos outros gráficos.

    4.5.3- Se houver mais dimensões, inclua-as na ordem de importância para alterar cor ou agrupamento.

    4.5.4- valor: valor numérico associado à combinação de dimensões.

    5- Para gráficos de mapas_coropleticos, use os nomes de estados padronizados conforme o exemplo fornecido.

    6- Todos os dados da resposta devem ser adaptados para cada tipo de gráfico e mantidos consistentes entre as visualizações.

    7- Os gráficos de barras verticais e orizontais devem ter os mesmos dados na lista de dados do json
    
    8- Responda apenas com um JSON **puro**, **sem usar blocos de código Markdown** () ou quaisquer outros caracteres adicionais.
    
    9- Não inclua explicações, texto ou palavras fora do JSON.
    
    Exemplo de resposta (JSON puro):
    {
        "visualizacoes": [
            {
            "tipo": "grafico_barras_vertical",
            "score": 0.9,
            "titulo": "",
            "dados": [
                { "dimensoes": { "estado": "São Paulo" }, "valor": 18201 },
                { "dimensoes": { "estado": "Rio de Janeiro" }, "valor": 12361 },
                { "dimensoes": { "estado": "Pernambuco" }, "valor": 5251 },
                { "dimensoes": { "estado": "Pará" }, "valor": 4804 },
                { "dimensoes": { "estado": "Rio Grande do Sul" }, "valor": 4729 },
                { "dimensoes": { "estado": "Bahia" }, "valor": 4324 },
                { "dimensoes": { "estado": "Minas Gerais" }, "valor": 3799 },
                { "dimensoes": { "estado": "Amazonas" }, "valor": 3659 },
                { "dimensoes": { "estado": "Ceará" }, "valor": 3491 },
                { "dimensoes": { "estado": "Maranhão" }, "valor": 2492 },
                { "dimensoes": { "estado": "Paraná" }, "valor": 2201 },
                { "dimensoes": { "estado": "Santa Catarina" }, "valor": 1937 },
                { "dimensoes": { "estado": "Rio Grande do Norte" }, "valor": 1366 },
                { "dimensoes": { "estado": "Espírito Santo" }, "valor": 1350 },
                { "dimensoes": { "estado": "Mato Grosso do Sul" }, "valor": 1387 },
                { "dimensoes": { "estado": "Mato Grosso" }, "valor": 1151 },
                { "dimensoes": { "estado": "Paraíba" }, "valor": 1248 },
                { "dimensoes": { "estado": "Goiás" }, "valor": 1000 },
                { "dimensoes": { "estado": "Alagoas" }, "valor": 939 },
                { "dimensoes": { "estado": "Sergipe" }, "valor": 934 },
                { "dimensoes": { "estado": "Piauí" }, "valor": 745 },
                { "dimensoes": { "estado": "Rondônia" }, "valor": 570 },
                { "dimensoes": { "estado": "Acre" }, "valor": 528 },
                { "dimensoes": { "estado": "Roraima" }, "valor": 435 },
                { "dimensoes": { "estado": "Amapá" }, "valor": 406 },
                { "dimensoes": { "estado": "Distrito Federal" }, "valor": 337 },
                { "dimensoes": { "estado": "Tocantins" }, "valor": 217 }
            ]
            },
            {
            "tipo": "grafico_barras_horizontal",
            "score": 0.9,
            "titulo": "",
            "dados": [
                { "dimensoes": { "estado": "São Paulo" }, "valor": 18201 },
                { "dimensoes": { "estado": "Rio de Janeiro" }, "valor": 12361 },
                { "dimensoes": { "estado": "Pernambuco" }, "valor": 5251 },
                { "dimensoes": { "estado": "Pará" }, "valor": 4804 },
                { "dimensoes": { "estado": "Rio Grande do Sul" }, "valor": 4729 },
                { "dimensoes": { "estado": "Bahia" }, "valor": 4324 },
                { "dimensoes": { "estado": "Minas Gerais" }, "valor": 3799 },
                { "dimensoes": { "estado": "Amazonas" }, "valor": 3659 },
                { "dimensoes": { "estado": "Ceará" }, "valor": 3491 },
                { "dimensoes": { "estado": "Maranhão" }, "valor": 2492 },
                { "dimensoes": { "estado": "Paraná" }, "valor": 2201 },
                { "dimensoes": { "estado": "Santa Catarina" }, "valor": 1937 },
                { "dimensoes": { "estado": "Rio Grande do Norte" }, "valor": 1366 },
                { "dimensoes": { "estado": "Espírito Santo" }, "valor": 1350 },
                { "dimensoes": { "estado": "Mato Grosso do Sul" }, "valor": 1387 },
                { "dimensoes": { "estado": "Mato Grosso" }, "valor": 1151 },
                { "dimensoes": { "estado": "Paraíba" }, "valor": 1248 },
                { "dimensoes": { "estado": "Goiás" }, "valor": 1000 },
                { "dimensoes": { "estado": "Alagoas" }, "valor": 939 },
                { "dimensoes": { "estado": "Sergipe" }, "valor": 934 },
                { "dimensoes": { "estado": "Piauí" }, "valor": 745 },
                { "dimensoes": { "estado": "Rondônia" }, "valor": 570 },
                { "dimensoes": { "estado": "Acre" }, "valor": 528 },
                { "dimensoes": { "estado": "Roraima" }, "valor": 435 },
                { "dimensoes": { "estado": "Amapá" }, "valor": 406 },
                { "dimensoes": { "estado": "Distrito Federal" }, "valor": 337 },
                { "dimensoes": { "estado": "Tocantins" }, "valor": 217 }
            ]
            },
            {
            "tipo": "mapas_coropleticos",
            "score": 0.9,
            "titulo": "",
            "dados": [
                { "dimensoes": { "estado": "São Paulo" }, "valor": 18201 },
                { "dimensoes": { "estado": "Rio de Janeiro" }, "valor": 12361 },
                { "dimensoes": { "estado": "Pernambuco" }, "valor": 5251 },
                { "dimensoes": { "estado": "Pará" }, "valor": 4804 },
                { "dimensoes": { "estado": "Rio Grande do Sul" }, "valor": 4729 },
                { "dimensoes": { "estado": "Bahia" }, "valor": 4324 },
                { "dimensoes": { "estado": "Minas Gerais" }, "valor": 3799 },
                { "dimensoes": { "estado": "Amazonas" }, "valor": 3659 },
                { "dimensoes": { "estado": "Ceará" }, "valor": 3491 },
                { "dimensoes": { "estado": "Maranhão" }, "valor": 2492 },
                { "dimensoes": { "estado": "Paraná" }, "valor": 2201 },
                { "dimensoes": { "estado": "Santa Catarina" }, "valor": 1937 },
                { "dimensoes": { "estado": "Rio Grande do Norte" }, "valor": 1366 },
                { "dimensoes": { "estado": "Espírito Santo" }, "valor": 1350 },
                { "dimensoes": { "estado": "Mato Grosso do Sul" }, "valor": 1387 },
                { "dimensoes": { "estado": "Mato Grosso" }, "valor": 1151 },
                { "dimensoes": { "estado": "Paraíba" }, "valor": 1248 },
                { "dimensoes": { "estado": "Goiás" }, "valor": 1000 },
                { "dimensoes": { "estado": "Alagoas" }, "valor": 939 },
                { "dimensoes": { "estado": "Sergipe" }, "valor": 934 },
                { "dimensoes": { "estado": "Piauí" }, "valor": 745 },
                { "dimensoes": { "estado": "Rondônia" }, "valor": 570 },
                { "dimensoes": { "estado": "Acre" }, "valor": 528 },
                { "dimensoes": { "estado": "Roraima" }, "valor": 435 },
                { "dimensoes": { "estado": "Amapá" }, "valor": 406 },
                { "dimensoes": { "estado": "Distrito Federal" }, "valor": 337 },
                { "dimensoes": { "estado": "Tocantins" }, "valor": 217 }
            ]
            },
            {
            "tipo": "graficos_linhas",
            "score": 0.1,
            "titulo": "",
            "dados": [
                { "dimensoes": { "numMes": 1, "mes": "Janeiro" }, "valor": 5333 },
                { "dimensoes": { "numMes": 2, "mes": "Fevereiro" }, "valor": 6205 },
                { "dimensoes": { "numMes": 3, "mes": "Março" }, "valor": 7194 },
                { "dimensoes": { "numMes": 4, "mes": "Abril" }, "valor": 6731 },
                { "dimensoes": { "numMes": 5, "mes": "Maio" }, "valor": 6748 },
                { "dimensoes": { "numMes": 6, "mes": "Junho" }, "valor": 7102 },
                { "dimensoes": { "numMes": 7, "mes": "Julho" }, "valor": 7576 },
                { "dimensoes": { "numMes": 8, "mes": "Agosto" }, "valor": 8241 },
                { "dimensoes": { "numMes": 9, "mes": "Setembro" }, "valor": 8162 },
                { "dimensoes": { "numMes": 10, "mes": "Outubro" }, "valor": 7946 },
                { "dimensoes": { "numMes": 11, "mes": "Novembro" }, "valor": 8159 },
                { "dimensoes": { "numMes": 12, "mes": "Dezembro" }, "valor": 8052 }
            ]
            },
            {
            "tipo": "graficos_com_proporcao",
            "score": 0.7,
            "titulo": "",
            "dados": [
                                { "dimensoes": { "mes": "Janeiro", "raca": "Parda" }, "valor": 4847 },
                { "dimensoes": { "mes": "Janeiro", "raca": "Branca" }, "valor": 2378 },
                { "dimensoes": { "mes": "Janeiro", "raca": "Preta" }, "valor": 1282 },
                { "dimensoes": { "mes": "Janeiro", "raca": "Ignorado" }, "valor": 524 },
                { "dimensoes": { "mes": "Janeiro", "raca": "Amarela" }, "valor": 100 },
                { "dimensoes": { "mes": "Janeiro", "raca": "Indígena" }, "valor": 97 },

                { "dimensoes": { "mes": "Fevereiro", "raca": "Parda" }, "valor": 3916 },
                { "dimensoes": { "mes": "Fevereiro", "raca": "Branca" }, "valor": 2094 },
                { "dimensoes": { "mes": "Fevereiro", "raca": "Preta" }, "valor": 1072 },
                { "dimensoes": { "mes": "Fevereiro", "raca": "Ignorado" }, "valor": 421 },
                { "dimensoes": { "mes": "Fevereiro", "raca": "Amarela" }, "valor": 67 },
                { "dimensoes": { "mes": "Fevereiro", "raca": "Indígena" }, "valor": 70 },

                { "dimensoes": { "mes": "Março", "raca": "Parda" }, "valor": 5476 },
                { "dimensoes": { "mes": "Março", "raca": "Branca" }, "valor": 2687 },
                { "dimensoes": { "mes": "Março", "raca": "Preta" }, "valor": 1413 },
                { "dimensoes": { "mes": "Março", "raca": "Ignorado" }, "valor": 566 },
                { "dimensoes": { "mes": "Março", "raca": "Amarela" }, "valor": 117 },
                { "dimensoes": { "mes": "Março", "raca": "Indígena" }, "valor": 87 },

                { "dimensoes": { "mes": "Abril", "raca": "Parda" }, "valor": 4405 },
                { "dimensoes": { "mes": "Abril", "raca": "Branca" }, "valor": 2185 },
                { "dimensoes": { "mes": "Abril", "raca": "Preta" }, "valor": 1177 },
                { "dimensoes": { "mes": "Abril", "raca": "Ignorado" }, "valor": 461 },
                { "dimensoes": { "mes": "Abril", "raca": "Amarela" }, "valor": 87 },
                { "dimensoes": { "mes": "Abril", "raca": "Indígena" }, "valor": 71 },

                { "dimensoes": { "mes": "Maio", "raca": "Parda" }, "valor": 5154 },
                { "dimensoes": { "mes": "Maio", "raca": "Branca" }, "valor": 2494 },
                { "dimensoes": { "mes": "Maio", "raca": "Preta" }, "valor": 1391 },
                { "dimensoes": { "mes": "Maio", "raca": "Ignorado" }, "valor": 500 },
                { "dimensoes": { "mes": "Maio", "raca": "Indígena" }, "valor": 132 },
                { "dimensoes": { "mes": "Maio", "raca": "Amarela" }, "valor": 82 },

                { "dimensoes": { "mes": "Junho", "raca": "Parda" }, "valor": 4624 },
                { "dimensoes": { "mes": "Junho", "raca": "Branca" }, "valor": 2385 },
                { "dimensoes": { "mes": "Junho", "raca": "Preta" }, "valor": 1314 },
                { "dimensoes": { "mes": "Junho", "raca": "Ignorado" }, "valor": 429 },
                { "dimensoes": { "mes": "Junho", "raca": "Indígena" }, "valor": 96 },
                { "dimensoes": { "mes": "Junho", "raca": "Amarela" }, "valor": 79 },

                { "dimensoes": { "mes": "Julho", "raca": "Parda" }, "valor": 4928 },
                { "dimensoes": { "mes": "Julho", "raca": "Branca" }, "valor": 2333 },
                { "dimensoes": { "mes": "Julho", "raca": "Preta" }, "valor": 1307 },
                { "dimensoes": { "mes": "Julho", "raca": "Ignorado" }, "valor": 424 },
                { "dimensoes": { "mes": "Julho", "raca": "Indígena" }, "valor": 118 },
                { "dimensoes": { "mes": "Julho", "raca": "Amarela" }, "valor": 92 },

                { "dimensoes": { "mes": "Agosto", "raca": "Parda" }, "valor": 5311 },
                { "dimensoes": { "mes": "Agosto", "raca": "Branca" }, "valor": 2666 },
                { "dimensoes": { "mes": "Agosto", "raca": "Preta" }, "valor": 1480 },
                { "dimensoes": { "mes": "Agosto", "raca": "Ignorado" }, "valor": 540 },
                { "dimensoes": { "mes": "Agosto", "raca": "Indígena" }, "valor": 105 },
                { "dimensoes": { "mes": "Agosto", "raca": "Amarela" }, "valor": 80 },

                { "dimensoes": { "mes": "Setembro", "raca": "Parda" }, "valor": 4738 },
                { "dimensoes": { "mes": "Setembro", "raca": "Branca" }, "valor": 2330 },
                { "dimensoes": { "mes": "Setembro", "raca": "Preta" }, "valor": 1262 },
                { "dimensoes": { "mes": "Setembro", "raca": "Ignorado" }, "valor": 472 },
                { "dimensoes": { "mes": "Setembro", "raca": "Indígena" }, "valor": 91 },
                { "dimensoes": { "mes": "Setembro", "raca": "Amarela" }, "valor": 72 },

                { "dimensoes": { "mes": "Outubro", "raca": "Parda" }, "valor": 5043 },
                { "dimensoes": { "mes": "Outubro", "raca": "Branca" }, "valor": 2501 },
                { "dimensoes": { "mes": "Outubro", "raca": "Preta" }, "valor": 1337 },
                { "dimensoes": { "mes": "Outubro", "raca": "Ignorado" }, "valor": 467 },
                { "dimensoes": { "mes": "Outubro", "raca": "Indígena" }, "valor": 108 },
                { "dimensoes": { "mes": "Outubro", "raca": "Amarela" }, "valor": 104 },

                { "dimensoes": { "mes": "Novembro", "raca": "Parda" }, "valor": 4842 },
                { "dimensoes": { "mes": "Novembro", "raca": "Branca" }, "valor": 2239 },
                { "dimensoes": { "mes": "Novembro", "raca": "Preta" }, "valor": 1291 },
                { "dimensoes": { "mes": "Novembro", "raca": "Ignorado" }, "valor": 429 },
                { "dimensoes": { "mes": "Novembro", "raca": "Indígena" }, "valor": 104 },
                { "dimensoes": { "mes": "Novembro", "raca": "Amarela" }, "valor": 89 },

                { "dimensoes": { "mes": "Dezembro", "raca": "Parda" }, "valor": 4299 },
                { "dimensoes": { "mes": "Dezembro", "raca": "Branca" }, "valor": 2232 },
                { "dimensoes": { "mes": "Dezembro", "raca": "Preta" }, "valor": 1261 },
                { "dimensoes": { "mes": "Dezembro", "raca": "Ignorado" }, "valor": 454 },
                { "dimensoes": { "mes": "Dezembro", "raca": "Indígena" }, "valor": 100 },
                { "dimensoes": { "mes": "Dezembro", "raca": "Amarela" }, "valor": 90 }
            ]
            }
        ]
        }

    """

    _INSTRUCTION_GERAL_CONTINUACAO = """ 
    Você é um agente responsável por sugerir tipos de visualizações de dados e gerar os dados transformados para cada gráfico.

    Será fornecida as ultimas mensagens e a resposta correspondente em formato textual. Sua tarefa é analisar os dados retornados e gerar um JSON que contenha todas as visualizações possíveis, usando apenas os dados da resposta fornecida.

    Regras:

    1- As saídas devem ser consistentes: todos os gráficos devem usar os mesmos dados de entrada. Não crie gráficos de assuntos diferentes na mesma resposta.

    2- As opções de gráficos são: grafico_barras, grafico_linhas, mapas_coropleticos, graficos_com_proporcao.

    3- Para cada opção, forneça um score entre 0 e 1 indicando a relevância do gráfico para os dados.

    4- Cada visualização deve conter:
    4.1- tipo: nome do gráfico.

    4.2- score: peso de relevância.

    4.3- titulo: string contendo o título do gráfico.

    4.4- dados: array de objetos com:

    4.5- dimensoes: objeto com chaves representando dimensões.

    4.5.1- A primeira dimensão deve ser usada em um dos eixos do gráfico (x ou y) e ser a dimensão principal.

    4.5.2- A segunda dimensão deve indicar proporção/empilhamento nos gráficos de proporção ou cor/agrupamento nos outros gráficos.

    4.5.3- Se houver mais dimensões, inclua-as na ordem de importância para alterar cor ou agrupamento.

    4.5.4- valor: valor numérico associado à combinação de dimensões.

    5- Para gráficos de mapas_coropleticos, use os nomes de estados padronizados conforme o exemplo fornecido.

    6- Todos os dados da resposta devem ser adaptados para cada tipo de gráfico e mantidos consistentes entre as visualizações.

    7- Os gráficos de barras verticais e orizontais devem ter os mesmos dados na lista de dados do json
    
    8- Responda apenas com um JSON **puro**, **sem usar blocos de código Markdown** () ou quaisquer outros caracteres adicionais.
    
    9- Não inclua explicações, texto ou palavras fora do JSON.
    
    Exemplo de resposta (JSON puro):
    {
        "visualizacoes": [
            {
            "tipo": "grafico_barras_vertical",
            "score": 0.9,
            "titulo": "",
            "dados": [
                { "dimensoes": { "estado": "São Paulo" }, "valor": 18201 },
                { "dimensoes": { "estado": "Rio de Janeiro" }, "valor": 12361 },
                { "dimensoes": { "estado": "Pernambuco" }, "valor": 5251 },
                { "dimensoes": { "estado": "Pará" }, "valor": 4804 },
                { "dimensoes": { "estado": "Rio Grande do Sul" }, "valor": 4729 },
                { "dimensoes": { "estado": "Bahia" }, "valor": 4324 },
                { "dimensoes": { "estado": "Minas Gerais" }, "valor": 3799 },
                { "dimensoes": { "estado": "Amazonas" }, "valor": 3659 },
                { "dimensoes": { "estado": "Ceará" }, "valor": 3491 },
                { "dimensoes": { "estado": "Maranhão" }, "valor": 2492 },
                { "dimensoes": { "estado": "Paraná" }, "valor": 2201 },
                { "dimensoes": { "estado": "Santa Catarina" }, "valor": 1937 },
                { "dimensoes": { "estado": "Rio Grande do Norte" }, "valor": 1366 },
                { "dimensoes": { "estado": "Espírito Santo" }, "valor": 1350 },
                { "dimensoes": { "estado": "Mato Grosso do Sul" }, "valor": 1387 },
                { "dimensoes": { "estado": "Mato Grosso" }, "valor": 1151 },
                { "dimensoes": { "estado": "Paraíba" }, "valor": 1248 },
                { "dimensoes": { "estado": "Goiás" }, "valor": 1000 },
                { "dimensoes": { "estado": "Alagoas" }, "valor": 939 },
                { "dimensoes": { "estado": "Sergipe" }, "valor": 934 },
                { "dimensoes": { "estado": "Piauí" }, "valor": 745 },
                { "dimensoes": { "estado": "Rondônia" }, "valor": 570 },
                { "dimensoes": { "estado": "Acre" }, "valor": 528 },
                { "dimensoes": { "estado": "Roraima" }, "valor": 435 },
                { "dimensoes": { "estado": "Amapá" }, "valor": 406 },
                { "dimensoes": { "estado": "Distrito Federal" }, "valor": 337 },
                { "dimensoes": { "estado": "Tocantins" }, "valor": 217 }
            ]
            },
            {
            "tipo": "grafico_barras_horizontal",
            "score": 0.9,
            "titulo": "",
            "dados": [
                { "dimensoes": { "estado": "São Paulo" }, "valor": 18201 },
                { "dimensoes": { "estado": "Rio de Janeiro" }, "valor": 12361 },
                { "dimensoes": { "estado": "Pernambuco" }, "valor": 5251 },
                { "dimensoes": { "estado": "Pará" }, "valor": 4804 },
                { "dimensoes": { "estado": "Rio Grande do Sul" }, "valor": 4729 },
                { "dimensoes": { "estado": "Bahia" }, "valor": 4324 },
                { "dimensoes": { "estado": "Minas Gerais" }, "valor": 3799 },
                { "dimensoes": { "estado": "Amazonas" }, "valor": 3659 },
                { "dimensoes": { "estado": "Ceará" }, "valor": 3491 },
                { "dimensoes": { "estado": "Maranhão" }, "valor": 2492 },
                { "dimensoes": { "estado": "Paraná" }, "valor": 2201 },
                { "dimensoes": { "estado": "Santa Catarina" }, "valor": 1937 },
                { "dimensoes": { "estado": "Rio Grande do Norte" }, "valor": 1366 },
                { "dimensoes": { "estado": "Espírito Santo" }, "valor": 1350 },
                { "dimensoes": { "estado": "Mato Grosso do Sul" }, "valor": 1387 },
                { "dimensoes": { "estado": "Mato Grosso" }, "valor": 1151 },
                { "dimensoes": { "estado": "Paraíba" }, "valor": 1248 },
                { "dimensoes": { "estado": "Goiás" }, "valor": 1000 },
                { "dimensoes": { "estado": "Alagoas" }, "valor": 939 },
                { "dimensoes": { "estado": "Sergipe" }, "valor": 934 },
                { "dimensoes": { "estado": "Piauí" }, "valor": 745 },
                { "dimensoes": { "estado": "Rondônia" }, "valor": 570 },
                { "dimensoes": { "estado": "Acre" }, "valor": 528 },
                { "dimensoes": { "estado": "Roraima" }, "valor": 435 },
                { "dimensoes": { "estado": "Amapá" }, "valor": 406 },
                { "dimensoes": { "estado": "Distrito Federal" }, "valor": 337 },
                { "dimensoes": { "estado": "Tocantins" }, "valor": 217 }
            ]
            },
            {
            "tipo": "mapas_coropleticos",
            "score": 0.9,
            "titulo": "",
            "dados": [
                { "dimensoes": { "estado": "São Paulo" }, "valor": 18201 },
                { "dimensoes": { "estado": "Rio de Janeiro" }, "valor": 12361 },
                { "dimensoes": { "estado": "Pernambuco" }, "valor": 5251 },
                { "dimensoes": { "estado": "Pará" }, "valor": 4804 },
                { "dimensoes": { "estado": "Rio Grande do Sul" }, "valor": 4729 },
                { "dimensoes": { "estado": "Bahia" }, "valor": 4324 },
                { "dimensoes": { "estado": "Minas Gerais" }, "valor": 3799 },
                { "dimensoes": { "estado": "Amazonas" }, "valor": 3659 },
                { "dimensoes": { "estado": "Ceará" }, "valor": 3491 },
                { "dimensoes": { "estado": "Maranhão" }, "valor": 2492 },
                { "dimensoes": { "estado": "Paraná" }, "valor": 2201 },
                { "dimensoes": { "estado": "Santa Catarina" }, "valor": 1937 },
                { "dimensoes": { "estado": "Rio Grande do Norte" }, "valor": 1366 },
                { "dimensoes": { "estado": "Espírito Santo" }, "valor": 1350 },
                { "dimensoes": { "estado": "Mato Grosso do Sul" }, "valor": 1387 },
                { "dimensoes": { "estado": "Mato Grosso" }, "valor": 1151 },
                { "dimensoes": { "estado": "Paraíba" }, "valor": 1248 },
                { "dimensoes": { "estado": "Goiás" }, "valor": 1000 },
                { "dimensoes": { "estado": "Alagoas" }, "valor": 939 },
                { "dimensoes": { "estado": "Sergipe" }, "valor": 934 },
                { "dimensoes": { "estado": "Piauí" }, "valor": 745 },
                { "dimensoes": { "estado": "Rondônia" }, "valor": 570 },
                { "dimensoes": { "estado": "Acre" }, "valor": 528 },
                { "dimensoes": { "estado": "Roraima" }, "valor": 435 },
                { "dimensoes": { "estado": "Amapá" }, "valor": 406 },
                { "dimensoes": { "estado": "Distrito Federal" }, "valor": 337 },
                { "dimensoes": { "estado": "Tocantins" }, "valor": 217 }
            ]
            },
            {
            "tipo": "graficos_linhas",
            "score": 0.1,
            "titulo": "",
            "dados": [
                { "dimensoes": { "numMes": 1, "mes": "Janeiro" }, "valor": 5333 },
                { "dimensoes": { "numMes": 2, "mes": "Fevereiro" }, "valor": 6205 },
                { "dimensoes": { "numMes": 3, "mes": "Março" }, "valor": 7194 },
                { "dimensoes": { "numMes": 4, "mes": "Abril" }, "valor": 6731 },
                { "dimensoes": { "numMes": 5, "mes": "Maio" }, "valor": 6748 },
                { "dimensoes": { "numMes": 6, "mes": "Junho" }, "valor": 7102 },
                { "dimensoes": { "numMes": 7, "mes": "Julho" }, "valor": 7576 },
                { "dimensoes": { "numMes": 8, "mes": "Agosto" }, "valor": 8241 },
                { "dimensoes": { "numMes": 9, "mes": "Setembro" }, "valor": 8162 },
                { "dimensoes": { "numMes": 10, "mes": "Outubro" }, "valor": 7946 },
                { "dimensoes": { "numMes": 11, "mes": "Novembro" }, "valor": 8159 },
                { "dimensoes": { "numMes": 12, "mes": "Dezembro" }, "valor": 8052 }
            ]
            },
            {
            "tipo": "graficos_com_proporcao",
            "score": 0.7,
            "titulo": "",
            "dados": [
                { "dimensoes": { "mes": "Janeiro", "raca": "Parda" }, "valor": 4847 },
                { "dimensoes": { "mes": "Janeiro", "raca": "Branca" }, "valor": 2378 },
                { "dimensoes": { "mes": "Janeiro", "raca": "Preta" }, "valor": 1282 },
                { "dimensoes": { "mes": "Janeiro", "raca": "Ignorado" }, "valor": 524 },
                { "dimensoes": { "mes": "Janeiro", "raca": "Amarela" }, "valor": 100 },
                { "dimensoes": { "mes": "Janeiro", "raca": "Indígena" }, "valor": 97 },

                { "dimensoes": { "mes": "Fevereiro", "raca": "Parda" }, "valor": 3916 },
                { "dimensoes": { "mes": "Fevereiro", "raca": "Branca" }, "valor": 2094 },
                { "dimensoes": { "mes": "Fevereiro", "raca": "Preta" }, "valor": 1072 },
                { "dimensoes": { "mes": "Fevereiro", "raca": "Ignorado" }, "valor": 421 },
                { "dimensoes": { "mes": "Fevereiro", "raca": "Amarela" }, "valor": 67 },
                { "dimensoes": { "mes": "Fevereiro", "raca": "Indígena" }, "valor": 70 },

                { "dimensoes": { "mes": "Março", "raca": "Parda" }, "valor": 5476 },
                { "dimensoes": { "mes": "Março", "raca": "Branca" }, "valor": 2687 },
                { "dimensoes": { "mes": "Março", "raca": "Preta" }, "valor": 1413 },
                { "dimensoes": { "mes": "Março", "raca": "Ignorado" }, "valor": 566 },
                { "dimensoes": { "mes": "Março", "raca": "Amarela" }, "valor": 117 },
                { "dimensoes": { "mes": "Março", "raca": "Indígena" }, "valor": 87 },

                { "dimensoes": { "mes": "Abril", "raca": "Parda" }, "valor": 4405 },
                { "dimensoes": { "mes": "Abril", "raca": "Branca" }, "valor": 2185 },
                { "dimensoes": { "mes": "Abril", "raca": "Preta" }, "valor": 1177 },
                { "dimensoes": { "mes": "Abril", "raca": "Ignorado" }, "valor": 461 },
                { "dimensoes": { "mes": "Abril", "raca": "Amarela" }, "valor": 87 },
                { "dimensoes": { "mes": "Abril", "raca": "Indígena" }, "valor": 71 },

                { "dimensoes": { "mes": "Maio", "raca": "Parda" }, "valor": 5154 },
                { "dimensoes": { "mes": "Maio", "raca": "Branca" }, "valor": 2494 },
                { "dimensoes": { "mes": "Maio", "raca": "Preta" }, "valor": 1391 },
                { "dimensoes": { "mes": "Maio", "raca": "Ignorado" }, "valor": 500 },
                { "dimensoes": { "mes": "Maio", "raca": "Indígena" }, "valor": 132 },
                { "dimensoes": { "mes": "Maio", "raca": "Amarela" }, "valor": 82 },

                { "dimensoes": { "mes": "Junho", "raca": "Parda" }, "valor": 4624 },
                { "dimensoes": { "mes": "Junho", "raca": "Branca" }, "valor": 2385 },
                { "dimensoes": { "mes": "Junho", "raca": "Preta" }, "valor": 1314 },
                { "dimensoes": { "mes": "Junho", "raca": "Ignorado" }, "valor": 429 },
                { "dimensoes": { "mes": "Junho", "raca": "Indígena" }, "valor": 96 },
                { "dimensoes": { "mes": "Junho", "raca": "Amarela" }, "valor": 79 },

                { "dimensoes": { "mes": "Julho", "raca": "Parda" }, "valor": 4928 },
                { "dimensoes": { "mes": "Julho", "raca": "Branca" }, "valor": 2333 },
                { "dimensoes": { "mes": "Julho", "raca": "Preta" }, "valor": 1307 },
                { "dimensoes": { "mes": "Julho", "raca": "Ignorado" }, "valor": 424 },
                { "dimensoes": { "mes": "Julho", "raca": "Indígena" }, "valor": 118 },
                { "dimensoes": { "mes": "Julho", "raca": "Amarela" }, "valor": 92 },

                { "dimensoes": { "mes": "Agosto", "raca": "Parda" }, "valor": 5311 },
                { "dimensoes": { "mes": "Agosto", "raca": "Branca" }, "valor": 2666 },
                { "dimensoes": { "mes": "Agosto", "raca": "Preta" }, "valor": 1480 },
                { "dimensoes": { "mes": "Agosto", "raca": "Ignorado" }, "valor": 540 },
                { "dimensoes": { "mes": "Agosto", "raca": "Indígena" }, "valor": 105 },
                { "dimensoes": { "mes": "Agosto", "raca": "Amarela" }, "valor": 80 },

                { "dimensoes": { "mes": "Setembro", "raca": "Parda" }, "valor": 4738 },
                { "dimensoes": { "mes": "Setembro", "raca": "Branca" }, "valor": 2330 },
                { "dimensoes": { "mes": "Setembro", "raca": "Preta" }, "valor": 1262 },
                { "dimensoes": { "mes": "Setembro", "raca": "Ignorado" }, "valor": 472 },
                { "dimensoes": { "mes": "Setembro", "raca": "Indígena" }, "valor": 91 },
                { "dimensoes": { "mes": "Setembro", "raca": "Amarela" }, "valor": 72 },

                { "dimensoes": { "mes": "Outubro", "raca": "Parda" }, "valor": 5043 },
                { "dimensoes": { "mes": "Outubro", "raca": "Branca" }, "valor": 2501 },
                { "dimensoes": { "mes": "Outubro", "raca": "Preta" }, "valor": 1337 },
                { "dimensoes": { "mes": "Outubro", "raca": "Ignorado" }, "valor": 467 },
                { "dimensoes": { "mes": "Outubro", "raca": "Indígena" }, "valor": 108 },
                { "dimensoes": { "mes": "Outubro", "raca": "Amarela" }, "valor": 104 },

                { "dimensoes": { "mes": "Novembro", "raca": "Parda" }, "valor": 4842 },
                { "dimensoes": { "mes": "Novembro", "raca": "Branca" }, "valor": 2239 },
                { "dimensoes": { "mes": "Novembro", "raca": "Preta" }, "valor": 1291 },
                { "dimensoes": { "mes": "Novembro", "raca": "Ignorado" }, "valor": 429 },
                { "dimensoes": { "mes": "Novembro", "raca": "Indígena" }, "valor": 104 },
                { "dimensoes": { "mes": "Novembro", "raca": "Amarela" }, "valor": 89 },

                { "dimensoes": { "mes": "Dezembro", "raca": "Parda" }, "valor": 4299 },
                { "dimensoes": { "mes": "Dezembro", "raca": "Branca" }, "valor": 2232 },
                { "dimensoes": { "mes": "Dezembro", "raca": "Preta" }, "valor": 1261 },
                { "dimensoes": { "mes": "Dezembro", "raca": "Ignorado" }, "valor": 454 },
                { "dimensoes": { "mes": "Dezembro", "raca": "Indígena" }, "valor": 100 },
                { "dimensoes": { "mes": "Dezembro", "raca": "Amarela" }, "valor": 90 }
            ]
            }
        ]
        }

    """
    
    def __init__(self, sql_query: str = "", final_answer: str = "", tipo_pergunta: str = "", last_messages = None):
        self.llm_service = LLM_service()
        self.sql_query = sql_query
        self.final_answer = final_answer
        self.tipo_pergunta=tipo_pergunta
        self.last_messages=last_messages
    
    async def create_json(self):
        if self.tipo_pergunta == "consulta_nova":
            suggested_json = await self.llm_service.ask_question(
                instructions=self._INSTRUCTION, 
                context=[f"resposta correspondente ao sql em formato textual: {self.final_answer}"], 
                question=self.sql_query
            )
        else:
            suggested_json = await self.llm_service.ask_question(
                instructions=self._INSTRUCTION_GERAL_CONTINUACAO, 
                context=[f"resposta correspondente ao sql em formato textual: {self.final_answer}"], 
                question=self.sql_query
            )
        
        # Tenta converter para objeto Python (dict)
        try:
            json.loads(suggested_json)
            return suggested_json
        except ValueError:
            return f"Resposta não é um JSON válido \n{suggested_json}\n"
    
        