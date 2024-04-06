print("Ответьте 'да' или 'нет' на следующие вопросы:")

short_hair = input("Собака короткошерстной породы? ").lower()
if short_hair == "да":
    height_less_50 = input("Рост собаки менее 50 см? ").lower()
    if height_less_50 == "да":
        short_tail = input("У собаки короткий хвост? ").lower()
        if short_tail == "да":
            print("Порода: Английский бульдог")
        else:
            long_ears = input("У собаки длинные уши? ").lower()
            if long_ears == "да":
                print("Порода: Гончая")
            else:
                short_body = input("У собаки короткое тело? ")
                if short_body == "да":
                    print("Порода: Мопс")
                else:
                    print("Порода: Чихуахуа")
    else:
        weight_more_50 = input("Собака весит более 50 кг? ").lower()
        if weight_more_50 == "да":
            print("Порода: Датский Дог")
        else:
            print("Порода: Фоксхаунд")
else:
    height_less_50 = input("Рост собаки менее 50 см? ").lower()
    if height_less_50 == "да":
        character = input("У собаки доброжелательный характер? ")
        if character == "да":
            print("Порода: Кокер-Спаниэль")
        else:
            print("Порода: Ирландский Сеттер")
    else:
        height_more_70 = input("У собаки рост менее 70 см? ").lower()
        if height_less_50 == "да":
            long_ears = input("У собаки длинные уши? ").lower()
            if long_ears == "да":
                print("Порода: Большой Вандейский Грифон")
            else:
                 print("Порода: Колли")
        else:
            red_color = input("Окрас рыжий с белыми отметинами? ")
            if red_color == "да":
                print("Порода: Сенбернар")
            else:
                white_color = input("Белоснежный окрас? ")
                if white_color == "да":
                    print("Порода: Ирландский волкодав")
                else:
                    print("Порода: Ньюфаундленд")