from random import choice

rounds = 1

def choose_options(): 
  options = ('piedra', 'papel', 'tijera')
  user_option = input('Piedra, papel o tijera => ')
  user_option = user_option.lower()

  
  if not user_option in options:
    print("Esa opción no es válida")
    return None, None

  
  computer_option = choice(options) 
  
  print('User option => ', user_option)
  print('computer option => ', computer_option)

  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option :
    print('Empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('El computer tiene tijera')
      print('piedra gana a tijera')
      print('User ganó')
      user_wins +=1
    else:
      print('El computer tiene papel')
      print('Papel gana a priedra')
      print('Computer gano')
      computer_wins +=1
  
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('El computer tiene piedra')
      print('Papel le gana a la piedra')
      print('User ganó')
      user_wins +=1
    else:
      print('El computer tiene tijera')
      print('Tijera gana a papel')
      print('Computer ganó')
      computer_wins +=1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('El computer tiene papel')
      print('Tijera gana a papel')
      print('User gano')
      user_wins +=1
      
    else:
      print('El computer tiene piedra')
      print('Piedra gana a tijera')
      print('Computer gano')
      computer_wins +=1
  return user_wins, computer_wins


def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  while True:

    print('*'*10)
    print('ROUND ', rounds)
    print('*'*10)
    print('computer_wins: ', computer_wins)
    print('user_wins: ', user_wins)
    rounds +=1
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    
  
    if(computer_wins == 2):
      print('El ganador es la computadora')
      break
  
    if(user_wins == 2):
      print('El ganador es el usuario')
      break

run_game()
