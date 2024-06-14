from flask import Flask

app = Flask(__name__)

# Importando as rotas
import routes

if __name__ == '__main__':
    app.run(debug=True)
