# Написати функцію, що за послідовністю цілих будує список її елементів, що зустрічаються в ній
# більше одного разу.

def sort_list(numbers: list) -> list:
    new_list = []
    dict = {}
    for number in numbers:
        if number not in dict:
            dict[number] = 1
        else:
            dict[number] += 1
    for key, value in dict.items():
        if value > 1:
            new_list.append(key)
    return new_list


def show_example(input_list):
    print(sort_list(input_list))


show_example([0, 1, 1, 3, 5])
