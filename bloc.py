from voice import parler # importation de mon fichier avec le modole pyttsx3
parler("bienvenu dans le programme ruphy qui prédit l'avenir!") # application du module et de la fonction parler
parler("commençons par ce pétit test qui prédit à 49pourcents et bientot 79,8pourcents ton avenir lointain")

print() #   de la ligne
 #---------------- début du programme-------------- #
print("==========🤖=========avenir:")
name=input("Donne ton nom:")
print("c'est magnifique comme nom,on continue ")
second_name=input("donne ton prénom ou ton deuxieme nom:")
print(name, second_name, "ton nom est magnifique voyons si tu es l'un des prédestinés")
choise=int(input("maintenant choisis ton chiffre préféré entre:3;6;8;0;2:")) # le choi d'un nombre avec la variable choise
print("bravo  on apresque fini il nous manque l'analyse")
 #----------------analyse avec les structures conditionnelles (if,else et elif)-------------- #
if name in ["agandaze","baraka","kambale","nzigire","mateso","ashuza","aganze","kasoki","mumbere",
"masika","bahati","nsimire","hamuli","tambwe","masudi","mbala","ndungo","atukuzwe","bénin"]: # la bibliotheque des noms 
    print("votre nom est bel et bien dans le livre des destins")
    if second_name in ["princesse","clarisse","délice","dénice","perpetue","pricilla",
    "daniela","joana","jenifer","plamédie","aurore","rachelle",
    "pricille","eliette","eliana","christella","cathérine","dorotée","patricia","jorgette",
    "keren","aline","alice","ariella","mirabelle","marieposa","marie","clair","cintiche",
    "quorailla"]: # la bibliotheque des prénoms pour filles et vérifie si ton prénom ne serait pas celui d'une fille
        print("tu es une fille,et ton prénom est dans les livres des déstins") # si oui ton prénom vérifie la regle et ton nom aussi ta classe est alors déterminée
        print("Tu es bien parti pour etre une des élues")
        if choise==8: #si second_name in bibliotheque fille et le choise est 8 alors tu es élu 
            print("ton chiffre préferé est aussi 8,tu es sans doute l'une des prétandates")
        elif choise==3:
            print("Tu vas gagné ta vie,c'est sur mais tu n'es pas l'élu,")
        else:
            print("tu servira dieu et tu sera riche,bye et à bientot") # fin de la structure et du cycle fille
     #------------------- début de la structure pour les hommes--------------------------- #        
    elif second_name in ["ruphin","raul","josias","madrilain","saint","rodi","pascal","eli","eben"]:
        parler("•tu es encore en course pour devenir l'élu,c'est bien,continue comme-ça et ta vie sera magnifique")
        if choise <=3:
            parler("bravo tu es un élu ta vie sera comme au paradie,tu sera trés riche!meme moi je t'envie")
            
    else:
        print("désolé mais ton prénom n'est pas celui des élus!pars tenter ta chance ailleurs")
        print("tu sera un serviteur de Dieu")
else:
    print("repare d'abort ta vie puis revient car ton avenir s'annonce décevante") # fin de la structure principale 

        



