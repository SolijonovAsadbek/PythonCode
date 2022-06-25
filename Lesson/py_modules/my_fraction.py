from fractions import Fraction

a = Fraction(1, 2) + Fraction(2, 3)

if __name__ == '__main__':
    # numerator - Bu kasrning surat qismi.
    print('Kasrning surati: ', a.numerator)

    # denominator - Bu kasrning maxraj qismi.
    print('Kasrning maxraji: ', a.denominator)

    print("Kasrning qiymati: ", a)
