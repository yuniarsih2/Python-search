# Temukan elemen yang paling sering muncul dalam sebuah list

def sequential_seacrh_most_frequent(data):
    count_dict = {}
    for item in data:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    most_frequent = None
    max_cont = 0
    for key in count_dict:
        if count_dict[key] > max_cont:
            most_frequent = key
            max_cont = count_dict[key]
    return most_frequent


my_list = [3, 7, 2, 5, 7, 3, 7, 2, 7]
frequent_element = sequential_seacrh_most_frequent(my_list)
print(f"Element yang paling sering muncul adalah {frequent_element}")

# Output Element yang paling sering muncul adalah elemen 7
