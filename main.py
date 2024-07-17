print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')
print("Welcome to Laugh Tale Island, the legendary final island in the Grand Line.")
print("Your mission is to find the One Piece and become the King of the Pirates!.") 



#Write your code below this line 👇
# 1 ask user to go left or right
#.lower() function can be added at the end of input after the bracket  
left_or_right = input("You stand at a crossroad, surrounded by dense jungle. Do you want to go left towards the mountains or right towards the forest? Type 'left' or 'right'.\n")
# Make input lower case
l_or_r = left_or_right.lower()

# 2 if left, ask user to swim or wait
if l_or_r == "right":
    print("You fell into a hidden pitfall set by the Marines. Game over.")
elif l_or_r == "left":
    swim_or_wait = input("You reach a cliff overlooking the sea. Do you want to swim across the turbulent waters or wait for a ship? Type 'swim' or 'wait'.\n")
    # Make it lower case
    s_or_w = swim_or_wait.lower()
    if s_or_w == "swim":
        print("Game Over, a Sea King emerged and devoured you.")
    elif s_or_w == "wait":
        door = input("A mysterious ship arrives and takes you to a grand castle with three doors. Do you want to enter the red, yellow, or blue door? Type 'red', 'yellow' or 'blue'.\n")
        # Make it lower case
        d = door.lower()
        if d == "red":
            print("Game Over, you were engulfed in flames from Akainu's magma.")
        elif d == "blue":
            print("Game Over, wild beasts unleashed by Kaido have devoured you.")
        elif d == "yellow":
            print("You have found the One Piece! Congratulations, you are now the Pirate King! You win!")
        else:
            print("Game Over, you chose a door that does not exist.")