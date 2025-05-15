# 📦Projeto Controle de Estoque - Instituto Joga Junto

## 📝Descrição  
Aplicação para controle de estoque que permite gerenciar produtos e movimentações de entrada e saída. O sistema visa tornar a experiência de colaboradores o mais intuitiva possível, garantindo que os produtos sejam catalogados e navegados facilmente.

O projeto conta com testes manuais e automatizados utilizando Selenium WebDriver, BDD com Behave, e geração de dados dinâmicos com Faker.


## 🛠️Tecnologias e Ferramentas

- Python  
- Selenium WebDriver  
- Behave (BDD)  
- Faker  
- Python-dotenv  
- Requests  
- Logging personalizado (`utils/logger_config`)


## 🐍Dependências Python

- selenium  
- behave  
- faker  
- python-dotenv  
- requests


## 🧱Arquitetura da Aplicação  
O projeto segue o padrão **Page Object Model (POM)** para organizar os testes, facilitando a manutenção e reutilização. Cada página da aplicação é representada por uma classe que encapsula os elementos da interface e as ações possíveis.

📂**Exemplo de estrutura:**  
`pages/register_user_page.py` representa a página de cadastro de usuário.


## 🔁 Fluxo dos Testes

1. Preparação do ambiente e carregamento das variáveis do arquivo `.env`.  
2. Execução dos passos definidos nos arquivos `.feature` com Behave.  
3. Interação com a aplicação via Selenium WebDriver através das classes do POM.  
4. Geração de dados dinâmicos com Faker para testes realistas.  
5. Validação dos resultados e registro dos logs via logger personalizado.

---

## 🪵Logger Personalizado  
O logger customizado configurado em `utils/logger_config.py` é usado para:  
- Registrar informações úteis durante a execução dos testes.  
- Ajudar na depuração e análise dos resultados.  
- Capturar exceções e erros com mensagens claras.



## 🔐Variáveis de Ambiente Necessárias

```env
VALID_EMAIL_LOGIN=usuario_valido@email.com
VALID_PASSWORD_LOGIN=senha_valida

INVALID_EMAIL_LOGIN=email_invalido@email.com
INVALID_PASSWORD_LOGIN=senha_invalida

VALID_EMAIL_REGISTER= 
INVALID_EMAIL_REGISTER=email_invalido_para_cadastro.com
PASSWORD_REGISTER=senha_de_cadastro
CONFIRM_PASSWORD_REGISTER=senha_de_cadastro
WRONG_CONFIRM_PASSWORD_REGISTER=senha_diferente

NAME_PRODUCT=Nome do Produto
DESCRIPTION_PRODUCT=Descrição detalhada do produto para testes
PRICE_PRODUCT=0.00
PATH_IMAGE=caminho/para/imagem/do_produto.webp
SHIPMENT_PRODUCT=0.00

URL_WEB=https://url-da-aplicacao-web.com/
LOGIN_URL=https://url-da-api.com/login
PRODUCTS_URL=https://url-da-api.com/produtos
```

## ⚙️Instalar Dependências

Para rodar os testes, você precisa instalar as bibliotecas usadas no projeto. Execute o seguinte comando no terminal para instalar as dependências necessárias:

```bash
pip install selenium behave faker python-dotenv requests
```

## ▶️Como Rodar os Testes

Configure o arquivo `.env` com as variáveis necessárias.

Execute os testes com o Behave:

```bash
behave
```

## 🎯Informações do Projeto

### Objetivo do Produto

O sistema de controle de estoque do Instituto Joga Junto busca facilitar a catalogação e navegação dos produtos para colaboradores, otimizando tempo e recursos, e promovendo uma boa experiência.

### 👤Objetivos e Valores do Stakeholder (Persona)

- Multinacional do ramo têxtil com clientes globais.
- Necessidade de manipulação de informações em múltiplos idiomas.
- Fortalecer o senso de equipe e orgulho pela marca com identidade visual consistente.
- Navegação simples e eficiente para diversas categorias e tipos de produtos.
- Otimização das ações das equipes de estoque e vendas.

### 📋Principais Regras de Negócio

| Código  | Requisito                                      |
|---------|------------------------------------------------|
| RF0001  | Impedir cadastro de usuário externo            |
| RF0002  | Login com e-mail e senha                       |
| RF0003  | Cadastro de usuário só pelo administrador      |
| RF0004  | Cadastro de produtos                           |
| RF0005  | Edição de produtos                             |
| RF0006  | Filtragem por categoria                        |
| RF0007  | Filtragem por preço                            |
| RF0008  | Exclusão de produtos                           |
| RF0009  | Exibir dados do usuário no perfil              |
| RF0010  | Atualizar quantidade após transação            |
| RF0011  | Acompanhamento de pedidos e prazos             |
| RF0012  | Registro detalhado de transações               |
| RF0013  | Suporte a múltiplos idiomas                    |

### ⚙️Requisitos Não Funcionais

| Código  | Descrição                                               |
|---------|---------------------------------------------------------|
| NF0001  | Sistema disponível em múltiplos idiomas                 |
| NF0002  | Identidade visual da marca presente em todos os elementos |
| NF0003  | Interface intuitiva e simples de usar                   |
| NF0004  | Integração com sistemas de vendas e financeiro         |

## 📚Documentações Relacionadas

- [Plano de Teste](https://docs.google.com/spreadsheets/d/1F2JOvuMtzlURWD06VXXnPGN0eu1ET4UTC-nFjh0N_tY/edit?gid=151555461#gid=151555461)
- [Bug Report](https://docs.google.com/spreadsheets/d/1uJmNWskikRXjc0_1HuhvhR6ixNTKSGzvPXVIpYbUFlc/edit?gid=222628309#gid=222628309)
- [Relatório Cobertura de Teste](https://1drv.ms/w/c/d91b9bb6cccd1fbc/ERHzSKQYi05Jo8gLyCKcvEMBZg2cWnq85xQtIVSSLPD8PA)
- [Estatísticas de Teste](https://docs.google.com/spreadsheets/d/1IKI5TDvlIqlyjtnArTqyc1arp5TtURiaR4Y1tKIrOrU/edit?gid=216178387#gid=216178387)

