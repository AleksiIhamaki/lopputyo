import random

import random

class Asiakas:
    """Luokka asettaa asiakkaalle numeron, nimen, iän ja luo numeron.
    Julkiset methodit
        set_nimi()
        set_ika()
        get_nimi()
        get_ika()
        get_asiakasnumero()
    """
    def __init__(self, nimi, ika):
        """Konstruktorissa annetaan muuttujat, jotka peritään myöhemmin.
        :ivar asiakasnumero: asiakkaan puhelin numero
        :type asiakasnumero: int[]
        :ivar nimi: asiakkaan nimi
        :type nimi: str
        :ivar ika: asiakkaan ikä
        :type ika: int
        """
        self.__asiakasnumero = self.__luo_nro()
        self.__nimi = nimi
        self.__ika = ika
        
    def __luo_nro(self):
        """Satunnaisesti arvoo asiakkaan puhelinnumeron.
        :ivar numero: lista johon pistetään arvottu puhelinnumero
        :type numero: int[]
        """
        numero = []
        numero.append(random.randint(0, 99))
        numero.append(random.randint(0, 999))
        numero.append(random.randint(0, 999))
        return numero

    def set_nimi(self, nimi):
        """ Jos nimeä ei annettu, nostetaan virhe, jossa ilmoitetaan nimen puuttumisesta
        :param nimi: asiakkaan nimi
        :type nimi: str
        """
        if bool(nimi):
            self.nimi = nimi
        else:
            raise ValueError('Uusi nimi on annettava.')

    def set_ika(self, ika):
        """Jos type on int, sijoitetaan ikä, muutoin nostetaan virhe
        :param ika: asiakkaan ikä
        :type ika: int
        """
        if type(ika) is int:
            self.ika = ika
        else:
            raise ValueError('Virhe! Anna ika uudestaan.')

    def get_nimi(self):
        """Palautetaan __nimi
        """
        return self.__nimi

    def get_ika(self):
        """Palautetaan __ika
        """
        return self.__ika
    
    def get_asiakasnumero(self):
        """Palautetaan asiakasnumero
        """
        return f'{self.__asiakasnumero[0]:02}-{self.__asiakasnumero[1]:03}-{self.__asiakasnumero[2]:03}'

class Palvelu():
    def __init__(self, Asiakas, tuotenimi):
        self.tuotenimi = str(tuotenimi)
        self.asiakkaat = []

    def luo_asiakasrivi(self, Asiakas):
        pass

    def lisaa_asiakas(self, Asiakas):
        try:
            if self.nimi and self.ika == "":
                self.asiakkaat.append(self.nimi, self.ika)
        except ValueError:
            print("Anna kunnon asiakas")
            

    def poista_asiakas(self, Asiakas):
        try:
            self.asiakkaat.remove(self.nimi, self.ika)
        except ValueError:
            pass

    def tulosta_asiakkaat(self):
        print(self.__nimi, self.__ika, self.__asiakasnumero)

class ParempiPalvelu(Palvelu):
    def __init__(self, Asiakas, tuotenimi, edut):
        super().__init__(Asiakas, tuotenimi)
        self.edut = []

    def lisaa_etu(self):
        pass

    def poista_etu(self):
        pass

    def tulosta_edut(self):
        pass
