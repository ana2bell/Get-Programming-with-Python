phrase = "Eek, two snake eyes"
num = "1"

num_repeat = num * 4
print(num_repeat)

str_not_num = num_repeat.replace("1", "one")
print(str_not_num)

together = phrase + ": " + str_not_num
print(together)

num_times = together.count("neon")
print(num_times)