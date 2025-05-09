from abc import ABC, abstractmethod
from typing import List, Union

class AbstractStore(ABC):

    @property
    @abstractmethod
    def supplies(self)-> List["Product"]:
        """
        Property get di supplies. Contiene i prodotti disponibili in magazzino e le vendite.
        :return: Restituisce una lista di oggetti Product
        :rtype: List["Product"]
        """
        pass

    @supplies.setter
    @abstractmethod
    def supplies(self, products: List["Product"]):
        """
        Property set di supplies.
        :param products: List["Product"]
        :return: None
        :rtype: None
        """
        pass

    @property
    @abstractmethod
    def queries(self) -> dict:
        """
        Property get di queries. Un dizionario contenente tutte le funzioni che l'utente può utilizzare.
        :return: Restituisce il dizionario dei comandi, key-value -> "comando": "descrizione del comando"
        :rtype: dict
        """
        pass

    @abstractmethod
    def add_query(self) -> None:
        """
        Metodo per aggiungere un nuovo prodotto o per incrementarne uno già esistente tramite input utente.
        :return: None
        """
        pass

    @abstractmethod
    def sell_query(self) -> None:
        """
        Metodo per registrare la vendita di un prodotto.
        :return: None
        """
        pass

    @abstractmethod
    def list_query(self) -> None:
        """
        Metodo per elencare i prodotti in magazzino.
        :return: None
        """
        pass

    @abstractmethod
    def profit_query(self) -> None:
        """
        Metodo per calcolare il profitto lordo e netto sulle vendite effettuate.
        :return: None
        """
        pass

    @abstractmethod
    def help_query(self) -> None:
        """
        Metodo per mostrare i comandi disponibili per l'utente.
        :return: None
        """
        pass

    @abstractmethod
    def _get_product_index(self, name: str) -> int:
        """
        Metodo per ottenere l'indice di un prodotto disponibile nel magazzino dalla lista dei prodotti.
        :param name: nome del prodotto da ricercare
        :return: la posizione del prodotto nella lista, -1 se inesistente
        :rtype: int
        """
        pass

    @abstractmethod
    def _get_product_input(self, info: str, msg: str) -> Union[str, int, float]:
        """
        Metodo per gestire l'input utente per le informazioni del prodotto.
        :param info: str; attributo del prodotto da definire, può assumere i valori "name", "quantity", "selling_price" e "purchase_price"
        :param msg: str; messaggio di input da mostrare all'utente
        :return: str per "name", int per "quantity", float per "selling_price" e "purchase_price"
        :rtype: Union[str, int, float]
        """
        pass

    @abstractmethod
    def _get_available_products(self) -> List["Product"]:
        """
        Metodo che restituisce solo i prodotti disponibili nel magazzino (prodotto.status == "available").
        :return: lista di prodotti
        :rtype: List["Product"]
        """
        pass

