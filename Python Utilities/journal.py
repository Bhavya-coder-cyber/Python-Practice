import datetime

current_date = datetime.datetime.now()
date_str = current_date.strftime("%Y-%m-%d - %I:%M %p")

entry = input("What did you do today? ").strip()
productivity = input("How productive were you today?(1, 5, optional) ").strip()

journal_entry = f"\n{date_str}\n{entry}"
if productivity:
    journal_entry += f"\nProductivity: {productivity}"
journal_entry += "\n" + "-" * 50

with open("journal.txt", "a", encoding="utf-8") as f:
    f.write(journal_entry)

print("Journal entry saved to journal.txt")