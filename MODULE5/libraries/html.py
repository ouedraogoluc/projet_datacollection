
import json
from .utils import Utils
from bs4 import BeautifulSoup


BASE_URL = 'COURSE/DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'


class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(
                data,
                'html.parser')
            file.close()
        return data
    
    
    """
    2. Mettre ces données sous forme de liste d'objects. 
    Dans le fichier html, nous avons les noeuds: name, phone, email, LatLon, salary et age.
    Pour respecter la consigne de la question 3, je considère juste les noeuds qui sont communs aux databases 
    de htmlFactory,csvFactory, jsonFactory (name, phone, email, address, latlng, salary, age)
    3. Assurez vous que les noeuds présents dans cette liste soient exactement comme dans CsvFactory, et JsonFactory
    """
    @classmethod
    def getBoxData(cls):
        soupering = cls.openFile()
        table = []
        soupering = soupering\
            .find_all('tr')
        for i in soupering[1:]:
            td = i.find_all('td')
            soupering = td[0].text.split(' ')
           
            table.append({
                'name' : f'{soupering[0]} {soupering[-1].upper()}',
                'phone':td[1].text,
                'email':td[2].text,
                'latlng': td[3].text,
                'salary':td[4].text,
                'age':td[5].text 
                
            })
        return table
    
    # 1. Completer le code de HtmlFactory, afin de récupérer les données
    @classmethod
    def main(cls):
        data = cls.openFile()
        data = cls.getBoxData()
        return data 
    