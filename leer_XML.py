from xml.dom import minidom
archivo = minidom.parse("archivoXML.xml")

def main():
    print("")
    clientes = archivo.getElementsByTagName("cliente")
    print("Tipo de Dato: ")
    print(type(archivo))

    for aux in clientes:
        nombre = aux.getElementsByTagName("nombre")[0]
        apellido = aux.getElementsByTagName("apellido")[0]
        edad = aux.getElementsByTagName("edad")[0]
        telefono = aux.getElementsByTagName("telefono")[0]
        print("nombre:%s" % nombre.firstChild.data)
        print("apellido:%s" % apellido.firstChild.data)
        print("edad:%s" % edad.firstChild.data)
        print("telefono:%s" % telefono.firstChild.data)
        print("")


if __name__ == '__main__':
    main()