class Conocimientos:
    def __init__(self):
        self.conocimiento = {
            "Hola": "Hola! En que puedo ayudarte?",
            "Como estas": "Estoy bien, gracias por preguntar. Y tu?",
            "De que te gustaria hablar": "Puedo hablar de muchos temas! Que te interesa?"
        }

    def ObtenerRespuesta(self, entrada):
        respuesta = self.conocimiento.get(entrada)
        if respuesta:
            return respuesta
        else:
            return "Lo siento, no entendi. Podrias proporcionar mas detalles?"

    def AdquirirConocimiento(self, pregunta, resultado):
        self.conocimiento[pregunta] = resultado
        return "Nuevo conocimiento agregado correctamente."

AdquirirConocimientos = Conocimientos()

def chat():
    print("Bienvenido! Soy un chatbot. Puedes empezar escribiendo alguna de estas lineas: 'Hola', 'Como estas' o 'De que te gustaria hablar'.")

    while True:
        EntradaUsuario = input("Tu: ")
        respuesta = AdquirirConocimientos.ObtenerRespuesta(EntradaUsuario)

        if EntradaUsuario.lower() == 'adios':
            print("Hasta luego!")
            break
        else:
            print("Bot:", respuesta)
            if respuesta == "Lo siento, no entendi. Podrias proporcionar mas detalles?":
                PreguntaNueva = input("Bot: Cual es la pregunta adecuada para la respuesta? ")
                RespuestaNueva = input("Bot: Cual es la respuesta a esa pregunta? ")
                print(AdquirirConocimientos.AdquirirConocimiento(PreguntaNueva, RespuestaNueva))

if __name__ == "__main__":
    chat()
