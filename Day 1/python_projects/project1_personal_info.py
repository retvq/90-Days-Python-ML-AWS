# NOTE: Personal Info Collector

# -----------------------
#Welcome Text
# -----------------------
print("\n\n"+"=" * 50)
print("\tPERSONAL INFO COLLECTOR")
print("=" * 50)
print("\nWelcome! We'll collect some info and then present it as a personal biography!!")

# -----------------------
# Get User Details
# -----------------------
first_name = input("Enter your Firstname: ").strip()
last_name = input("Enter your LastName: ").strip()
nick_name = input("Enter your NickName: ").strip()
age = int(input("Enter your Age: ").strip())
city = input("Enter your City: ").strip()
profession = input("Enter your Profession: ").strip()
email = input("Enter your Email: ").strip()
while True:
    if ('@' in email): break
    else: email = input("Please enter correct email: ".strip())
hobbies = input("Mention 3 Hobbies (seprated by whitespaces): ").strip()
hobby1, hobby2, hobby3 = hobbies.split(' ')
# -----------------------
current_year = 2025
birth_year = current_year - age
full_name = f"{first_name} {last_name}"

# -----------------------
# Display Details

print("\n"+"=" * 50)
print("Your Persoal Biography:")
print("=" * 50)
biography = ""
biography = f"""
Name:           {full_name}
Age:            {age}
Birth Year:     {birth_year}
Location:       {city}
Profession:     {profession}
Mail:           {email}
\nAbout: {full_name} is a {age} years old {profession}, living in {city}.
Born in {birth_year}, {first_name} is making a significant impact in their field.
{first_name} is closely called as {nick_name}, their hobbies include {hobby1}, {hobby2} and {hobby3}.
To contact {first_name}, Mail them at {email}.

"""

print(biography)
# -----------------------
# Fun Statistics

print("\nFun Stats\n")
print(f"Days Lived:         {age*365:,}")
print(f"Hours Lived:        {age*365*25:,}")
print(f"Years until age 60: {60-age}")
print("=" * 50)