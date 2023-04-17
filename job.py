print(f'Наша компания нуждается в высококлассных рабочих; \nЕсли вы считаете себя таковым,' 
      f'то вы можете заполнить анкету и мы подберём вам лучшую вакансию!') 

#Пользователь вводит данные о себе
type_of_profession = input('Выберете желаемый тип профессии: 1 - Человек-Человек, 2 - Человек-Знаковая система, 3 - Человек-Природа, 4 - Человек-Художественный образ, 5 - Человек-Техника: ')
name = input('Введите ваше ФИО: ')
age = int(input('Введите ваш возраст: '))
gender = input('Введите ваш пол: ')
education_level = input('Введите ваш уровень образования: ')
work_experience = int(input('Введите ваш стаж работы (в годах): '))
experience_in_position = int(input('Введите количество месяцев назад, когда вы выполняли обязанности аналогичной должности (в том же типе профессии): '))


flag = False


#Пользователь выбирает желаемый тип профессии и программа выводит предложение в зависимости от остальных введённых данных
if type_of_profession == '1':
    if age >= 21 and education_level == 'специалист' and work_experience >= 1:
        print(f'Уважаемый {name}! В нашей компании имеется для вас вакансия: Преподаватель')
        flag = True
    elif 23 <= age <= 50 and education_level == 'бакалавр' and work_experience >= 3:
        print(f'Уважаемый {name}! В нашей компании имеется для вас вакансия: Психолог')
        flag = True
    elif 18 <= age <= 50:
        print(f'Уважаемый {name}! В нашей компании имеется для вас вакансия: Менеджер')
        flag = True


elif type_of_profession == '2':
    if 18 <= age <= 42:
        print(f'Уважаемый {name}! В нашей компании имеется для вас вакансия: Флорист')
        flag = True


elif type_of_profession == '3':
    if 21 <= age <= 55 and education_level == 'бакалавр' and work_experience >= 5:
        print(f'Уважаемый {name}! В нашей компании имеется для вас вакансия: Бригадир цеха')
        flag = True
    elif 28 <= age <= 60 and education_level == 'специалист' and work_experience >= 5:
        print(f'Уважаемый {name}! В нашей компании имеется для вас вакансия: Электромонтёр')
        flag = True
    elif 20 <= age <= 60:
        print(f'Уважаемый {name}! В нашей компании имеется для вас вакансия: Заведующий складом')
        flag = True


elif type_of_profession == '4':
    if age >= 18:
        print(f'Уважаемый {name}! В нашей компании имеется для вас вакансия: Театральный художник')
        flag = True


elif type_of_profession == '5':
    if age >= 25 and education_level == 'специалист' and work_experience >= 5:
        print(f'Уважаемый {name}! В нашей компании имеется для вас вакансия: Инженер-программист')
        flag = True
    elif 18 <= age <= 35 and education_level == 'бакалавр' and work_experience >= 2:
        print(f'Уважаемый {name}! В нашей компании имеется для вас вакансия: Системный администратор')
        flag = True
    elif age >= 20 and education_level == 'высшее':
        print(f'Уважаемый {name}! В нашей компании имеется для вас вакансия: Инженер-конструктор')
        flag = True


#Если для пользовательского ввода не было предложений, система будет искать другие вакансии в наличии
if not flag:
    print(f'Уважаемый {name}! На данный момент в нашей компании отсутствуют вакансии для Вас')
    other_jobs = []
    if age >= 25 and education_level == 'специалист' and work_experience >= 5:
        other_jobs.append('Инженер главного конструктора')
    elif age >= 25 and education_level == 'высшее' and work_experience >= 2:
        other_jobs.append('Менеджер по продажам')
    elif age >= 18 and education_level == 'бакалавр' and work_experience >= 1:
        other_jobs.append('Менеджер по маркетингу')


if len(other_jobs) > 0:
    print(f"Вы также можете подойти для следующих вакансий: {', '.join(other_jobs)}")
