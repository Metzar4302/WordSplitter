#gl
vowel_arr = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
#sogl
consonant_arr = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

sonor_consonant = ['й', 'р', 'л', 'м', 'н']

addition_consonant = ['б', 'в', 'з', 'ж', 'г', 'й', 'м', 'д', 'л', 'р', 'н']

spec_sign = ['ь', 'ъ']

def Main():
    input = "Сообщение"
    print(MoscowSplitter(input))


def MoscowSplitter(input):
    output = ""
    status = "Srch"
    for i in range(len(input)):
        if str.lower(input[i]) in consonant_arr:
            if status == "Srch":
               output += input[i]
            elif status == "VowelFnd":
                if str.lower(input[i]) in sonor_consonant and str.lower(input[i+1]) in consonant_arr:
                # if str.lower(input[i]) in addition_consonant:
                    output += input[i]
                    if str.lower(input[i+1]) in spec_sign:
                        output += input[i+1] + '-'
                    else:
                        output += '-'
                # elif str.lower(input[i+1]) in consonant_arr:
                #     output += input[i] + '-'
                else:
                    output += input[i] + '-'
                status = "Srch"
                
        
        elif str.lower(input[i]) in vowel_arr:
            if status == "Srch":
                if i+1 >= len(input):
                    output += input[i]
                    break
                elif  str.lower(input[i+1]) in vowel_arr and i+2 >= len(input):
                    output += input[i] + input[i+1]
                    break
                else:
                    output += input[i]
                    status = "VowelFnd"
            elif status == "VowelFnd":
                if str.lower(input[i+1]) in addition_consonant:
                    output += '-' + input[i] + '-'
                    status = "Srch"
                else:
                    output += '-' + input[i]
        else:
            print("Wrong letter!")
            status = "Error. Wrong letter"
            break
    return output

Main()