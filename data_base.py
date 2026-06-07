print("========Ruphy_base-😃-===========")
print("pret pour entrer dans le systeme RuphyEngine")
name_user=input("saisis ton nom : ")
print("salut", name_user)
environ=input("veuiller mettre l'environnement")
print(name_user ,"tu prefere entrer dans",environ)
pass_word=input("saisis le mot de passe: ")
print("es tu sur que ceci est le vrai mot de passe car l'analise va débuter ")
# Début de l'algoritme
if environ =="ruphy":
    if pass_word=="1234":
        if name_user=="RUPHIN":
            input("bien venu maitre,que desire tu car ta cérémonie d'accesion approche:")
            print("mes mises à jours ne sont pas pretes")
        elif name_user=="admin":
            input("fait ta commande mon admin")
            print("desolé programme non executable dans le terminal RuphinEngine")
        else:
            print("environnement ruphy ouvert,partez executer le serveur")
    elif pass_word=="123":
        print("ton mot de passe doit contenir 4 chiffres tu réessayeras la fois prochaine")
    else:
        print("la base ruphy ne reconnait pas ce mot de passe tu es un infiltré")
elif environ=="ruphy-data":
    if pass_word=="2345":
        input(f"{name_user} welcome to data_base are you sur to continue this program:")
        print("url du site ruphy est http://localhost:300")
    else:
        print("tu n'es pas un admin ,le pass_word est incorecte")
elif environ=="ruphia":
    if pass_word=="0037":
        if name_user in ["ruphin","gloire"]:
            print(f"maitre {name_user} bienvenu dans la base ruphia")
            print("l'adresse du serveur est http://127.01:300")
        else:
            print("welcome dans la base ruphia")
    else:
        print(f"mot de passe {pass_word} est incorrect")
else:
    print("la base n'existe pas dans la data_base ruphy")







