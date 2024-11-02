# Totalização simples de vendas de produtos

**Descrição do Projeto**\
Este projeto estará baseado na leitura de um arquivo texto de entrada contendo código, quantidade e valor unitário de produtos 
vendidos. O conteúdo deste arquivo estará formatado como CSV (Comma Separated Values).\
Ele terá o nome VENDAS.CSV e conterá dados conforme o layout mostrado abaixo. Nos campos numéricos reais lembre-se de usar o 
caractere ponto (.) como separador decimal.: 

19200;120;7.22\
19800;68;3.52\
14300;123;4.24\
16700;115;10.76\
15400;119;2.76\
18700;51;5.24\
...

Como pode ser visto acima, cada linha do arquivo refere-se a um produto vendido. Para os testes do programa utilize o arquivo de 
dados fornecido pelo professor juntamente com este enunciado. As informações de cada linha do arquivo estão descritas na tabela:

| Posição | Informação        | Formato             | Observações                                              |
|:--------|:------------------|:--------------------|:---------------------------------------------------------|
| (1)     | Código do produto | 5 dígitos numéricos | Os códigos de produtos serão números entre 10000 e 21000 |
| (2)     | Quantidade        | Número inteiro      |                                                          |
| (3)     | Preço unitário    | Número Real         |                                                          |

**Pede-se neste Projeto Programa**
- O programa deve ler os dados do arquivo de entrada e carregá-los em memória usando listas do Python 3. Procurem pensar em 
uma forma esperta de fazer isso e descrevam através de comentários no código do programa o que elaboraram.  
- Após a leitura o programa deve calcular e mostrar na tela o total geral vendido (somatória de todas as Quantidades x Preço 
Unitário).  
- Em seguida deve permanecer em laço enquanto não for digitado zero (0). Para cada repetição do laço deve-se ler um código de 
produto, obrigatoriamente no intervalo [10000 e 21000] e mostrar na tela o total vendido para aquele produto. 
