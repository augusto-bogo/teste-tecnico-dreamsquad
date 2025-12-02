# Desafio API de Chat com Agente de IA - DreamSquad

Este readme contém a implementação do Desafio Técnico de Estágio em IA da DreamSquad.

## Descrição do Desafio

Desenvolver uma API de Chat simples que se conecta a um Agente de IA. O Agente deve ser configurado para utilizar uma tool de Cálculo Matemático para resolver operações. 
O projeto deve ser configurado para ser executado localmente com Ollama como LLM.

## Requisitos do Sistema

* Python 3.10 ou superior
* Git
* Ollama (para execução do LLM local)

##  Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento.

### 1. Clonar o Repositório

```bash
git clone https://github.com/augusto-bogo/teste-tecnico-dreamsquad.git
cd teste-tecnico-dreamsquad
````

### 2\. Configurar o Ambiente Virtual

Crie e ative um ambiente virtual para isolar as dependências:

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3\. Instalar Dependências

Instale os pacotes listados no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

O projeto já inclui um arquivo de modelo chamado `.env.example` com as variáveis necessárias. Para configurar seu ambiente local, basta criar uma cópia deste arquivo renomeando-a para `.env`.

Execute o comando abaixo de acordo com seu sistema:

**Linux/macOS:**
```bash
cp .env.example .env
```


## Configuração do Ollama

O projeto utiliza o Ollama para rodar o modelo de linguagem localmente.

1.  Baixe e instale o Ollama em [ollama.com](https://ollama.com/download).
2.  Após instalar, abra o terminal e baixe o modelo utilizado no projeto (Llama 3.1 8b):

<!-- end list -->

```bash
ollama pull llama3.1:8b
```


## Execução

Para iniciar o servidor da API, execute o comando:

```bash
uvicorn main:app --reload
```

Documentação Interativa 

Você pode testar diretamente pelo navegador acessando:
``http://127.0.0.1:8000/docs``
