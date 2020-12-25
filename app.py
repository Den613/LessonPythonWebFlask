import sqlite3
from sqlite3 import Error
from flask import Flask, request, render_template,session

app = Flask(__name__)
app.secret_key = 'j4lhxe8lvk7j4v5cmkfzytyn5235chf1'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/test', methods=['GET', 'POST'])
def test():

    q=[
    "В каком городе родился Михаил Булгаков?",
    "Сколько раз был женат Михаил Афанасьевич?",
    "Кому Михаил Булгаков посвятил свое произведение Белая гвардия?",
    "Первая публикация Михаила Булгакова состоялась в 1919 году в газете Грозный. Какое его произведение было тогда напечатано?",
    "На основе какого романа написана пьеса Дни Турбиных?",
    "Какую фамилию носил профессор из повести Роковые яйца?",
    "Действительно ли Михаил Афанасьевич Булгаков покончил жизнь самоубийством?",
    "Какой режиссер снял фильм Собачье сердце (1988) и телесериал Мастер и Маргарита(2005)?",
    "Из какого произведения Булгакова эта фраза - ...разруха не в клозетах, а в головах.",
    "Кто из героев романа Мастер и Магарита произносит следующие слова: Никогда и ничего не просите! Никогда и ничего, и в особенности у тех, кто сильнее вас. Сами предложат и сами всё дадут!"
    ]

    ans = ["Киев","Три","Любовь Белозерская","Грядущие перспективы","Белая гвардия","Персиков","Нет","Владимир Бортко","Собачье сердце","Воланд"]
    if 'visits' in session:
           session['visits'] = session.get('visits') + 1  # чтение и обновление данных сессии
    else:
           session['visits'] = 1
    if format(session.get('visits')) == "10":
        session['visits'] = 1

    if request.method == 'GET':
        render_template('test.html',q=q[int(format(session.get('visits')))])
    else:

        test = request.form['test']

        print(q[int(format(session.get('visits')))+1])
        print(ans[int(format(session.get('visits')))+1])
        #print(test)

        if test.lower() == ans[int(format(session.get('visits')))-1].lower():
            return render_template('text.html',q=format(session.get('visits')), name="Правильно", level = "Плюс очко")
        else:
            return render_template('text.html',q=format(session.get('visits')), name="Неправильно", level = "Минус очко")

    return render_template('test.html',q=q[int(format(session.get('visits')))])
    #return format(session.get('visits'))



if __name__ == "__main__": #проверяет является ли этот файл главным для запуска
    app.run(debug=True) #run() - запускает наш файл debug = True выводит все ошибки
