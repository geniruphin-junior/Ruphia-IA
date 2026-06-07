from modules.conversation import discuter
from modules.conversation import discuter
from modules.memoire import memoire
from voice import parler

def main():
    
    print("=== Ruphia est en ligne 🤖 ===")
   
    while True:
        user = input("Ruphin: ")
       
        if user.lower() in ["quit", "exit"]:
            print("Ruphia : À bientôt 👋")
            break
       
        reponse = discuter(user)
        print("Ruphia :", reponse)
        


if __name__ == "__main__":
    main()
