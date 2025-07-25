# Calculator for serial numbers by a US Customs standard
# https://www.cbp.gov/sites/default/files/documents/in_bond_check_1.pdf
import math

def get_full_serial_number(initial):
    return (initial * 10) + math.ceil(((((initial * 10) // 7) % 10) / 10) * 7)

def main():
    print(get_full_serial_number(25770003)) # 257700030
    print(get_full_serial_number(25770005)) # 257700052

if __name__ == "__main__":
    main()