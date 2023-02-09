print('Ini merupakan kalkulator sederhana!')
ex = 'lanjut'
while ex != 'Q':
    angka1 = int(input('Masukan Angka Pertama : '))
    operator = input('Masukkan operator [ + | - | * | / ] : ')
    angka2 = int(input('Masukan Angka Kedua : '))
    if operator == '+':
        print(f'{angka1} + {angka2} = ', angka1+angka2)
    elif operator == '-':
        print(f'{angka1} - {angka2} = ', angka1-angka2)
    elif operator == '*':
        print(f'{angka1} * {angka2} = ', angka1*angka2)
    elif operator == '/':
        print(f'{angka1} - {angka2} = ', angka1/angka2)
    ex = input('')
    