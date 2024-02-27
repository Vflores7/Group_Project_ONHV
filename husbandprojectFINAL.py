


def test_husband_requirements():
    print("Hello, welcome to the husband requirements test\n")
    name = input("What's your name?\n")
    answer = input("Who's husband requirements would you like to be tested on?\n" + "Oli, Nati, Hanna or Vale?\n\n").lower()
    score = 0

    def draw_heart():
        heart = [
            "  **     **  ",
            "****    ****",
            "****** ******",
            "*************",
            " *********** ",
            "  *********  ",
            "   *******   ",
            "    *****    ",
            "     ***     ",
            "      *      "
        ]
        for line in heart:
            print(line.center(20))

    def display_hearts(score):
        heart2 = " ❤️ "
        hearts = heart2 * score
        return(hearts)

    if answer in ["oli", "olivia", "o"]:
        tall = input("Are you taller than Oli?\n")
        if tall in ["yes", "Yes", "Y", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        athletic = input("Are you athletic?\n")
        if athletic in ["yes", "Yes", "Y", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        stable = input("Are you emotionally stable?\n")
        if stable in ["yes", "Yes", "Y", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        rich = input("Are you rich AF?\n")
        if rich in ["yes", "Yes", "Y", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        shoulders = input("Do you have broad shoulders?\n")
        if shoulders in ["yes", "Yes", "Y", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        latino = input("Are you latino?\n")
        if latino in ["yes", "Yes", "Y", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        if score >= 15:
            import turtle

            t = turtle.Turtle()
            s = turtle.Turtle()

            t.hideturtle()
            t.goto(0, -10)

            t.pensize(3)
            t.color("red")
            t.begin_fill()
            t.left(140)
            t.forward(180)
            t.circle(-90, 200)
            t.setheading(60)
            t.circle(-90, 200)
            t.forward(178)
            t.end_fill()

            t.penup()

            t.goto(-130, 130)
            t.pendown()
            t.color('white')
            t.write("Congratulations! \n You are husband material ;)", font=("Courier", 15))
            t.penup()
            t.goto(-90, 100)
            t.pendown()
            t.color('white')
            t.write("[Click on red 'x' above]", font=("Courier", 10))
            turtle.done()

        else:
            print("Sorry, you don't qualify this time. But don't give up!")

    elif answer in ["nati", "n", "natalia"]:

        smoke = input("Do you smoke?\n")

        if smoke in ["no", "n"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        family = input("Are you close to your family?\n")

        if family in ["yes", "y"]:
            score += 2
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        hoe = input("Are you a retired hoe?\n")

        if hoe in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        jewelry = input("Do you wear jewelry (rings, bracelets, and necklaces)?\n")

        if jewelry in ["yes", "y"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        gym = input("Do you workout?\n")

        if gym in ["yes", "y"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        fulfillement = input("Do you think being personally fulfilled is important?\n")

        if fulfillement in ["yes", "y"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        communication = input("Do you value open and truthful communication?\n")

        if communication in ["yes", "y"]:
            score += 2
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        adventure = input("Are you willing to try new experiences and get out of your comfort zone?\n")

        if adventure in ["yes", "y"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        eatinghabits = input("Do you have healthy eating habits?\n")

        if eatinghabits in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        reading = input("Do you like reading?\n")

        if reading in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        theatre = input("Do you like going to the theatre?\n")

        if theatre in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        manners = input("Do you have good manners?\n")

        if manners in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        sports = input("Do you play or used to play any sports?\n")

        if sports in ["yes", "y"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        movies = input("Do you like old movies?\n")

        if movies in ["yes", "y"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        music = input("Do you like classical music?\n")

        if music in ["yes", "y"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        humor = input("Do you like dark humor?\n")

        if humor in ["yes", "y"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        friends = input("Do you have a healthy close group of friends?\n")

        if friends in ["yes", "y"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        murcia = input("Do you like Murcia?\n")

        if murcia in ["yes", "y"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        religion = input("Do you believe in God?\n")

        if religion in ["yes", "y"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        growth = input("Do you seek personal growth?\n")

        if growth in ["yes", "y"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        relationship = input("Do you see yourself in a long-term relationship?\n")

        if relationship in ["yes", "y"]:
            score += 1
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        children = input("Do you want to have kids?\n")

        if children in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        animals = input("Do you want to have a dog?\n")

        if animals in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        if score >= 25:
            import turtle

            t = turtle.Turtle()
            s = turtle.Turtle()

            t.hideturtle()
            t.goto(0, -10)

            t.pensize(3)
            t.color("red")
            t.begin_fill()
            t.left(140)
            t.forward(180)
            t.circle(-90, 200)
            t.setheading(60)
            t.circle(-90, 200)
            t.forward(178)
            t.end_fill()

            t.penup()

            t.goto(-130, 130)
            t.pendown()
            t.color('white')
            t.write("Congratulations! \n You are husband material ;)", font=("Courier", 15))
            t.penup()
            t.goto(-90, 100)
            t.pendown()
            t.color('white')
            t.write("[Click on red 'x' above]", font=("Courier", 10))
            turtle.done()

        else:
            print("Sorry, you don't qualify this time. But don't give up!")


    elif answer in ["hanna", "hann"]:

        older = input("Are you older than 22?\n")

        if older in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        tennis = input("Do you like tennis?\n")

        if tennis in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        time = input("Are you always on time?\n")

        if time in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        baking = input("Do you like baking?\n")

        if baking in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        city = input("Do you prefer the city over the countryside?\n")

        if city in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        countries = input("Would you like to live in more than three different countries in the future?\n")

        if countries in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        languages = input("Do you speak more than three languages?\n")

        if languages in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        nightowl = input("Do you often stay awake until late?\n")

        if nightowl in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        suits = input("Do you like wearing suits?\n")

        if suits in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

        if score >= 21:
            import turtle

            t = turtle.Turtle()
            s = turtle.Turtle()

            t.hideturtle()
            t.goto(0, -10)

            t.pensize(3)
            t.color("red")
            t.begin_fill()
            t.left(140)
            t.forward(180)
            t.circle(-90, 200)
            t.setheading(60)
            t.circle(-90, 200)
            t.forward(178)
            t.end_fill()

            t.penup()

            t.goto(-130, 130)
            t.pendown()
            t.color('white')
            t.write("Congratulations! \n You are husband material ;)", font=("Courier", 15))
            t.penup()
            t.goto(-90, 100)
            t.pendown()
            t.color('white')
            t.write("[Click on red 'x' above]", font=("Courier", 10))
            turtle.done()

        else:
            print("Sorry, you don't qualify this time. But don't give up!")

    elif answer in ["vale", "v", "valeria"]:
        stable = input("Are you emotionally stable?\n")
        if stable in ["yes", "y"]:
            score += 3
            print("Nice! Your current score has risen to: ")
            print(display_hearts(score))

            tall = input("Are you taller than Valeria?\n")
            if tall in ["yes", "y"]:
                score += 3
                print("Nice! Your current score has risen to: ")
                print(display_hearts(score))

            self_esteem = int(input("From 1 to 10, how would you rate your self-esteem?\n"))
            if 1 <= self_esteem <= 10:
                score += self_esteem
                print("Nice! Your current score has risen to: ")
                print(display_hearts(score))

            else:
                print("Please enter a number between 1 and 10.")
                return

            workout = input("Do you deadlift more than 90 kilos?\n")
            if workout in ["yes", "y"]:
                score += 3
                print("Nice! Your current score has risen to: ")
                print(display_hearts(score))

            travel = int(input("From 1 to 10, how much do you like to travel?\n"))
            if 1 <= travel <= 10:
                score += travel
                print("Nice! Your current score has risen to: ")
                print(display_hearts(score))

            else:
                print("Please enter a number between 1 and 10.")
                return
            adventure = input("Are you willing to try new experiences and get out of your comfort zone?\n")

            if adventure in ["yes", "y"]:
                score += 1
                print("Nice! Your current score has risen to: ")
                print(display_hearts(score))

            communication = int(input("From 1 to 10, how well do you communicate your needs and feelings?\n"))
            if 1 <= communication <= 10:
                score += communication
                print("Nice! Your current score has risen to: ")
                print(display_hearts(score))

            else:
                print("Please enter a number between 1 and 10.")
                return
            relationship = input("Do you see yourself in a long-term relationship?\n")

            if relationship in ["yes", "y"]:
                score += 1
                print("Nice! Your current score has risen to: ")
                print(display_hearts(score))

            children = input("Do you want to have kids?\n")

            if children in ["yes", "y"]:
                score += 3
                print("Nice! Your current score has risen to: ")
                print(display_hearts(score))

            cats = input("Do you LOVE cats?\n")

            if cats in ["yes", "y"]:
                score += 1
                print("Nice! Your current score has risen to: ")
                print(display_hearts(score))

            if score >= 29:
                import turtle

                t = turtle.Turtle()
                s = turtle.Turtle()

                t.hideturtle()
                t.goto(0, -10)

                t.pensize(3)
                t.color("red")
                t.begin_fill()
                t.left(140)
                t.forward(180)
                t.circle(-90, 200)
                t.setheading(60)
                t.circle(-90, 200)
                t.forward(178)
                t.end_fill()

                t.penup()

                t.goto(-130, 130)
                t.pendown()
                t.color('white')
                t.write("Congratulations! \n You are husband material ;)", font=("Courier", 15))
                t.penup()
                t.goto(-90, 100)
                t.pendown()
                t.color('white')
                t.write("[Click on red 'x' above]", font=("Courier", 10))
                turtle.done()

            else:
                print("Sorry, you don't qualify this time. But don't give up!")

    else:
        print("Invalid input. Please choose Oli, Nati, Hanna, or Vale.")
        return


    print("Thank you for your response. Your total score is:", score)
    draw_heart()

    return score


def start_again():
    restart = input("Would you like to restart? Type 'start' to begin again, or any other key to exit.\n").lower()
    if restart == "start":
        test_husband_requirements()


test_husband_requirements()
start_again()