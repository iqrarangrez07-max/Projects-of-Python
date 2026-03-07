import os 
from datetime import datetime
class JournalManager :
    def __init__(self,filename="journal.txt"):
        self.filename=filename
    def add_entry(self):
        entry=input("Enter your journal entry : \n")
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try :
            with open(self.filename, "a") as file: 
                file.write(f"\n [{timestamp}]\n")
                file.write(entry+"\n")
                print("Entry added successfully! \n")
        except Exception as e :
            print("Error while adding entry :", e)
    def view_entries(self):
        try :
            with open(self.filename,"r") as file :
                content=file.read()
                if content.strip()=="":
                    print("No journal entries found. \n")
                else :
                    print("Your journal entries :")
                    print("-"*30)
                    print(content)
        except FileNotFoundError:
            print("Error : The journal file does not exist. Please add a new entry first. \n")
    def search_entry(self):
        keyword=input("Enter a keyword or date to search : ")
        try :
            with open(self.filename, "r") as file :
                lines=file.readlines()
                found=False
                print("\nMatching Entries : ")
                print("-"*30)
                for line in lines:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found=True
                if not found :
                    print(f"No entries were found for the keyword: {keyword}")
        except FileNotFoundError :
            print("Error : The journal file does not exist. \n")
    def delete_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries to delete. \n")
            return
        confirm=input("Are you sure you want to delete all entries? (yes/no) : ")
        if confirm.lower()=="yes":
            try :
                with open(self.filename, "w") as file:
                    pass
                print("All journal entries have been deleted.\n")
            except Exception as e :
                print("Error while deleting :", e)
        else:
            print("Deletion cancelled.\n")
def main():
        journal=JournalManager()
        while True:
            print("Welcome to Personal Journal Manager!")
            print("Please select an option :")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")
            choice=input("Enter your choice from above : ")
            if choice=="1":
                journal.add_entry()
            elif choice=="2":
                journal.view_entries()
            elif choice=="3":
                journal.search_entry()
            elif choice=="4":
                journal.delete_entries()
            elif choice=="5":
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break
            else:
                print("Invalid option. Please select a valid option. \n")
if __name__=="__main__":
    main()