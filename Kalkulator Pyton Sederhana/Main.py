number_1 = input("Masukkan angka pertama: ")
operator = input("Masukkan operator (+, -, *, **, %, //, /): ")
number_2 = input("Masukkan angka kedua: ")

try:
    number1 = float(number_1)
    number2 = float(number_2)

    def floor_division(num1, num2):
        return num1 // num2

    if operator == '+':
        hasil = number1 + number2
        print("Hasil:", hasil)
    elif operator == '-':
        hasil = number1 - number2
        print("Hasil:", hasil)
    elif operator == '*':
        hasil = number1 * number2
        print("Hasil:", hasil)
    elif operator == '**':
        hasil = number1 ** number2
        print("Hasil:", hasil)
    elif operator == '//':
        if number2 == 0:
            print("Error: Pembagian dengan nol tidak diizinkan!")
        else:
            hasil = floor_division(number1, number2)
            print("Hasil:", hasil)
    elif operator == '%':
        hasil = number1 % number2
        print("Hasil:", hasil)
    elif operator == '/':
        if number2 == 0:
            print("Error: Pembagian dengan nol tidak diizinkan!")
        else:
            hasil = number1 / number2
            print("Hasil:", hasil)
    else:
        print("Operator tidak valid!")

except ValueError:
    print("Input tidak valid. Harap masukkan angka.")

print("Terima kasih sudah bermain di kalkulator sederhana ini!")

print("Adnan mengucapkan terima kasih banyak sudah menggunakan kalkulator sederhana ini!")

