# -*- coding: utf-8 -*-

import urllib
import json
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

PATH_URL = 'cours/cours-des-devises-contre-Franc-CFA-appliquer-aux-transferts'
URL = f'https://www.bceao.int/fr/{PATH_URL}'
currencies=['EUR','USD','Yen']

class DataSouper(object):
    @classmethod
    def httpFetcher(cls, URL):
        with requests.Session() as session:
            result = session.get(URL)
            result = result.text
            return result
        
#

class CurrencyScrapper(object):
    
    @classmethod
    def scrapLink(cls, URL):
        return DataSouper \
            .httpFetcher(URL)
    
    
    @classmethod
    def souper(cls, URL):
        result = cls.scrapLink(URL)
        return BeautifulSoup(
            result,
            'html.parser')
    
    @classmethod
    def getBoxCourse(cls, URL):
        soupering = cls.souper(URL)
        soupering = soupering \
            .find_all(attrs={
                'id': 'box_cours'})
        if soupering:
            table = soupering[0].table
            return table
        return None
    
    
    @classmethod
    def makeCurrencyList(cls, URL):
        soupering = cls.getBoxCourse(URL)
        if soupering:
            tr = soupering.find_all('tr')
            factory = [
                item.find_all('td')
                for item in tr
            ][1:]
            factory = [
                {
                    'Devise': x.string.strip(),
                    'Achat': float(y.string.strip().replace(',', '.')),
                    'Vente': float(z.string.strip().replace(',', '.')),
                }
                for (x, y, z) in factory
            ]
            return factory
        return None



    @classmethod
    def makeconversion(cls,URL):
        while True:
            amount_i=input('Entrer la valeur a convertir:')
            try:
                amount_i=float(amount_i)
                break
            except Exception:
                print ('Veuillez entrer une valeur correcte!')
                
        while True:
            currency_i=input('Entrer la devise de depart "EUR,USD,Yen"...:')
            if not (currency_i)  in currencies:
                print ('Veuillez entrer une valeur dans la liste', currencies)
                continue
            else:
                break
            
        while True:
            currency_f=input('Entrer la devise de destination "EUR,USD,YEN"...:')
            if not (currency_f)  in currencies:
                print ('Veuillez entrer une valeur dans la liste', currencies)
                continue
            else:
                break
            

                

            



result = CurrencyScrapper.makeCurrencyList(URL)

print(result)
