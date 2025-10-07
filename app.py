from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    heroes = ["Motoyasu (Héroe De La Lanza)", "Ren (Héroe De La Espada)", "Itsuki (Héroe Del Arco)"]
    autor = "Naofumi Iwatani (Héroe Del Escudo)"
    return render_template("index.html", nombre = autor, heroes = heroes)
    
    
@app.route("/2")
def habilidades():
    habilidades_escudo = ["Escudo de Aire.", "Escudo Meteoro.", "Prisión de Escudo."]
    autor = "Naofumi Iwatani (Héroe Del Escudo)"
    return render_template("index2.html", nombre = autor, habilidades_escudo = habilidades_escudo)
    
    
@app.route("/3")
def utilidades():
    caracteristicas = ["Escudo De Aire crea un escudo traslucido de color verde en el aire que protege donde se invoque y resiste cierto daño.", "Escudo Meteoro usa los SP del usuario para resistir todo el daño que sea necesario, consumiendo mas y mas mientras se siga usando.", "Prisión De Escudo crea una esfera hecha de escudos que protege o encierra a quien este dentro según su uso."]
    autor = "Naofumi Iwatani (Héroe Del Escudo)"
    return render_template("index3.html", nombre = autor, caracteristicas = caracteristicas)

if __name__ == "__main__":
    app.run(debug=True)