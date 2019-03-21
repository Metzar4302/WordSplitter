#gl
vowel_arr = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
#sogl
consonant_arr = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

sonor_consonant = ['й', 'р', 'л', 'м', 'н']

addition_consonant = ['б', 'в', 'з', 'ж', 'г', 'й', 'м', 'д', 'л', 'р', 'н']

spec_sign = ['ь', 'ъ']

def Main():
    input = "светлофиолетовый"
    print("\"{0}\" split by Moscow rights: {1}".format(input, MoscowSplitter(input)))

def MoscowSplitter(input):
    output = ""
    for i in range(len(input)):
        output += input[i]
        if str.lower(input[i]) in consonant_arr:
            if str.lower(input[i]) in sonor_consonant:
                try:
                    if str.lower(input[i+1]) in consonant_arr:
                        output += '-'
                except IndexError:
                    pass

        elif str.lower(input[i]) in vowel_arr:
            try:
                if i+1 >= len(input):
                    pass
                elif str.lower(input[i+1]) in vowel_arr:
                    output += '-'
                elif str.lower(input[i+1]) in sonor_consonant:
                    if str.lower(input[i+2]) in consonant_arr:
                        pass
                    else:
                        output += '-'
                elif str.lower(input[i+1]) in consonant_arr and i+2 >= len(input):
                    pass
                else:
                    output += '-'
            except IndexError:
                pass
            
        else:
            print("Wrong letter!")
            break
    return output

Main()