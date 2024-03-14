import json

class Conocimientos:
    def __init__(self):
        self.conocimiento = {
            "Hola": "Hola! En que puedo ayudarte?",
            "Como estas": "Bien, gracias, Y tu?",
            "De que te gustaria hablar": "Puedo hablar de muchos temas! Que te interesa?"
        }

    def ObtenerRespuesta(self, entrada):
        respuesta = self.conocimiento.get(entrada)
        if respuesta:
            return respuesta
        else:
            return "No entendí la pregunta o no cuento con información, ¿me ayudas a entender?"

    def AdquirirConocimiento(self, pregunta, resultado):
        self.conocimiento[pregunta] = resultado
        return "Conocimiento agregado correctamente."

    def GuardarDiccionario(self):
        Archivo = "Conocimiento.txt"
        with open(Archivo, "w") as archivo:
        json.dump(self.conocimiento, archivo)

AdquirirConocimientos = Conocimientos()

def chat():
    print("Bienvenido! Soy un chatbot. Puedes empezar escribiendo alguna de estas lineas: 'Hola', 'Como estas' o 'De que te gustaria hablar'.")

    while True:
        EntradaUsuario = input("Tu: ")
        respuesta = AdquirirConocimientos.ObtenerRespuesta(EntradaUsuario)

        if EntradaUsuario.lower() == 'adios':
            print("Hasta luego!")
            AdquirirConocimientos.GuardarDiccionario
            break
        else:
            print("Bot:", respuesta)
            if respuesta == "No entendí la pregunta o no cuento con informacion, ¿me ayudas a entender?":
                PreguntaNueva = input("Bot: Cual es la pregunta adecuada para la respuesta? ")
                RespuestaNueva = input("Bot: Cual es la respuesta a esa pregunta? ")
                print(AdquirirConocimientos.AdquirirConocimiento(PreguntaNueva, RespuestaNueva))

if __name__ == "__main__":
    chat()
