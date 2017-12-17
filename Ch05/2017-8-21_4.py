## Ch05 P 5.31

def color_to_value(temp):
    if temp >=0 and temp <=25:
        red = 0
        blue = 255
        green = color_number(temp)
    elif temp >= 25 and temp <= 50:
        red = 0
        green = 255
        blue = color_number(25-(temp-25))
    elif temp >= 50 and temp <= 75:
        blue = 0
        green = 255
        red = color_number(temp-50)
    elif temp >= 75 and temp <= 100:
        blue = 0
        red = 255
        green = color_number(25-(temp-75))

    color = 65536 * red + 256 * green + blue

    return round(color)

def color_number(temp):
    color = 255/25*temp
    return color

print(color_to_value(74))
print(color_to_value(75))
print(color_to_value(76))