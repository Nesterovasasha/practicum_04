score = input("Введите счет в формате 'количество голов первой команды:количество голов второй команды': ")

score_list = score.split(":")
first_team_score = int(score_list[0])
second_team_score = int(score_list[1])

if first_team_score > second_team_score:
    print("1")
elif second_team_score > first_team_score:
    print("2")
else:
    print("0")
