import google.generativeai as genai

genai.configure(api_key="AIzaSyAsrD8NvkLnjgRxtX7I8F2-ROVW4UfURGM")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


convo = model.start_chat(history=[{
                                "role": "user",
                                "parts": [
                                    {
                                        "text": "Você me respondera como um especialista em video games e somente poderar aceitar perguntas que sejam relacionadas a este tema, caso contrário, responda com a seguinte frase \"Não consigo responder sobre esse tema, vamos falar sobre video games.\" Se você entendeu e consegue realizar as ações requisitadas responda com um \"okay\"",
                                    }
                                ],
                                },
                                {"role": "model", "parts": [{"text": "Okay! ️  Pode perguntar!"}]},
                            ])

while True:
    try:
        mensagem = input("Faça uma pergunta: ")
        convo.send_message(mensagem)
        print(convo.last.text)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")