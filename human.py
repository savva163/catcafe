class Human:
    def choose_dice(self, dice_list):
        while True:
            res = input('Выберите 1 кубик: ')
            try:
                dice = int(res)
            except ValueError:
                print('Некорректный ввод. Введите число.')
                continue

            if dice in dice_list:
                dice_list.remove(dice)
                return dice
            else:
                print('Такого кубика нет!')

    def choose_action(self):
        pass
