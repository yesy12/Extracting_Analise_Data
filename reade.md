1. Primeiro passo.

Roda este comando abaixo
choco install selenium-all-drivers

2. Segundo passo
pip install requirements.txt

3. Terceiro passo
python startAll.py

4. Quarto passo
python .\Extracting_Data\start.py


Objetivos
[-] Obter Dados
    [X] Salvar game no Banco de Dados
    [ ] Selecionar lingua ao salvar o review
    [X] Likes
        [X] Util
        [X] Engraçada
        [X] Emoticon
    [X] Votes
        [X] Recomendado
        [X] Horas
    [X] Review
        [-] Review Completo 
            - Evitar duplicado
        [X] Dia Publicado
    [X] Informação do Player
        [X] Link do player
        [-] Quantidade de games publico
            - Um jeito de pegar a quantidade de games do jogador
        [-] Quantidade de comentarios total
        [-] Comentarios
            [X] Comentarios página 1
            [ ] Comentarios de outras páginas
            [ ] Contabilizar a quantidade de comentarios do review com a quantidade que foi publicada em todas as paginas
            [ ] Resolver erro, Pegar a data quando o comentario foi publicado
    [-] Review
        [  ] Resolver erro das classes que obtem os dados

[ ] Pandas
[ ] IA
    [ ] Analisar publicações
        - Entre Super Negativo, Negativo,  Normal, Engraçada, Super Engraçada, Positiva, Super Positiva
    [ ] Analisar comentários
        - Super inútil, inútil, útil, super util

[ ] Ferramentas de testes
    [ ] Likes Emoticon, Funny, Util
    [ ] Recomendado e Horas
    [ ] Comentarios 
        [ ] Data e Comentario
    [ ] Link Players, Quantify Game e Quantify Comment
    [ ] Abrir nova aba
    [ ] Salvar coisas no Database
    [ ] Functions
    


Links https://www.selenium.dev/
Links https://chocolatey.org/install