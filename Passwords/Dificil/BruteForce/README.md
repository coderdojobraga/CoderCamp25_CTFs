## Passwords - Difícil

Neste desafio o ninja deve descobrir a password usada para fazer login.

**Material**:
- Executável 'login' (Unix) ou 'login.exe' (Windows) e ficheiro 'passwords\.txt' 

**NOTAS**: 
- O programa login é um executável (escrito em C), para o terminal.
- Recebe uma password como argumento e verifica se é a certa. Nesse caso retorna a flag (# ./login <password>).
- O objetivo é utilizar força bruta para encontrar a password correta.
- Uma possível solução está no ficheiro 'solucao\.py', usando a biblioteca *subprocess* (corre o terminal).

**Password:** coderdojo
**Segredo:** CD25{passwords-forcabruta}