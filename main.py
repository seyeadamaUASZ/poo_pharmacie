
# affichage d'un menu au terminal
from medicament import Medicament
from Operation import AjouterMedicament
from Operation import Approvisionnement
from Operation import Achat
import datetime


def printMenu():
    print("\n=========== MENU PHARMACIE ===========")
    print("1 - Ajouter médicament")
    print("2 - Approvisionner")
    print("3 - Acheter médicament")
    print("4 - Quantité Stock")
    print("5 - Quitter")
    print("============================\n")


def end_message():
    """
        Prints the end message at the end of the script.
    """
    print("=========== GOOD-BYE ===========")


def choice(input_msg):
    """donner le choix de l'utilisateur"""
    user_input = input(f"{input_msg} : ")
    return user_input


def __is_input_valid(user_input):
    """
        Checks if the input corresponds to a possibility of operations.

        :param user_input: User input enter in the method run().
        :return: Return True if the input corresponds to a possibility of operations
                    otherwise it return False.
    """
    return user_input in ["1", "2", "3", "4"]


def __is_quit(user_input):
    """
        Checks if the user ask for stop the script thanks to the input enter
        in the method run().

        :param user_input: User input enter in the method run().
        :return: True if the user ask for exit the script.
    """
    return not user_input == "5"


def continue_message():
    """
        Requests to press enter to continue.
    """
    input("Appuyez sur ENTRER pour continuer ...")


def operations():
    msg = " Entrer votre choix "
    user_input = choice(msg)
    if user_input == "1":
        ajoutMed = AjouterMedicament("Ajout médoc", datetime.datetime.today())
        medicament = ajoutMed.userDialog()
        print(medicament)

    elif user_input == "2":
        approvision = Approvisionnement(
            "Approvisionner", datetime.datetime.today())
        quantite = int(input("Entrer la quantité du médicament: "))
        nomMed = input("Nom médicament: ")
        medicament = Medicament(0, 0, nomMed, "")
        approvision.approvisionner(quantite, medicament)
        

    elif user_input == "3":
        achat = Achat("achat ", datetime.datetime.today())
        nomMed = input("Entrer le nom du médicament ")
        quantite = int(input("Entrer la quantité à acheter"))

        achat.calculMontant(quantite, medicament)

    elif user_input == "4":
        pass

    continue_message()


def run():
    printMenu()
    is_menu_home = True
    while is_menu_home:
        user_input = choice("Entrer votre choix ")
        if __is_input_valid(user_input):
            operations()
            printMenu()
        is_menu_home = __is_quit(user_input)
    end_message()


if __name__ == "__main__":
    run()
