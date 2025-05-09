from core import Store

"""
L'import all'interno del file core/__init__.py mi permette di importare direttamente la classe Store di core/store.py
"""

if __name__ == '__main__':
    s = Store()
    print("Per visualizzare i comandi disponibili digita 'aiuto', altrimenti digita un comando.")
    while True:
        query = input("\nInserisci un comando: ")
        if query == "aiuto":
            s.help_query()
        elif query == "elenca":
            s.list_query()
        elif query == "aggiungi":
            s.add_query()
        elif query == "vendita":
            s.sell_query()
        elif query == "profitti":
            s.profit_query()
        elif query == "chiudi":
            print("Bye bye")
            break
        else:
            print("Comando non valido")
            s.help_query()
