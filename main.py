from players import Player
from utils import load_random_word

def main():
    name = input("Введите имя игрока: ")

    player = Player(name)

    print(f"Привет, {player.name}!")

    word = load_random_word()
    print(f"Составь {word.count()} слов из слова {word.word}")
    print("Слова должны быть не короче 3 букв")
    print("Чтобы закончить игру, угадайте все слова или напишите 'stop'")
    print("Поехали, ваше первое слово?")
    while len(player.used_ans) < word.count():
        ans = input()
        if ans == 'stop' or ans == 'стоп':
            break

        if len(ans) < 3:
            print('слишком короткое слово')
            continue

        if player.check_used(ans):
            print("уже было")
            continue

        elif word.check(ans):
            player.use_ans(ans)
            print("верно!")

        else:
            print("Неверно!")
            continue

    print(f" Игра завершена, вы угадали {player.count_used()} слов!")

if __name__ == "__main__":
    main()


