def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)
if __name__ == "__main__":
    count = int(input("Введите количество элементов: "))
    numbers = []
    for _ in range(count):
        num = float(input("Введите число: "))
        numbers.append(num)
    
    print("Максимум:", find_max(numbers))

