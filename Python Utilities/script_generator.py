import datetime, textwrap

name = input("Enter your name: ").strip()
age = input("Enter your age: ").strip()
city = input("Enter your city: ").strip()
profession = input("Enter your profession: ").strip()
hobby = input("Enter your hobby: ").strip()

intro_message = (
    f"Hello, my name is {name}. I am {age} years old. I live in {city}. I am a {profession}. My hobby is {hobby}. "
    f"Nice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_message += f"Logged on: {current_date}"

border = "-" * 50
final_message = f"{border}\n {intro_message}\n {border}"

print(textwrap.dedent(final_message))
save = input("Do you want to save the message? (y/n): ").strip().lower()
if save == "y":
    file_name = f"{name.lower().replace(' ', '_')}_{current_date}.txt";
    with open(file_name, "w") as f:
        f.write(final_message)
    print(f"Message saved to {file_name}")