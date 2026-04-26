import psycopg2
import csv
import json
from config import load_config


def get_conn():
    return psycopg2.connect(**load_config())


def execute_sql_file(filename):
    with get_conn() as conn:
        with conn.cursor() as cur:
            with open(filename, "r", encoding="utf-8") as file:
                cur.execute(file.read())
    print(f"✅ {filename} executed")


def add_contact(name, email, birthday, group_name):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO groups(name)
                VALUES (%s)
                ON CONFLICT (name) DO NOTHING;
            """, (group_name,))

            cur.execute("SELECT id FROM groups WHERE name = %s;", (group_name,))
            group_id = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO contacts(name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (name) DO UPDATE
                SET email = EXCLUDED.email,
                    birthday = EXCLUDED.birthday,
                    group_id = EXCLUDED.group_id;
            """, (name, email, birthday, group_id))


def add_phone(name, phone, phone_type):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL add_phone(%s, %s, %s);", (name, phone, phone_type))


def filter_by_group(group_name):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
                FROM contacts c
                LEFT JOIN groups g ON c.group_id = g.id
                LEFT JOIN phones p ON c.id = p.contact_id
                WHERE g.name = %s
                ORDER BY c.name;
            """, (group_name,))
            print_rows(cur.fetchall())


def search_by_email(query):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT name, email, birthday
                FROM contacts
                WHERE email ILIKE %s;
            """, (f"%{query}%",))
            for row in cur.fetchall():
                print(row)


def search_all(query):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts(%s);", (query,))
            print_rows(cur.fetchall())


def sort_contacts(sort_by):
    allowed = {
        "name": "c.name",
        "birthday": "c.birthday",
        "date": "c.created_at"
    }

    if sort_by not in allowed:
        print("❌ Sort only by: name, birthday, date")
        return

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT c.name, c.email, c.birthday, g.name
                FROM contacts c
                LEFT JOIN groups g ON c.group_id = g.id
                ORDER BY {allowed[sort_by]};
            """)
            for row in cur.fetchall():
                print(row)


def pagination_loop(limit=3):
    offset = 0

    while True:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT c.name, c.email, c.birthday, g.name
                    FROM contacts c
                    LEFT JOIN groups g ON c.group_id = g.id
                    ORDER BY c.name
                    LIMIT %s OFFSET %s;
                """, (limit, offset))

                rows = cur.fetchall()

                print(f"\n--- Page offset {offset} ---")
                for row in rows:
                    print(row)

        command = input("next / prev / quit: ").lower()

        if command == "next":
            offset += limit
        elif command == "prev":
            offset = max(0, offset - limit)
        elif command == "quit":
            break
        else:
            print("❌ Unknown command")


def export_json(filename="contacts.json"):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.id, c.name, c.email, c.birthday, g.name
                FROM contacts c
                LEFT JOIN groups g ON c.group_id = g.id
                ORDER BY c.name;
            """)

            contacts = []

            for contact_id, name, email, birthday, group_name in cur.fetchall():
                cur.execute("""
                    SELECT phone, type
                    FROM phones
                    WHERE contact_id = %s;
                """, (contact_id,))

                phones = [
                    {"phone": p[0], "type": p[1]}
                    for p in cur.fetchall()
                ]

                contacts.append({
                    "name": name,
                    "email": email,
                    "birthday": str(birthday) if birthday else None,
                    "group": group_name,
                    "phones": phones
                })

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)

    print("✅ Exported to JSON")


def import_json(filename="contacts.json"):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        name = item["name"]

        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM contacts WHERE name = %s;", (name,))
                exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists. skip/overwrite: ").lower()
            if choice == "skip":
                continue

        add_contact(
            item["name"],
            item.get("email"),
            item.get("birthday"),
            item.get("group", "Other")
        )

        for phone in item.get("phones", []):
            add_phone(item["name"], phone["phone"], phone["type"])

    print("✅ JSON imported")


def import_csv_extended(filename="contacts.csv"):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            add_contact(
                row["name"],
                row["email"],
                row["birthday"],
                row["group"]
            )

            add_phone(
                row["name"],
                row["phone"],
                row["phone_type"]
            )

    print("✅ CSV imported")


def print_rows(rows):
    for row in rows:
        print(row)


def menu():
    while True:
        print("""
1. Search all fields
2. Filter by group
3. Search by email
4. Sort contacts
5. Pagination
6. Export JSON
7. Import JSON
8. Import CSV
9. Add phone
10. Move to group
0. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            search_all(input("Search: "))

        elif choice == "2":
            filter_by_group(input("Group: "))

        elif choice == "3":
            search_by_email(input("Email search: "))

        elif choice == "4":
            sort_contacts(input("Sort by name/birthday/date: "))

        elif choice == "5":
            pagination_loop()

        elif choice == "6":
            export_json()

        elif choice == "7":
            import_json()

        elif choice == "8":
            import_csv_extended()

        elif choice == "9":
            add_phone(
                input("Contact name: "),
                input("Phone: "),
                input("Type home/work/mobile: ")
            )

        elif choice == "10":
            with get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "CALL move_to_group(%s, %s);",
                        (input("Contact name: "), input("Group name: "))
                    )

        elif choice == "0":
            break

        else:
            print("❌ Wrong choice")


if __name__ == "__main__":
    menu()