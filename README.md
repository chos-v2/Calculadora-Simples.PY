# 🐍 Calculadora Simples em Python (CLI)

Este é um projeto simples de calculadora desenvolvido em Python para praticar os fundamentos da linguagem, com foco em estruturação de código, tratamento de exceções e modularização.

## ✨ Funcionalidades

A calculadora opera via Linha de Comando (CLI) e é capaz de realizar as seguintes operações:

* Soma (`+`)
* Subtração (`-`)
* Multiplicação (`*`)
* Divisão (`/`)

## 🛠️ Conceitos e Abordagem

O projeto foi estruturado para demonstrar o domínio dos seguintes conceitos:

* **Modularização:** O código principal (`Principal.py`) e a lógica de cálculo (`Modulo_calculo.py`) foram separados em módulos diferentes para melhorar a organização e o reuso.
* **Tratamento de Exceções (`try-except`):**
    * Lida com erros de **`ValueError`** (quando o usuário digita letras em vez de números).
    * Lida com erros de **`ZeroDivisionError`** (impedindo a quebra do programa na divisão por zero).
* **Controle de Fluxo:** Uso eficiente de **`while True`** e **`break/continue`** para criar *loops* robustos de repetição e validação de entrada (números e operadores).
* **Funções:** Uso de `def` para encapsular a lógica de cálculo (função `Calculadora`) e a formatação visual (função `ponto`).

## ⚙️ Como Executar

1.  Certifique-se de ter o Python instalado.
2.  Clone o repositório:
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    ```
3.  Execute o arquivo principal:
    ```bash
    python Principal.py
    ```

***
