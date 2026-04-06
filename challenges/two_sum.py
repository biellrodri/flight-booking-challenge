""" "
Desafio de lógica 1:

    Dado um array de números inteiros e um alvo (target), encontre os índices de dois
    números que somam esse alvo.

    Você não pode reutilizar o mesmo elemento, e sempre existe uma solução.

Exemplo:

    Entrada:
        nums = [2, 7, 11, 15], target = 9

    Saída:
        [0, 1]

    Porque:
    2 + 7 = 9
"""


def two_sum(nums, target):
    prev_nums = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in prev_nums:
            return [prev_nums[complement], i]

        prev_nums[num] = i

    return []


print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
