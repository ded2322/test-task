def find_groups(numbers):
    """
    Группирует числа в 3 группы более простым способом:
    1. Сортируем числа
    2. Ищем самые большие "прыжки" между соседними числами
    3. Используем эти прыжки как границы групп
    """
    if len(numbers) < 3:
        return [1] * len(numbers)

    # Сортируем числа
    sorted_nums = sorted(numbers)

    # Находим разницы между соседними числами
    gaps = []
    for i in range(len(sorted_nums) - 1):
        gap = sorted_nums[i + 1] - sorted_nums[i]
        gaps.append((gap, i))

    # Находим два самых больших прыжка - это будут границы групп
    gaps.sort(reverse=True)
    split_points = sorted([gaps[0][1], gaps[1][1]])

    # Создаём словарь: для каждого числа запоминаем его группу
    groups = {}
    for i, num in enumerate(sorted_nums):
        if i <= split_points[0]:
            groups[num] = 1
        elif i <= split_points[1]:
            groups[num] = 2
        else:
            groups[num] = 3

    # Возвращаем номера групп в том же порядке, что и входные числа
    return [groups[x] for x in numbers]



# Пример использования:
if __name__ == "__main__":
    # Тестовые данные
    test_numbers = [75, 31, 33, 82, 10, 12, 9, 33, 71, 5, 42]

    result = find_groups(test_numbers)

    # Выводим результат
    print("Числа:", test_numbers)
    print("Группы:", result)

    # Выводим группы подробнее
    for group in range(1, 4):
        numbers_in_group = [num for num, g in zip(test_numbers, result) if g == group]
        print(f"\nГруппа {group}:", sorted(numbers_in_group))
