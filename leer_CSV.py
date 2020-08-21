import csv

def main():
    with open ('archivoCSV.csv') as file:
        leer = csv.reader(file)
        print("Tipo de Dato:")
        print(type(leer))
        for row in leer:
            print('Nombre: {0}, Apellido : {1}, Edad: {2}, Carrera: {3}'.format(row[0], row[1], row[2], row[3]))

if __name__ == '__main__':
    main()