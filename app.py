from flask import Flask, render_template, request, redirect, url_for
import random
from capitulos import capitulo1, capitulo2, capitulo3, capitulo4, capitulo5, capitulo6, capitulo7, capitulo8, capitulo9

app = Flask(__name__)

capitulos = {
    "1": capitulo1,
    "2": capitulo2,
    "3": capitulo3,
    "4": capitulo4,
    "5": capitulo5,
    "6": capitulo6,
    "7": capitulo7,
    "8": capitulo8,
    "9": capitulo9,
    "geral": capitulo1 + capitulo2 + capitulo3 + capitulo4 + capitulo5 + capitulo6 + capitulo7 + capitulo8 + capitulo9
}

@app.route('/')
def indice():
    # Criar dicionário com número máximo de perguntas por capítulo
    max_por_capitulo = {k: len(v) for k, v in capitulos.items()}
    return render_template('index.html', capitulos=capitulos, max_por_capitulo=max_por_capitulo)


@app.route('/teste', methods=['POST'])
def teste():
    capitulo = request.form['capitulo']
    total = int(request.form['total'])

    perguntas = capitulos[capitulo].copy()
    random.shuffle(perguntas)
    perguntas = perguntas[:total]

    return render_template("teste.html", perguntas=perguntas, total=total)

@app.route('/resultado', methods=['POST'])
def resultado():
    total = int(request.form['total'])
    acertos = 0

    for i in range(total):
        certa = request.form.get(f'resposta_certa_{i}')
        marcada = request.form.get(f'resposta_{i}')
        if marcada == certa:
            acertos += 1

    percentual = (acertos / total) * 100
    return render_template("resultado.html", acertos=acertos, total=total, percentual=percentual)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
