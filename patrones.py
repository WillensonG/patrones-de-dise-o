
class Postre:
    def preparar(self):
        pass

    def servir(self):
        pass



class Pastel(Postre):
    def preparar(self):
        print("Preparando el pastel")

    def servir(self):
        print("Sirviendo el pastel")


class Galleta(Postre):
    def preparar(self):
        print("Preparando la galleta")

    def servir(self):
        print("Sirviendo la galleta")


# Patrón Singleton: 
class TiendaDePostres:
    _instance = None

    @staticmethod
    def obtener_instancia():
        if not TiendaDePostres._instance:
            TiendaDePostres._instance = TiendaDePostres()
        return TiendaDePostres._instance

    def vender_postre(self, tipo):
        if tipo == "pastel":
            return Pastel()
        elif tipo == "galleta":
            return Galleta()
        else:
            raise ValueError("Tipo de postre no válido")


#patrón Factory Method 
def main():
    tienda = TiendaDePostres.obtener_instancia()
    
    pastel = tienda.vender_postre("pastel")
    pastel.preparar()
    pastel.servir()

    galleta = tienda.vender_postre("galleta")
    galleta.preparar()
    galleta.servir()


if __name__ == "__main__":
    main()
