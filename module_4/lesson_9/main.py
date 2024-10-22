import requests

res = requests.get("http://numbersapi.com/8/13/date")
print(res.json)
print(res.text)




#Найдите ресурс, в котором есть API(бесплатное). 
# Вам в этом поможет данная статья(https://habr.com/ru/companies/macloud/articles/562700/).
#Вам необходимо написать успешный запрос к серверу и получить ответ в формате JSON.