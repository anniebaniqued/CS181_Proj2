import player1.player
import player2.player
import game_interface
import random
import signal
import sys
import time
import traceback
from optparse import OptionParser

class TimeoutException(Exception):
  def __init__(self):
    pass

def get_move(view, cmd, options, player_id):
  def timeout_handler(signum, frame):
    raise TimeoutException()
  signal.signal(signal.SIGALRM, timeout_handler)
  signal.alarm(1)
  try: 
    (mv, eat) = cmd(view)
    # Clear the alarm.
    signal.alarm(0)
  except TimeoutException:
    # Return a random value
    # Should probably log this to the interface
    (mv, eat) = (random.randint(0, 4), False)
    error_str = 'Error in move selection (%d).' % view.GetRound()
    if options.display:
      game_interface.curses_debug(player_id, error_str)
    else:
      print error_str
  return (mv, eat)

def run(options):
  game = game_interface.GameInterface(20,10,1, 100,1)
  """
  game = game_interface.GameInterface(options.plant_bonus,
                                      options.plant_penalty,
                                      options.observation_cost,
                                      options.starting_life,
                                      options.life_per_turn)
  if options.display:
    if game_interface.curses_init() < 0:
      return
    game_interface.curses_draw_board(game)"""
  player1_view = game.GetPlayer1View()
  player2_view = game.GetPlayer2View()


  # Keep running until one player runs out of life.
  roundNum = 0
  while True:
    (mv1, eat1) = get_move(player1_view, player1.player.get_move, options, 1)
    (mv2, eat2) = get_move(player2_view, player2.player.get_move, options, 2)

    old_life1 = player1_view.GetLife()
    old_life2 = player2_view.GetLife()
    game.ExecuteMoves(mv1, eat1, mv2, eat2)
    
    old_xpos1 = player1_view.GetXPos()
    old_xpos2 = player2_view.GetXPos()
    old_ypos1 = player1_view.GetYPos()
    old_ypos2 = player2_view.GetYPos()

    if False: #OPTIONS.DISPLAY
      game_interface.curses_draw_board(game)
      game_interface.curses_init_round(game)
      
    else:
      #print mv1, eat1, mv2, eat2
      #print player1_view.GetLife(), player2_view.GetLife()
      #print "Location1: (" + str(player1_view.GetXPos()) + ", " + str(player1_view.GetYPos()) + ")\n"
      #print "Location2: (" + str(player2_view.GetXPos()) + ", " + str(player2_view.GetYPos()) + ")\n"
      #print "RoundNum: " + str(player1_view.GetRound()) + " Coords: (" + str(player1_view.GetXPos()) + ", " + str(player1_view.GetYPos()) + ")"
      # if eat1:
      #   if player1_view.GetLife() - old_life1 > 0:
      #     #print "Location1: (" + str(player1_view.GetXPos()) + ", " + str(player1_view.GetYPos()) + "): Nutritious" + "\n"
      #     print "1 " + str(player1_view.GetXPos()) + " " + str(player1_view.GetYPos()) + " N" + "\n"
      #   else: 
      #     #print "Location1: (" + str(player1_view.GetXPos()) + ", " + str(player1_view.GetYPos()) + "): Poisonous" + "\n"
      #     print "1 " + str(player1_view.GetXPos()) + " " + str(player1_view.GetYPos()) + " P" + "\n"
      
      # if eat2:
      #   if player2_view.GetLife() - old_life2 > 0:
      #     #print "Location2: (" + str(player2_view.GetXPos()) + ", " + str(player2_view.GetYPos()) + "): Nutritious" + "\n"
      #     print "2 " + str(player2_view.GetXPos()) + " " + str(player2_view.GetYPos()) + " N" + "\n"
        
      #   else: 
      #     #print "Location2: (" + str(player2_view.GetXPos()) + ", " + str(player2_view.GetYPos()) + "): Poisonous" + "\n"
      #     print "2 " + str(player2_view.GetXPos()) + " " + str(player2_view.GetYPos()) + " P" + "\n"
      
      if eat1:
        if player1_view.GetLife() - old_life1 > 0:
          #print "Location1: (" + str(player1_view.GetXPos()) + ", " + str(player1_view.GetYPos()) + "): Nutritious" + "\n"
          print "N  1 " + str(old_xpos1) + " " + str(old_ypos1) + " N" + "\n"
        else: 
          #print "Location1: (" + str(player1_view.GetXPos()) + ", " + str(player1_view.GetYPos()) + "): Poisonous" + "\n"
          print "P  1 " + str(old_xpos1) + " " + str(old_ypos1) + " P" + "\n"
      #else: 
      #  print "1 " + str(old_xpos1) + " " + str(old_ypos1) + "\n"
      if eat2:
        if player2_view.GetLife() - old_life2 > 0:
          #print "Location2: (" + str(player2_view.GetXPos()) + ", " + str(player2_view.GetYPos()) + "): Nutritious" + "\n"
          print "N  2 " + str(old_xpos2) + " " + str(old_ypos2) + " N" + "\n"
        else: 
          #print "Location2: (" + str(player2_view.GetXPos()) + ", " + str(player2_view.GetYPos()) + "): Poisonous" + "\n"
          print "P  2 " + str(old_xpos2) + " " + str(old_ypos2) + " P" + "\n"
      #else: 
      #  print "2 " + str(old_xpos2) + " " + str(old_ypos2) + "\n"


    # Check whether someone's life is negative.
    l1 = player1_view.GetLife()
    l2 = player2_view.GetLife()

    if l1 <= 0 or l2 <= 0:
      if False: # OPTIONS.DISPLAY
        winner = 0
        if l1 < l2:
          winner = 2
        else:
          winner = 1
        game_interface.curses_declare_winner(winner)
      else:
        if l1 == l2:
          print 'Tie, remaining life: %d v. %d' % (l1, l2)
          return 2
        elif l1 < l2:
          print 'Player 2 wins: %d v. %d' % (l1, l2)
          return 0
        else:
          print 'Player 1 wins: %d v. %d' % (l1, l2)
          return 1
      # Wait for input
      sys.stdin.read(1)
      if options.display:
        game_interface.curses_close()
      break

def main(argv):
  parser = OptionParser()
  parser.add_option("-d", action="store", dest="display", default=1, type=int,
                    help="whether to display the GUI board")
  parser.add_option("--plant_bonus", dest="plant_bonus", default=20,
                    help="bonus for eating a nutritious plant",type=int)
  parser.add_option("--plant_penalty", dest="plant_penalty", default=10,
                    help="penalty for eating a poisonous plant",type=int)
  parser.add_option("--observation_cost", dest="observation_cost", default=1,
                    help="cost for getting an image for a plant",type=int)
  parser.add_option("--starting_life", dest="starting_life", default=100,
                    help="starting life",type=int)
  parser.add_option("--life_per_turn", dest="life_per_turn", default=1,
                    help="life spent per turn",type=int)
  (options, args) = parser.parse_args()

  try:
    run(options)
  except KeyboardInterrupt:
    if options.display:
      game_interface.curses_close()
  except:
    game_interface.curses_close()
    traceback.print_exc(file=sys.stdout)

if __name__ == '__main__':
  main(sys.argv)
