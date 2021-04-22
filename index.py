from flask import Flask, render_template

app = Flask(__name__, static_folder="templates")


@app.route("/")
def index():
    return render_template('Главная.html')


@app.route("/automobiles")
def auto():
    return render_template('Автомобили.html')


@app.route("/virtual_reality")
def vr():
    return render_template('Виртуальная-реальность.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template('Предложить-идею.html')


@app.route("/AI")
def ai():
    return render_template('Искусственный-интеллект.html')


@app.route("/gadgets")
def gadgets():
    return render_template('Гаджеты.html')


@app.route("/multimedia")
def multimedia():
    return render_template('Мультимедиа.html')


@app.route("/architecture")
def architecture():
    return render_template('Архитектура.html')


@app.route("/cafe")
def cafe():
    return render_template('Кафе-и-рестораны.html')


if __name__ == '__main__':
    db_session.global_init()
    session = db_session.create_session()
    if not session.query(User).first():
        import fill_base

    app.run(host='0.0.0.0', port=os.environ.get("PORT", 5000))

    app.run(port=8080, host='127.0.0.1')
