def Calculate_sum(numbers):
    assert len(numbers) != 0  # Condition: List can not be empty
    return sum(numbers) / len(numbers)


num_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(" Calculated sum of given numbers: ", Calculate_sum(num_1))

num_2 = [8, 5, 6, 7, 4, 3]
print(" Calculated sum of given numbers: ", Calculate_sum(num_2))
