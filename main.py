import leer_json
import leer_CSV
import leer_XML

def menu():

    print("Menu\n" +
        "Seleccione una Opcion.\n" +
        "a. Archivos JSON\n" +
        "b. Archivos XML\n" +
        "c. Archivos CSV\n"+
        "d. Salir")

def main():
    while True:
        menu()
        a = input()
        if a == 'a':
            print("JSON")
            leer_json.main()
        elif a == 'b':
            print("XML")
            leer_XML.main()
        elif a == "c":
            print("CSV")
            leer_CSV.main()
        elif a== "d":
            break
        else:
            print("Seleccione una Opcion Valida")

if __name__ == '__main__':
    main()

