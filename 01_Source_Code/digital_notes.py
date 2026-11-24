
import os

FILE_NAME = "notes.txt"


# Read all notes from file
def read_notes():
    notes = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split("|", 2)

                    if len(parts) == 3:
                        notes.append({
                            "id": parts[0],
                            "title": parts[1],
                            "content": parts[2]
                        })

    return notes


# Save notes to file
def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        for note in notes:
            file.write(
                note["id"] + "|" +
                note["title"] + "|" +
                note["content"] + "\n"
            )


# Generate new note ID
def generate_id(notes):
    if not notes:
        return "N1"

    numbers = []

    for note in notes:
        numbers.append(int(note["id"][1:]))

    return "N" + str(max(numbers) + 1)


# Add a note
def add_note():
    notes = read_notes()

    title = input("Title: ").strip()

    if title == "":
        print("Title cannot be empty. Note not saved.")
        return

    content = input("Content: ").strip()

    note_id = generate_id(notes)

    notes.append({
        "id": note_id,
        "title": title,
        "content": content
    })

    save_notes(notes)

    print("Note saved:", note_id, "|", title)


# View all notes
def view_notes():
    notes = read_notes()

    if not notes:
        print("No notes found.")
        return

    for note in notes:
        print("\nID:", note["id"])
        print("Title:", note["title"])
        print("Content:", note["content"])


# Search notes
def search_note():
    notes = read_notes()

    keyword = input("Enter keyword: ").strip().lower()
    found = False

    for note in notes:
        if (keyword in note["title"].lower()
                or keyword in note["content"].lower()):

            print("\nID:", note["id"])
            print("Title:", note["title"])
            print("Content:", note["content"])

            found = True

    if not found:
        print("No matching notes found.")


# Edit a note
def edit_note():
    notes = read_notes()

    note_id = input("Enter note ID: ").strip()
    found = False

    for note in notes:
        if note["id"] == note_id:
            new_content = input("New content: ").strip()

            note["content"] = new_content
            found = True
            break

    if found:
        save_notes(notes)
        print("Note updated.")
    else:
        print("Note ID does not exist.")


# Delete a note
def delete_note():
    notes = read_notes()

    note_id = input("Enter note ID: ").strip()

    new_notes = [
        note for note in notes
        if note["id"] != note_id
    ]

    if len(new_notes) == len(notes):
        print("Note ID does not exist.")
    else:
        save_notes(new_notes)
        print("Note deleted.")


# Main menu
def main():
    while True:
        print("\n===== DIGITAL NOTES MANAGEMENT SYSTEM =====")
        print("1. Add Note")
        print("2. View All Notes")
        print("3. Search Note")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            search_note()

        elif choice == "4":
            edit_note()

        elif choice == "5":
            delete_note()

        elif choice == "6":
            print("Thank you for using Digital Notes Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run program
if __name__ == "__main__":
    main()
                          
