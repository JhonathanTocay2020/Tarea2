import json

def main():

    with open('archivoJSON.json') as file:
        dato = json.load(file)
        print("Tipo de Dato:")
        print(type(dato))
        print("\n")
        for alumno in dato['alumno']:
            print('Nombre:', alumno['nombre'])
            print('Apellido:', alumno['apellido'])
            print('edad:', alumno['edad'])
            print('carnet:', alumno['carnet'])
            print('')

if __name__ == '__main__':
    main()