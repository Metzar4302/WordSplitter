#gl
vowel_arr = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
#sogl
consonant_arr = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

spec_letters = ['й', 'р', 'л', 'м', 'н']

def Main():
    input = "Сообщение"
    print(Splitter(input))

#! Wrong
def Splitter(input):
    output = ""
    status = "Srch"
    for i in range(len(input)):
        if str.lower(input[i]) in consonant_arr:
            if status == "Srch":
               output += input[i]
            elif status == "VowelFnd":
                # if str.lower(input[i]) in spec_letters:
                #     output += input[i]
                #     if str.lower(input[i+1]) == 'ь':
                #         output += input[i+1] + '-'
                # elif input[i+1] in consonant_arr:
                #     output += input[i] + '-'
                # else:
                #     output += '-'
                # status = "Srch"
                output += input[i] + '-'
            status = "Srch"
        
        elif str.lower(input[i]) in vowel_arr:
            if status == "Srch":
                if i+1 >= len(input):
                    output += input[i]
                    break
                elif input[i+1] in vowel_arr and i+2 >= len(input):
                    output += input[i] + input[i+1]
                    break
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

Main()