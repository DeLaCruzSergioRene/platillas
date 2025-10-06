from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    heroes = ["Motoyasu (Héroe De La Lanza)", "Ren (Héroe De La Espada)", "Itsuki (Héroe Del Arco)"]
    autor = "Naofumi Iwatani (Héroe Del Escudo)"
    
    return render_template("index.html", nombre = autor, heroes = heroes)
if __name__ == "__main__":
    app.run(debug=True)
    
    
@app.route("/2")
def index():
    habilidades_escudo = ["Escudo de Aire", "Escudo Meteoro", "Prisión de Escudo"]
    autor = "Naofumi Iwatani (Héroe Del Escudo)"
    
    return render_template("index2.html", nombre = autor, habilidades_escudo = habilidades_escudo)
if __name__ == "__main__":
    app.run(debug=True)
    
    
@app.route("/3")
def index():
    caracteristicas = ["Motoyasu (Héroe De La Lanza)", "Ren (Héroe De La Espada)", "Itsuki (Héroe Del Arco)"]
    autor = "Naofumi Iwatani (Héroe Del Escudo)"
    
    return render_template("index3.html", nombre = autor, caracteristicas = caracteristicas)
if __name__ == "__main__":
    app.run(debug=True)