class ParempiPalvelu(Palvelu):
    """Luokassa käsitellään tuotenimeä ja sen etuja.
    Julkiset metodit
        listaa_etu()
        poista_etu()
        tulosta_edut()
    """
    def __init__(self,tuotenimi):
        """Konstruktorissa peritään tuotenimi Palvelu luokalta
        :ivat __edut: Tuotenimen edut
        :type __edut: str[]
        """
        super().__init__(tuotenimi)
        self.__edut = []

    def lisaa_etu(self, etu):
        """Liitetään kutsunnassa pistetty etu listaan
        """
        self.__edut.append(etu)

    def poista_etu(self, etu):
        """Poistetaan kutsunnassa pistettu etu listasta. Jos ei ole olemassa, virhe ohitetaan
        """
        try:
            self.__edut.remove(etu)
        except:
            pass

    def tulosta_edut(self):
        """Lopulta tulostaa tuotenimi ja sen edut kutsunnassa
        """
        print("Tuotteeen " + self.tuotenimi + " edut ovat:")
        for etu in self.__edut:
            print(f'{etu}')