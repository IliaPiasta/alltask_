a = (1, 2, 4 , 6 , 8)

def main(numbers):
    max_index = 0
    min_index = 0
    
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[max_index]:
            max_index = i
        if numbers[i] <= numbers[min_index]:
            min_index = i

    return max_index, min_index
