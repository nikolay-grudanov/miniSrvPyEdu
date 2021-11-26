# miniSrvPyEdu
__Описание__
Это серевер на питоне, с его помощью можно отлаживать запросы.
У данного сервера есть следующие возможности
1. При отправке запроса (кроме 2 зарезервированных URL) выводит в консоль подробную информацию о вашем запросе. Подерживаемые методы: GET, POST, PUT, DELETE. Под описанием пример вывода в консоль.
1. URL /delay Подерживаемые методы: GET, POST, PUT, DELETE. Обязательные параметры запроса: wait. В парметре wait указать количество секунд ожидания.
1. URL /return-file Подерживаемые методы: GET. Обязательные параметры запроса: name. В парметре name указать имя файла с рашерением, подерживается формат JSON. Файл должен находиться в той же деректории что и исполняймый файл.

__Пример__

Получен запрос в  2021-03-07.19.44.54

url:    http://127.0.0.1:5000/test1/test2/test3?q1=111&q2=abc

path:   test1/test2/test3

query params: 

   q1 = 111
   
   q2 = abc
   
method: GET

headers: 

   Host = 127.0.0.1:5000
    
   User-Agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0
    
   Accept = text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    
   Accept-Language = ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
    
   Accept-Encoding = gzip, deflate
    
   Dnt = 1
    
   Connection = keep-alive
    
   Upgrade-Insecure-Requests = 1
    
data: 




__P.S.__
_Я только учусь программировать, поэтомк если вы увидите ошибки, пожалуйста, предложите улучшения._
