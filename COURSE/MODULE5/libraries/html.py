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

    @classmethod
    def getBoxData(cls):
        soupering = cls.openFile()
        table=[]
        soupering = soupering \
            .find_all('tr')
        for i in soupering[1:]:
            td=i.find_all('td')
            soupering=td[0].text.split(' ')
            table.append({
                'name':f'{soupering[0]} {soupering[-1].upper()}',
                'phone':td[1].text,
                'email':td[2].text,
                'address':td[3].text,
                'latng':td[4].text,
                'salary':td[4].text,
                'age':td[5].text,
            })
            return table

    @classmethod
    def main(cls):
        data=cls.getBoxData()
        return data
