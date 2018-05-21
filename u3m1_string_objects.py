text = "MY 1ST TIME PLAYING WITH STRINGS! &OSIDJOIF@$#@NLOIS*@^%@$ASIDU"

without_cat = text[0:33:1]
print(without_cat)

middle_bit = without_cat[12:len(without_cat):1]
print(middle_bit)

proper_sentence = middle_bit.capitalize()
print(proper_sentence)