import os
from groq import Groq

# Defina a chave da API diretamente no código ou garanta que ela esteja configurada no ambiemte
os.environ["GROQ_API_KEY"] = "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"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Inicializa a lista de mensagens para manter o contexto da conversa 
messages = [ ]

while True:
    usuario = input("Digite uma mensagem ou 'sair' para encerrar: ")
    
    if usuario.lower() == 'sair':
        print("Conversa encerrada.")
        break
    
    # Adiciona a mensagem do usuário à lista de mensagens 
    messages.append({"role": "user", "content": usuario})
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.1-70b-versatile",
    )
    
    resposta = chat_completion.choices[0].message.content
    print("Resposta:", resposta)
    
    # Adiciona a resposta do assistente à lista de mensagens para manter o contexto
    messages.append({"role": "assistant", "content": resposta})