import json
from datetime import datetime


# Функция для чтения заметок из файла
def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        notes = []
    return notes


# Функция для сохранения заметок в файл
def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)


# Функция для добавления новой заметки
def add_note(title, message):
    notes = load_notes()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": timestamp,
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")


# Функция для вывода списка всех заметок
def list_notes():
    notes = load_notes()
    for note in notes:
        print(
            f"ID: {note['id']}, Заголовок: {note['title']}, Дата/время: {note['timestamp']}"
        )


# Функция для удаления заметки по ID
def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")


# Функция для редактирования заметки по ID
def edit_note(note_id, title, message):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["message"] = message
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")


# Основная функция программы
def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить новую заметку")
        print("2. Вывести список всех заметок")
        print("3. Удалить заметку")
        print("4. Редактировать заметку")
        print("5. Выйти из программы")
        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            message = input("Введите текст заметки: ")
            add_note(title, message)
        elif choice == "2":
            list_notes()
        elif choice == "3":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            message = input("Введите новый текст заметки: ")
            edit_note(note_id, title, message)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
