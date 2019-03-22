from PyQt5 import QtWidgets, uic
from design import Ui_MainWindow
import sys

#gl
vowel_arr = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
#sogl
consonant_arr = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

sonor_consonant = ['й', 'р', 'л', 'м', 'н']

addition_consonant = ['б', 'в', 'з', 'ж', 'г', 'й', 'м', 'д', 'л', 'р', 'н']

spec_sign = ['ь', 'ъ']

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mosStyleLable.setText("")
        self.ui.petStyleLabe.setText("")
        
        self.ui.splitBtn.clicked.connect(self.splitBtn_clicked)

    def splitBtn_clicked(self):
        self.ui.mosStyleLable.setText(MoscowSpliter(self.ui.inputTextField.toPlainText()))
        self.ui.petStyleLabe.setText(PeterSpliter(self.ui.inputTextField.toPlainText()))

def Main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())

# TODO: Have truble with twin letter
def MoscowSpliter(input):
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
            except Exception:
                print("Unknown exception. Please check code")
            
        else:
            print("Wrong letter!")
            break
    return output

# TODO: Have truble with two consonant in row
def PeterSpliter(input):
    output = ""
    for i in range(len(input)):
        output += input[i]
        if str.lower(input[i]) in consonant_arr:
            try:
                if str.lower(input[i+1]) in spec_sign:
                    pass
                elif str.lower(input[i]) == str.lower(input[i+1]):
                    output += '-'
                elif str.lower(input[i+1]) in consonant_arr:
                    if str.lower(input[i+1]) in addition_consonant:
                        if str.lower(input[i]) in sonor_consonant:
                            output += '-'
                        else:
                            pass
                    else:
                        output += '-'
                elif str.lower(input[i+1]) in vowel_arr:
                    pass
            except IndexError:
                pass
            except Exception:
                print("Unknown exception. Please check code")

        elif str.lower(input[i]) in vowel_arr:
            try:
                if str.lower(input[i+1]) in consonant_arr:
                    if str.lower(input[i+2]) in vowel_arr:
                        output += '-'
                    else:
                        # TODO: Truble here
                        pass
                else:
                    output += '-'
            except IndexError:
                pass
            except Exception:
                print("Unknown exception. Please check code")

        else:
            print("Wrong letter!")
            break
    return output

Main()