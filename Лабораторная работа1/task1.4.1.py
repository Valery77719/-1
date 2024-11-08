numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_before=sum(numbers[:4])
sum_after=sum(numbers[5:])
len_before=len(numbers[:4])
len_after=len(numbers[4:])
change=((sum_before+sum_after)/(len_before+len_after))
numbers[4]=change
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
