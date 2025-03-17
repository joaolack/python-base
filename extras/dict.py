flamengoPlayers = [
  {'name': 'Gerson', 'position': 'Midfielder', 'jersey number': '8'},
  {'name': 'Rossi', 'position': 'Goalkeeper', 'jersey number': '1'},
  {'name': 'Arrascaeta', 'position': 'Midfielder', 'jersey number': '14'},
]


for i in flamengoPlayers:
  print(i['name'], "Position: ", i['position'])
  if (i['name'] == 'Arrascaeta'):
    i['jersey number'] = '10'
    new = {'gols': 2, 'assist': 2}
    i.update(new)
  elif (i['name'] == 'Gerson'):
    new2 = {'gols': 1, 'assists': 1}
    i.update(new2)
  else:
    new3 = {'gols': 0, 'assists': 0}
    i.update(new3)

for i in flamengoPlayers:
  print()
  for chave, valor in i.items():
    print(chave, ": ", valor)
    