from flask import Flask, render_template
from statistics_module import get_statistics

app = Flask(__name__)

@app.route('/')
def home():
    stats = get_statistics()  # Получение статистики из MySQL
    return render_template('index.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
