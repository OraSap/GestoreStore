import os
from .product import Product
from .abstract_store_data_manager import AbstractStoreDataManager
from typing import List

class __StoreDataManager(AbstractStoreDataManager):
    #Questa classe non ha bisogno di variabili di istanza
    __slots__ = []


    def __new__(cls):
        """
        La creazione di instanze di questa classe non è necessaria, i metodi sono tutti statici e la classe è privata.
        """
        raise TypeError("Non è possibile creare istanze di questa classe.")

    @staticmethod
    def validate_path() -> None:
        """
        Implementazione:
        Il file di salvataggio deve essere contenuto nel percorso "data/store_supplies.txt".
        Verifico l'esistenza del percorso, se inesistenti creo cartella e file.
        """
        if not os.path.exists("data"):
            os.mkdir("data")
        if not os.path.exists("data/store_supplies.txt"):
            with open("data/store_supplies.txt", "w"):
                pass

    @staticmethod
    def get_supplies_from_file() -> List["Product"]:
        """
        Implementazione:
        Leggo il file e produco un oggetto Product per ogni riga salvando infine tutto in una lista.
        Un esempio di record è:
        tofu,100,4.0,2.0,available
        Questo record viene trasformato in un oggetto Product:
        Product(name, quantity, selling_price, purchase_price, status)
        """
        try:
            DM.validate_path() #uso l'alias definito alla fine del file per evitare il name mangling
            with open("data/store_supplies.txt") as f:
                data_list = [line.rstrip("\n") for line in f.readlines()]
            if len(data_list) > 0:
                data_list = \
                    list(
                        map(
                            lambda x: Product(x[0],x[1],x[2],x[3],x[4])
                            , [i.split(",") for i in data_list]
                        )
                    )
                return data_list
            return []
        except Exception as e:
            print(f"Errore durante la lettura del file.\n{e}")

    @staticmethod
    def save_file_supplies(supplies: List["Product"]) -> None:
        """
        Implementazione:
        Converto il contenuto della lista di prodotti nella codifica per il file con la struttura:
        name,quantity,selling_price,purchase_price,status
        Rappresentando un prodotto per riga.
        """
        try:
            DM.validate_path()  # uso l'alias definito alla fine del file per evitare il name mangling
            with open("data/store_supplies.txt","w") as f:
                if len(supplies) > 0:
                    f.writelines([f"{i.name},{i.quantity},{i.selling_price},{i.purchase_price},{i.status}{os.linesep}" for i in supplies])
        except Exception as e:
            print(f"Errore durante il salvataggio del file.\n{e}")

#assegno un alias
DM = __StoreDataManager