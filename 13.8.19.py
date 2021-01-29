# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов. Программа
# # должна работать следующим образом:
# #
# # 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
# #
# # 2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:
# #
# # Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# # От 18 до 25 лет — 990 руб.
# # От 25 лет — полная стоимость 1390 руб.
# # 3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек на
# # конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.

n=int(input("Введите количество билетов: "))
sum=0 #счетчик для подсчета суммы заказа
for i in range(n): #цикл по количеству билетов
    k=0  #временная пересенная, ограничивающая количество неверных попыток при вводе возраста посетителя
    while k<3:  #цикл для попыток ввода возраста
        try:
            age = int(input('Введите возраст ' + str(i + 1) + ' посетителя: '))
            if age > 100 or age <= 0:  #если возраст меньше 0 или старше  100 лет, считаем его ошибочным
               raise ValueError("Вы ввели неправильный возраст")
        except ValueError:
               k+=1 #при ошибке увеличиваем счетчик
               continue
        else:
           break #при верно введенном возрасте выходим из цикла while
    else:
        print('Извините, но на такой возраст конференция не расчитана. Процесс покупки билетов завершен')
        exit() # при превышении количества попыток выходим из программы
    if 18<= age <25 :
        sum+=990
    elif age>=25:
        sum+=1390
k=1 #временная переменная для вычисления скидок на общую сумму заказа
if n>3:
    k=0.9 # С учетом 10% скидки
print ('Сумма Вашего заказа за ',n,' бил. составляет ',sum*k,' руб.')