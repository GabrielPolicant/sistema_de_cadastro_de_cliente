# 📋 Sistema de Cadastro de Clientes

Aplicação desenvolvida em **Python** para gerenciamento de clientes através de uma interface de linha de comando (CLI).

O projeto foi desenvolvido com foco em praticar conceitos fundamentais de Python, organização de código em módulos, funções, estruturas de dados, validações, tratamento de exceções e criação de um sistema CRUD.

---

## 🚀 Funcionalidades

O sistema possui as seguintes operações:

* ✅ Cadastrar cliente
* 📄 Listar clientes cadastrados
* 🔎 Buscar cliente por **ID ou CPF**
* ✏️ Atualizar informações de um cliente
* 🗑️ Excluir cliente
* 🚪 Encerrar o sistema
* 🔐 Validação de CPF
* 📧 Validação de e-mail
* 🎂 Cálculo automático da idade
* 🖥️ Limpeza da tela de acordo com o sistema operacional
* 🎨 Mensagens coloridas para informações, erros e sucessos

---

## 🧩 Tecnologias utilizadas

* **Python 3**
* **Colorama** — estilização e cores no terminal
* **Datetime** — manipulação de datas e cálculo de idade
* **OS** — identificação do sistema operacional e limpeza do terminal
* **Time** — controle de pequenas pausas na interface

---

## 🏗️ Estrutura do projeto

```text
sistema-cadastro/
│
├── main.py
│
├── services/
│   └── client_services.py
│
├── utils/
│   └── auxiliares.py
│
└── README.md
```

### `main.py`

Responsável pelo fluxo principal da aplicação.

É onde o menu é apresentado e onde as operações de cadastro, consulta, atualização e exclusão são chamadas.

### `services/client_services.py`

Contém as principais regras relacionadas aos clientes:

* `cadastrar_cliente()`
* `listar_clientes()`
* `buscar_cliente()`
* `atualizar_cliente()`
* `excluir_cliente()`

### `utils/auxiliares.py`

Reúne funções auxiliares utilizadas pelo sistema, como:

* `log()`
* `limpar_tela()`
* `menu_option()`
* `validando_cpf()`
* `validando_email()`
* `formata_data()`
* `calcular_idade()`

---

## 💻 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Acesse a pasta do projeto

```bash
cd sistema-cadastro
```

### 3. Instale a dependência

O projeto utiliza a biblioteca `colorama`.

```bash
pip install colorama
```

### 4. Execute a aplicação

```bash
python main.py
```

---

## 📌 Exemplo do menu

```text
==============================
      SISTEMA DE CLIENTES
==============================
1 - Cadastrar Cliente
2 - Listar Clientes
3 - Buscar Cliente
4 - Atualizar Cliente
5 - Excluir Cliente
6 - Sair
==============================
Escolha uma opção:
```

---

## 👤 Dados do cliente

Durante o cadastro, o sistema solicita:

```text
Nome
CPF
Email
Telefone
Data de Nascimento
```

A idade é calculada automaticamente a partir da data de nascimento informada.

---

## 🔐 Validações

O sistema possui algumas validações para evitar dados inconsistentes.

### CPF

A aplicação:

* Remove pontos e hífen;
* Verifica se possui 11 dígitos;
* Verifica se os dígitos são numéricos;
* Impede CPFs com todos os números iguais;
* Calcula e valida os dígitos verificadores;
* Verifica se o CPF já está cadastrado.

### E-mail

A aplicação verifica:

* Se o campo foi preenchido;
* Se o e-mail já está cadastrado;
* Se contém `@` e `.`.

---

## 🧠 Conceitos praticados

Este projeto foi desenvolvido como prática de fundamentos de programação em Python, utilizando conceitos como:

* Funções
* Dicionários
* Listas
* Estruturas condicionais
* Laços de repetição
* `try/except`
* Manipulação de strings
* Validação de dados
* Modularização
* Importação de módulos
* Separação de responsabilidades
* CRUD
* Manipulação de datas
* Interação com o terminal

---

## ⚠️ Observação

Atualmente, os clientes são armazenados **somente em memória**, utilizando listas e dicionários.

Isso significa que os dados cadastrados são perdidos quando a aplicação é encerrada.

Como próximos passos, o projeto pode evoluir para utilizar:

* 💾 Banco de dados
* 🌐 API REST
* 🗃️ SQLAlchemy
* 🔑 Autenticação
* 🧪 Testes automatizados
* 📝 Logs estruturados
* 🖥️ Interface gráfica ou aplicação web

---

## 🎯 Objetivo do projeto

O objetivo principal deste projeto é colocar em prática conceitos de **Python e desenvolvimento de sistemas**, simulando uma aplicação de cadastro de clientes com operações CRUD e validações de dados.

O projeto também serve como base para futuras evoluções, principalmente na integração com **banco de dados, APIs e frameworks web**.

---

## 👨‍💻 Autor

Desenvolvido por **Gabriel Policant**.

Projeto criado para estudos e evolução prática em **Python, desenvolvimento de software e automação**.
