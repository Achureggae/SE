class KnowledgeBase:
    def __init__(self):
        self.knowledge = {
            "Hola": "Hola! En que puedo ayudarte?",
            "Como estas": "Estoy bien, gracias por preguntar. Y tu?",
            "De que te gustaria hablar": "Puedo hablar de muchos temas! Que te interesa?"
        }

    def get_response(self, input_text):
        response = self.knowledge.get(input_text)
        if response:
            return response
        else:
            return "Lo siento, no entendi. Podrias proporcionar mas detalles?"

    def add_knowledge(self, question, answer):
        self.knowledge[question] = answer
        return "Nuevo conocimiento agregado correctamente."

knowledge_base = KnowledgeBase()

def chat():
    print("Bienvenido! Soy un chatbot. Puedes empezar escribiendo alguna de estas lineas: 'Hola', 'Como estas' o 'De que te gustaria hablar'.")

    while True:
        user_input = input("Tu: ")
        response = knowledge_base.get_response(user_input)

        if user_input.lower() == 'adios':
            print("Hasta luego!")
            break
        else:
            print("Bot:", response)
            if response == "Lo siento, no entendi. Podrias proporcionar mas detalles?":
                new_question = input("Bot: Cual es la pregunta adecuada para la respuesta? ")
                new_answer = input("Bot: Cual es la respuesta a esa pregunta? ")
                print(knowledge_base.add_knowledge(new_question, new_answer))

if __name__ == "__main__":
    chat()
