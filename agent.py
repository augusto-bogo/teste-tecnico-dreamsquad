import os
from dotenv import load_dotenv
from strands import Agent 
from strands.models.ollama import OllamaModel
from strands_tools import calculator

load_dotenv()

ollama_model = OllamaModel(
    host= os.getenv("OLLAMA_URL"),
    model_id= os.getenv("OLLAMA_MODEL")        
)

agent = Agent(
    model=ollama_model,
    tools=[calculator],
    system_prompt=(
                     "Você é um assistente de IA útil e versátil. "
                     
                      "REGRAS DE DECISÃO PARA FERRAMENTAS:"
                      "1. Analise a intenção do usuário antes de agir."
                      "2. NÃO USE a ferramenta 'calculator' para perguntas sobre história, datas, fatos gerais, telefones ou códigos, mesmo que contenham números (ex: 'ano 1500', 'telefone 555-0199'). Nesses casos, responda apenas com texto."
                      "3. USE a ferramenta 'calculator' APENAS se a intenção for explicitamente realizar uma conta matemática (soma, subtração, conversão, raiz quadrada)."
                     
                     "INSTRUÇÕES DA CALCULADORA:"
                     "Se for necessário calcular: passe a expressão mantendo os operadores (+, -, *, /, **). "
                     "Para raiz quadrada use: sqrt(VALOR). "
                     "Jamais invente o resultado, use o retorno da ferramenta."
              )
)

