scores = input("Введите результаты игры через пробел: ")
scores_list = scores.split()

max_score = int(scores_list[0])
for score in scores_list:
    if int(score) > max_score:
        max_score = int(score)

print(f"Самый лучший результат: {max_score}")