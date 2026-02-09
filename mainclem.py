from database import Database

def show_menu():
    print("\n--- 🌊 BERKE JETSKI MANAGEMENT ---")
    print("1. List all Clients")
    print("2. Show available JetSkis")
    print("3. Add a new Client")
    print("4. Exit")
    return input("Select an option (1-4): ")

def main():
    db = Database()
    
    while True:
        choice = show_menu()

        if choice == "1":
            print("\n📋 CUSTOMER LIST:")
            results = db.fetch_all("SELECT nom, prenom, email FROM clients")
            for row in results:
                print(f"- {row[1]} {row[0]} ({row[2]})")

        elif choice == "2":
            print("\n🚀 AVAILABLE JETSKIS:")
            query = """
                SELECT j.jetski_id, m.marque, m.modele 
                FROM jetskis j
                JOIN jetski_modeles m ON j.modele_id = m.modele_id
                WHERE j.statut = 'disponible'
            """
            results = db.fetch_all(query)
            for row in results:
                print(f"ID: {row[0]} | {row[1]} {row[2]}")

        elif choice == "3":
            print("\n🆕 REGISTER NEW CLIENT:")
            nom = input("Nom: ")
            prenom = input("Prenom: ")
            email = input("Email: ")

        elif choice == "4":
            db.disconnect()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()