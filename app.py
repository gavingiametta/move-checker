from flask import Flask, render_template, request
from functions import get_pokemon_moves, pokemon_weaknesses, is_move_strong, format_move_list


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/submit-search', methods=['GET', 'POST'])
def submit_form():
    if request.method == "GET":
        return render_template("results.html")

    form_data = request.form
    user_pokemon_name = form_data['user_pokemon']
    enemy_pokemon_name = form_data['enemy_pokemon']

    strong_moves = []
    move_list = get_pokemon_moves(enemy_pokemon_name)
    weakness_list = pokemon_weaknesses(user_pokemon_name)

    for move in move_list:
        if is_move_strong(move, weakness_list) is True:
            strong_moves.append(move)

    return render_template("results.html", strong_moves=format_move_list(strong_moves))


if __name__ == '__main__':
    app.run()
