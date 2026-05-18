import os

FILE_NAME = "library_records.txt"

def add_borrow_record():
    """Allows a user to add a book title, borrower name, and borrow date to the file."""
    print("\n--- Add New Borrow Record ---")
    book_title = input("Enter Book Title: ").strip()
    borrower_name = input("Enter Borrower Name: ").strip()
    date_borrowed = input("Enter Date Borrowed (DD/MM/YYYY): ").strip()
    
    with open(FILE_NAME, "a") as file:
        file.write(f"{book_title}|{borrower_name}|{date_borrowed}\n")
    print("Record saved successfully!")

def display_all_records():
    """Displays all records stored in the file and handles missing file issues gracefully."""
    print("\n--- Saved Library Records ---")
    
    # Handle the situation where the file does not yet exist
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("Notification: No records found. The library records file does not exist yet.")
        return

    with open(FILE_NAME, "r") as file:
        print(f"{'Book Title':<25} | {'Borrower Name':<20} | {'Date Borrowed':<15}")
        print("-" * 66)
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 3:
                print(f"{parts[0]:<25} | {parts[1]:<20} | {parts[2]:<15}")

def display_total_borrowed():
    """Counts and displays the total number of books borrowed."""
    if not os.path.exists(FILE_NAME):
        print("\nTotal Books Borrowed: 0 (File does not exist)")
        return

    count = 0
    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip():
                count += 1
    print(f"\nTotal Number of Books Borrowed: {count}")

def main():
    while True:
        print("\n================================")
        print("   LIBRARY RECORDS MANAGEMENT   ")
        print("================================")
        print("1. Add Borrow Record")
        print("2. Display All Records")
        print("3. View Total Books Borrowed")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            add_borrow_record()
        elif choice == "2":
            display_all_records()
        elif choice == "3":
            display_total_borrowed()
        elif choice == "4":
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
