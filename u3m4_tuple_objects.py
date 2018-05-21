initials = ("AA", ("BB", ("CC", "CZ"), "BZ"), "AZ")
print(initials[1])
print(initials[1][1])
print(initials[1][1][1])

summer = "hot"
winter = "cold"
print(summer)
print(winter)
(summer, winter) = (winter, summer)
print(summer)
print(winter)