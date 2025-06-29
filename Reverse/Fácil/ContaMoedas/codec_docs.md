# CODEC

(C) Marcos Bernardo da Silva Lobo (a110959@alunos.uminho.pt), 29/06/2025

O módulo **CODEC** *(Codifica/Descodifica)* utiliza um algoritmo próprio baseado numa sequência de operações aritméticas para encriptar e desencriptar srings.

## Função encriptar(texto)

Transforma os caracteres através da aplicação da operação **((j - 33 - 14) % 94) + 33** à *ordem* dos mesmos.

>NOTA: A função só funciona corretamente para caracteres ASCII imprimíveis (códigos 33 a 126).

## Função desencriptar(texto)

Reverte os caracteres através da aplicação da operação **((j - 33 + 14) % 94) + 33** à *ordem* dos caracteres encriptados.

>NOTA: A função só funciona corretamente para caracteres ASCII imprimíveis (códigos 33 a 126).