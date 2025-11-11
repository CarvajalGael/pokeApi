from flask  import Flask, render_template, request,redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'secreto'
API = "https://pokeapi.co/api/v2pokemon/"

@app.route("/")
def inicio():
    return render_template("/index.html")

@app.route("/search",methods=['POST'])
def search_pokemon():
    pokemom_name = request.form.get('pokemon_name', '').strip().lower()
    
    
    if not pokemon_mame:
        flash('Por favor, ingresa un nombre de pokemon.','error')
        return redirect(url_for('index'))

try:
    response = requests.get|

if __name__ == '__main__':
    app.run(debug=True)