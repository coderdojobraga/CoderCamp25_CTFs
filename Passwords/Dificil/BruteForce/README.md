## Passwords - Difícil

Neste desafio o ninja deve descobrir a password usada para fazer login.

**Material**:
- Executável 'login' (Unix) ou 'login.exe' (Windows) e ficheiro 'passwords\.txt' 

**NOTAS**: 
- O programa login é um executável (escrito em C), para o terminal.
- Recebe uma password como argumento e verifica se é a certa:
    - Caso a password estaja certa é retornada a string "A password ... está correta!";
    - Caso a password estaja errada é retornada a string "A password ... está incorreta!";
- O objetivo é utilizar força bruta para encontrar a password correta.
- Uma possível solução está no ficheiro 'solucao\.py', usando a biblioteca *subprocess* (corre o terminal).
- Quando a password está certa, o executável retorna a string "Flag: CD25{...}"
- Caso não seja dada uma password, o executável retorna a string "# ./login <password>";

**Password:** coderdojo
**Flag:** CD25{passwords-forcabruta}