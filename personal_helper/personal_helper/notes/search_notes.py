"""
The code now includes a new feature to search for notes based on a keyword. 
When the user selects the option to search notes, they can enter a keyword, 
and the program will find and display the notes containing the keyword in their titles. 
The search is case-insensitive, and the matching notes' titles and contents are printed on the screen. 
If no matching notes are found, a "No notes found" message is displayed.
"""


def search_notes():
    keyword = input('Enter a keyword to search: ')
    found_notes = []

    with open('notes.txt', 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if lines[i].startswith('Title:') and keyword.lower() in lines[i].lower():
                title = lines[i][7:].strip()
                content = lines[i+1][6:].strip()
                note = {'title': title, 'content': content}
                found_notes.append(note)
                i += 2
            else:
                i += 1

    if found_notes:
        print('Found notes:')
        for note in found_notes:
            print(f"Title: {note['title']}")
            print(f"Text: {note['content']}")
            print()
    else:
        print('No notes found.')


if __name__ == "__main__":
    search_notes()

