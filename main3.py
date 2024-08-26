def math_dict(numbers: list[int]) -> dict:
    if not numbers:
        return {
            'sum': 0,
            'mean': 0,
            'max': None,
            'min': None
        }

    total_sum = sum(numbers)
    mean_value = total_sum / len(numbers)
    max_value = max(numbers)
    min_value = min(numbers)

    return {
        'sum': total_sum,
        'mean': mean_value,
        'max': max_value,
        'min': min_value
    }



numbers = [1, 2, 3, 4, 5]
result = math_dict(numbers)
print(result)

