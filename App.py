#gl
vowel_arr = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
#sogl
consonant_arr = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

sonor_consonant = ['й', 'р', 'л', 'м', 'н']

addition_consonant = ['б', 'в', 'з', 'ж', 'г', 'й', 'м', 'д', 'л', 'р', 'н']

spec_sign = ['ь', 'ъ']

def Main():
    input = "Сообщение"
    # print("\"{0}\" split by Moscow rights: {1}\n\"{0}\" split by Peter rights: {2}".format(input, MoscowSplitter(input), PeterSplitter(input)))
    print("\"{0}\" split by Moscow rights: {1}".format(input, MoscowSplitter(input)))

def PeterSplitter(input):
    output = ""
    status = "Srch"
    for i in range(len(input)):
        if str.lower(input[i]) in consonant_arr:
            if status == "Srch":
               output += input[i]
            elif status == "VowelFnd":
                if str.lower(input[i]) in sonor_consonant:
                    if str.lower(input[i+1]) in consonant_arr:
                        output += input[i] + '-'
                        status = "Srch"
                    if str.lower(input[i+1]) in spec_sign:
                        output += input[i+1] + '-'
                    else:
                        output += '-' + input[i]
                        status = "Srch"
                else:
                    output += input[i] + '-'
                status = "Srch"
            status = "Srch"
        
        elif str.lower(input[i]) in vowel_arr:
            if status == "Srch":
                if i+1 >= len(input):
                    output += input[i]
                    break
                # elif input[i+1] in vowel_arr and i+2 >= len(input):
                #     output += input[i] + input[i+1]
                #     break
                elif input[i+1] in vowel_arr:
                    output += input[i] + '-'
                else:
                    output += input[i]
                    status = "VowelFnd"
            elif status == "VowelFnd":
                output += '-' + input[i]
        else:
            print("Wrong letter!")
            status = "Error. Wrong letter"
            break
    return output


def MoscowSplitter(input):
    output = ""
    for i in range(len(input)):
        output += input[i]
        if str.lower(input[i]) in consonant_arr:
            if str.lower(input[i]) in sonor_consonant:
                if str.lower(input[i+1]) in consonant_arr:
                    output += '-'

        elif str.lower(input[i]) in vowel_arr:
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
            
        else:
            print("Wrong letter!")
            break
    return output

Main()