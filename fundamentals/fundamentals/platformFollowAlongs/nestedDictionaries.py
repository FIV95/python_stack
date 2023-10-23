users = [
      {"first": "bob", "usernumber": "0"},
      {"first": "sarah", "usernumber": "1"},
      {"first": "tim", "usernumber": "2"}
]
print([users[0]])
# to print the first name of index1
print(users[0]['first'])
# to print the usernumber of index1
print(users[0]['usernumber'])

resume_data = {
      "skills": ["front-end", "back-end", "eating"],
      "hobbies": ["rock-climbing", "basketball", "gaming"],
      "languages": ["swedish", "german", "english"]
}
# this is how to access the skills list index 0
print(resume_data['skills'][0])
# this is how to access an entire list within a dictionary
print(resume_data['skills'])

gameClasses = [

      {
       "name": ['Warrior'],
       "spells": ['Edge Slam', 'Juggernaut Blow', 'Onslaught'],
       "preffered stats": ['strength', 'vitality', 'cricial hit']
      },
      {
       "name": ['Priest'],
       "spells": ['Holy Vow', 'One Faith', 'Holy'],
       "preffered stats": ['Piety', 'vitality', 'spell speed']
      },
      {
       "name": ['Hunter'],
       "spells": ['Hot Shot', 'Rapid Fire', 'Ensnare'],
       "preffered stats": ['Dexterity', 'vitality', 'cricial hit']
      }

]

print(gameClasses[1]["spells"][0])