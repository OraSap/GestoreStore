from .abstract_product import AbstractProduct
from typing import List, Union

class Product(AbstractProduct):
    """
    Implementazione:
    La classe ammette solo le seguenti variabili di istanza private:
    '__name','__quantity', '__selling_price', '__purchase_price', '__status'
    Ognuna di esse dispone della relativa property per get e set.
    """
    __slots__ = ['__name', '__quantity', '__selling_price', '__purchase_price', '__status']

    def __init__(self, name: str, quantity: int, selling_price: float, purchase_price: float, status: str ="available"):
        self.name = name
        self.quantity = quantity
        self.selling_price = selling_price
        self.purchase_price = purchase_price
        self.status = status

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = Product.validate_name(name)

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: str) -> None:
        self.__quantity = Product.validate_quantity(quantity)

    @property
    def selling_price(self) -> float:
        return self.__selling_price

    @selling_price.setter
    def selling_price(self, selling_price: str) -> None:
        self.__selling_price = Product.validate_price(selling_price)

    @property
    def purchase_price(self) -> float:
        return self.__purchase_price

    @purchase_price.setter
    def purchase_price(self, purchase_price: str) -> None:
        self.__purchase_price = Product.validate_price(purchase_price)

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str) -> None:
        self.__status = status

    def __copy__(self):
        """
        Restituisco una shallow copy del prodotto. Non è necessario usare __deepcopy__ per il tipo delle varibili d'istanza.
        """
        return type(self)(self.name, self.quantity, self.selling_price, self.purchase_price, self.status)

    @staticmethod
    def validate_price(value: str) -> float:
        """
        Converto l'input in float e ne faccio il round a due cifre.
        Se l'oggetto non è convertibile sollevo un eccezione gestita esternamente.
        """
        try:
            value = float(value)
        except:
            raise TypeError("Il prezzo deve essere un valore numerico.")
        return round(value, 2)

    @staticmethod
    def validate_quantity(value: str) -> int:
        """
        Converto l'input in int e verifico che sia maggiore di 0.
        Se l'oggetto non è convertibile, o se è minore o uguale a 0, sollevo un eccezione gestita esternamente.
        """
        try:
            value = int(value)
        except:
            raise TypeError("La quantità deve essere un numero intero.")
        assert (value > 0), "La quantità deve essere maggiore di 0."
        return value

    @staticmethod
    def validate_name(name: str) -> str:
        """
        Verifico che l'input non sia una stringa vuota
        """
        assert (len(name.strip()) > 0), "Il nome non può essere vuoto."
        return name.strip()
