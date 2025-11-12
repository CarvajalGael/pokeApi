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
    
    
    if not pokemon_name:
        flash('Por favor, ingresa un nombre de pokemon.','error')
        return redirect(url_for('index'))

try:
    resp = requests.get(f"{API}{pokemon_name}")
    if resp.status_code == 200:
        pokemon_data = resp.json()
        return render_template('pokemon.html', pokemon=pokemon_data)
    else:
        flash(f'Pokémon "{pokemon_name}" no encontrado', 'error')
        return redirect(url_for('index'))
except requests.exceptions.RequestException as e:
    flash('Error al buscar el Pokémon', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)