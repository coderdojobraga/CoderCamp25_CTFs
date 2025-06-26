**Explicação:** Foi descoberto que o Champion do Coder Dojo está a guardar um segredo de todos nós. Descobrires este segredo vai te permitir resolver este desafio! Os mentores do CoderCamp conseguiram obter alguma informação do Computador do Hélder! Agora cabe-te a ti descobrires que informação podes retirar do computador dele. Para além disso, descobrimos o site pessoal do Hélder, onde ele guarda alguns segredos que descobre. Suspeitamos que seja neste site que ele guarda informações muito importantes sobre o segredo que queres descobrir.

**Solução:** O website pede um login com utilizador e password. Para descobrir o nome de utilizador, o ninja precisa de vasculhar o diário do Hélder, onde está guardada, em algum dia, a informação de que o username é helderg04. É importante usar o Ctrl+F para facilitar a procura.

Para descobrir a password, já há mais passos. Primeiro, é necessário encontrar o ficheiro segredo.txt, que contém informação em código binário. O código binário indica que a password é o animal favorito dele e a cor favorita dele.

Para saber a cor favorita, é preciso voltar ao diário e pesquisar sobre a cor favorita usando Ctrl+F. Para descobrir o animal favorito, é necessário encontrar a pasta com imagens de animais. Esta pasta tem imagens de três animais. Agora, é preciso analisar os metadados de cada imagem. Na imagem do mocho, há um metadado com texto que informa que o mocho é o animal favorito dele.

A password do site é mochoroxo (podendo ser escrita como mochoroxo, MochoRoxo ou Mochoroxo).

Agora, já dentro do site, é falado sobre Base64 e sobre o site CyberChef, que permite fazer decode de, por exemplo, texto codificado em Base64.

Para saber onde está o texto que temos de decodificar, é preciso ler o website, onde é dito que ele descobriu a existência de Base64 num ficheiro de vírus antigo que encontrou.

Ir à pasta Coisas Antigas/2023 e descobrir o ficheiro virus.vir. Neste ficheiro temos a flag codificada em Base64. Fazer decode e obter a flag em plaintext.

**Site:** https://diog0martins.github.io/segredodochampion/

**Solução:** CD25{estas a tornar-te num bom hacker}
