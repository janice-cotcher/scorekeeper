# Score keeper for the card game 21
# initalized the starting points at 0
points = 0


def setup():
    size(300, 300)
    background(0)
    print("""
    Press 1 for Aces
    Press 0 for any Face Cards
    Enter the number on the card for all others
    """)


def cal_points():
    """
    Calculate the points for one user for the game.
    Aces are worth 11 points, Face cards are worth 10 points,
    and all others are worth the number on the card.
    """
    # state that points is a global variable
    global points
    # ace is worth 11 points
    if key == "1":
        return points + 11
    # 2 is worth 2 points
    elif key == "2":
        return points + 2
    # 3 is worth 3 points
    elif key == "3":
        return points + 3
    # 4 is worth 4 points
    elif key == "4":
        return points + 4
    # 5 is worth 5 points
    elif key == "5":
        return points + 5
    # 6 is worth 6 points
    elif key == "6":
        return points + 6
    # 7 is worth 7 points
    elif key == "7":
        return points + 7
    # 8 is worth 8 points
    elif key == "8":
        return points + 8
    # 9 is worth 9 points
    elif key == "9":
        return points + 9
    # any face card are worth 10 points
    elif key == "0":
        return points + 10

def draw():
    return


def print_points():
    """Prints the value of the points on the canvas"""
    # state that points is a global variable
    global points
    background(0)
    # text size of 150 pixels
    textSize(150)
    # convert the points to a string and put the text on the canvas
    text(str(points), 50, 200)

def keyPressed():
    # state that points is a global variable
    global points
    # make point equal to the latest output from cal_points
    points = cal_points()
    """
    If the points are equal to 21 then the user wins.
    If the points are less than 21 then the user tries again.
    If the points are more than 21 then the user loses.
    """
    if points == 21:
        print_points()
        textSize(50)
        text("You win!", 50, 250)
        points = 0
    elif points > 21:
        print_points()
        textSize(50)
        text("You lost!", 50, 250)
        points = 0
    else:
        print_points()
        textSize(20)
        text("Score is less than 21.", 50, 250)
        text("Try again.", 50, 280)
