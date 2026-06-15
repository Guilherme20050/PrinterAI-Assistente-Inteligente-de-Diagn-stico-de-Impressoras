
# PrinterAI – Assistente Inteligente de Suporte Técnico

## Sobre o Projeto

O PrinterAI é um assistente virtual desenvolvido com foco em suporte técnico para impressoras.

A aplicação foi projetada para auxiliar usuários na identificação de problemas comuns e oferecer orientações claras e objetivas para resolução, reduzindo a necessidade de suporte especializado em situações simples.

---

## Objetivo

Fornecer uma solução eficiente, acessível e automatizada para diagnóstico inicial de falhas em impressoras.


---

## Funcionalidades

- Diagnóstico de problemas comuns (offline, atolamento, falha de impressão)
- Respostas baseadas em uma base de conhecimento estruturada
- Retorno seguro quando não há informação disponível
- Interface simples via terminal

---

## Como funciona

O assistente utiliza uma base de conhecimento em formato JSON e realiza a correspondência entre a pergunta do usuário e os problemas cadastrados.

Caso não encontre uma correspondência, retorna uma mensagem informando a ausência de dados confiáveis.

---

## Estrutura do Projeto

assistente-virtual-ia/
│
├── data/
│   └── problemas.json
│
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 03-prompts.md
│   └── 04-avaliacao.md
│
├── src/
│   └── chatbot.py
│
└── README.md

---

## Tecnologias Utilizadas

- Python 3
- JSON (base de conhecimento)
- Lógica de processamento de texto

---

## Como Executar

1. Clone o repositório: git clone https://github.com/seu-usuario/assistente-virtual-ia.git
2. Acesse a pasta: cd assistente-virtual-ia/src
3. Execute o projeto: python chatbot.py

---

## Possíveis Evoluções

- Integração com IA generativa (API)
- Interface web (Streamlit ou Flask)
- Expansão da base de conhecimento
- Tratamento de linguagem natural mais avançado

---

## Autor

Guilherme Gomes Augusto da Silva
Técnico Residente de Impressoras | Em evolução para Engenharia de Software



