0. O que é um _buffer overflow_?

- Na memória (stack) o _layout_ fica assim, em ordem crescente de endereço (basta olhar para a função _main_):
  1. Espaço reservado para `buf[N]`;
  2. A variável `auth`, que é um `int` (inteiro) e ocupa 4 _bytes_ ou 32 _bits_;
  3. Outras coisas relacionadas a _padding_ e utilitários de execução (_framed pointer_, etc), mas que aqui não são importantes.

- Repara que se conseguires escrever para além da variável `buf` poderás modificar o valor de `auth` e fazer com que `win` execute e imprima o valor da _flag_ (o objetivo principal 🚀).

1. Identifica a vulnerabilidade

- A função `gets(buf)` lê sem limitar o tamanho, permitindo que um _buffer overflow_ aconteça;

- Assim, basta escrever mais do que N _bytes_ para o `buf` ser sobescrito e o valor de `auth` ser modificado para 1 (ou seja, `auth = 1`).

2. Prepara o _payload_

- Precisamos de encher os N primeiros _bytes_ do _buffer_ com qualquer caracter (pode ser `A` ou `B`, por exemplo);

- Depois, sobrepôr o valor de `auth` com 1. Repara que em C tudo o que não for 0 é considerado verdadeiro e, portanto, podes simplesmente escreve N+1 _bytes_ de qualquer coisa.

- Finalmente, acrescentar uma nova linha - isto, caso estejas a automatizar a injeção via um script.

3. Executa o _payload_

- Manualmente:
  - `AAAAAAAAAAAAAAAA1`, para um N = 16 (aquele 1 pode ser um A, também).
  - Aqui não precisas do `\n` porque o terminal já o adiciona automaticamente quando pressionas 'Enter'.

- Via _script_ de Python:
  - `python3 -c 'import sys; sys.stdout.buffer.write(b"A" * 16 + b"1\n")' | ./local` 
  - Ou `... | nc epl.di.uminho.pt 4004`.
