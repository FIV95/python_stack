
student_info = [
      {"first_name": "Michael", "last_name": "Choi"},
      {"first_name": "John", "last_name": "Supsupin"},
      {"first_name": "Mark", "last_name": "Guillen"},
      {"first_name": "KB", "last_name": "Tonel"},
      ]
fullnames = []
for eachDictionary in student_info:
      first_name = eachDictionary.get("first_name", "")
      last_name = eachDictionary.get("last_name", "")
      full_name = f'{first_name} {last_name}'
      eachDictionary["full_name"] = full_name
print(student_info)