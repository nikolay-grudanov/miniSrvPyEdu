#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response, json
import werkzeug
import time
import os
import re
from colorama import Fore, Style

app = Flask(__name__)

# задаём параметры для работы приложения
success_input_port = False
test_port = 0


# Функция для выводв красного цвета
def out_red(text):
    print(Fore.RED + format(text))
    print(Style.RESET_ALL)


while success_input_port is False and test_port < 10:
    str_port = (input("Введите порт\nport = "))
    try:
        int_port = int(str_port)
        if 0 < int_port < 65535:
            success_input_port = True
        else:
            test_port = test_port + 1
            out_red("Порт должен быть от 0 до 65535 !!!")
    except:
        test_port = test_port + 1
        out_red("Порт должен быть числом !!!")
else:
    if test_port == 10:
        out_red("Не получилось ввести порт 10 раз подряд !!!\nСервер прекратит работу через 5 секунд.")
        time.sleep(5)

    else:
        pass


# функция которая выводит информацию о поступившем запросе
@app.route('/', methods=['GET', 'POST'], defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def request_info(path):
    if path is None:
        path = "null"

    args = request.args
    if len(args) == 0:
        str_args = "null"
    else:
        args_m = []
        for i, j in args.to_dict().items():
            args_m.append('\n   ' + ''.join(i) + ' = ' + ''.join(j))
        str_args = ''.join(args_m)

    if request.url is None:
        url = "null"
    else:
        url = request.url

    if request.method is None:
        method = "null"
    else:
        method = request.method

    if request.headers.items() is None:
        header = "null"
    else:
        header = werkzeug.datastructures.Headers(request.headers.items())
    len_hed = header.__len__()
    # счётчик
    i = 0
    # пустой массив
    a = []
    while i < len_hed:
        a.append('\n    ' + ''.join(header[i][0]) + ' = ' + ''.join(header[i][1:len(header[i])]))
        i += 1
    str_headers = ''.join(a)
    # работа с телом запроса
    date_dict = request.form.to_dict()
    if len(date_dict) != 0:
        str_date = json.dumps(date_dict)
    else:
        try:
            str_date = request.get_data().decode()
        except:
            save_body = open("save_" + time.strftime('%Y-%m-%d.%H.%M.%S') + "_.txt", 'wb')
            save_body.write(request.get_data())
            save_body.close()
            str_date = "Не получилось прочитать тело"
    # собираем всю инфу в строку
    str_info = '''Получен запрос в  ''' + time.strftime('%Y-%m-%d.%H.%M.%S') + '''
url:    ''' + url + '''
path:   ''' + path + '''
query params: ''' + str_args + '''
method: ''' + method + '''
headers:  ''' + str_headers + '''
data: \n''' + str_date
    # сохраняем в файл в отдельной папке

    # выводим результат в консоль
    print(str_info)
    return make_response(jsonify({'Info': 'Ok'}), 200)


# функция для проверки задежки
@app.route('/delay')
def delay_response():
    str_wait = request.args.to_dict().get("wait")
    if str_wait is None:
        # abort(400, 'Not found query params "wait"')
        return make_response(jsonify({"error": "Not found query params wait"}), 400)
    else:
        try:
            int_wait = int(str_wait)
            time.sleep(int_wait)
            return make_response(jsonify({'delay': str_wait + ' second'}), 200)
        except:
            return make_response(jsonify({"error": "Params wait must be integer"}), 400)


# функция для получения файла
@app.route('/return-file')
def return_file_response():
    str_name = request.args.to_dict().get("name")
    if str_name is None:
        return make_response(jsonify({"error": "Not found query params name"}), 400)

    result = re.split(r'\.', str_name)

    if len(result) < 2:
        response_str = "You need to specify the file extension."
        abort(400, response_str) 

    if result[1] != "json":
        response_str = "Only json files are supported. You have sent: " + str(result[1])
        abort(400, response_str) 


    try:
        with open(str_name) as json_file:
            json_data = json.load(json_file)
        return make_response(json_data, 200)
    except :
            cwd = os.getcwd()
            response_str = "Failed to open the file. Check it path: " + cwd + "\\" + str_name 
            abort(400, response_str) 


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int_port)
