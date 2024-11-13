
#* -------------- Colorama Example ------------------

#? This code is from the colorama documentation, showing us how to import the required classes, use them for coloured output, and reset
#? We used it to prove our installs had worked, and as a reference to the assignment

from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')