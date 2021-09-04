print("Your fortune cookie says...")
furtune_random_number: int = randint(1, 30)
SECRET_NUMBER_1: int = 8
if furtune_random_number == SECRET_NUMBER_1:
    print("A beautiful, smart, and loving person will be coming into your life.")
else:
    if furtune_random_number > SECRET_NUMBER_1:
        print("Your life will be happy and peaceful.")
    else:
        if furtune_random_number < SECRET_NUMBER_1:
            print("Soon life will become more interesting.")
print("Now, go spread positive vibes!")

count: int = 0
repeat_words: str = input("What beat do you want to repeat?")
print("What beat do you want to repeat?" + repeat_words)
repeat_times: int = int(input("How many times you want to repeat?"))
print("How many times you want to repeat?" + str(repeat_times))
after_required_numbers_of_repetition: str = ""
if repeat_times <= count:
    print("No beat...")
else: 
    while count < repeat_times:
        count = count + 1
        after_required_numbers_of_repetition = after_required_numbers_of_repetition + repeat_words
print(after_required_numbers_of_repetition)

input_letter: str = input("What letter do you want to seach for?: ")
print("What letter do you want to seach for?: " + input_letter)
input_word: str = input("Enter a word: ")
print("Enter a word: " + input_word)
length: int = len(input_word) - 1
count_1: int = 0
count_target: int = 0
character: str = input_word[count_1]
while length >= count_1:
    if character == input_letter:
        count_target = count_target + 1
    else:
        count_target = count_target
    count_1 = count_1 + 1
print("Count: " + str(count_target))