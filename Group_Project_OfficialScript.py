def test_husband_requirements():
    print("Hello, welcome to the husband requirements test\n")
    name = input("What's your name?\n")
    answer = input("Who's husband requirements would you like to be tested on?\n" + "Oli, Nati, Hanna or Vale?\n\n").lower()
    score = 0

    if answer in ["oli", "olivia", "o"]:
        tall = input("Are you taller than Oli?\n")
        if tall in ["yes", "Yes", "Y", "y"]:
            score += 3

        athletic = input("Are you athletic?\n")
        if athletic in ["yes", "Yes", "Y", "y"]:
            score += 3

        stable = input("Are you emotionally stable?\n")
        if stable in ["yes", "Yes", "Y", "y"]:
            score += 3

        rich = input("Are you rich AF?\n")
        if rich in ["yes", "Yes", "Y", "y"]:
            score += 3

        shoulders = input("Do you have broad shoulders?\n")
        if shoulders in ["yes", "Yes", "Y", "y"]:
            score += 3

        latino = input("Are you latino?\n")
        if latino in ["yes", "Yes", "Y", "y"]:
            score += 3

        if score >= 15:
            print(f"Congratulations, {name}! You qualify to be {answer.capitalize()}'s husband!")
        else:
            print("Sorry, you don't qualify this time. But don't give up!")

    elif answer in ["nati", "n", "natalia"]:

        smoke = input("Do you smoke?\n")

        if smoke in ["no", "n"]:
            score += 1

        family = input("Are you close to your family?\n")

        if family in ["yes", "y"]:
            score += 2

        hoe = input("Are you a retired hoe?\n")

        if hoe in ["yes", "y"]:
            score += 3

        jewelry = input("Do you wear jewelry (rings, bracelets, and necklaces)?\n")

        if jewelry in ["yes", "y"]:
            score += 1

        gym = input("Do you workout?\n")

        if gym in ["yes", "y"]:
            score += 1

        fulfillement = input("Do you think being personally fulfilled is important?\n")

        if fulfillement in ["yes", "y"]:
            score += 1

        communication = input("Do you value open and truthful communication?\n")

        if communication in ["yes", "y"]:
            score += 2

        adventure = input("Are you willing to try new experiences and get out of your comfort zone?\n")

        if adventure in ["yes", "y"]:
            score += 1

        eatinghabits = input("Do you have healthy eating habits?\n")

        if eatinghabits in ["yes", "y"]:
            score += 3

        reading = input("Do you like reading?\n")

        if reading in ["yes", "y"]:
            score += 3

        theatre = input("Do you like going to the theatre?\n")

        if theatre in ["yes", "y"]:
            score += 3

        manners = input("Do you have good manners?\n")

        if manners in ["yes", "y"]:
            score += 3

        sports = input("Do you play or used to play any sports?\n")

        if sports in ["yes", "y"]:
            score += 1

        movies = input("Do you like old movies?\n")

        if movies in ["yes", "y"]:
            score += 1

        music = input("Do you like classical music?\n")

        if music in ["yes", "y"]:
            score += 1

        humor = input("Do you like dark humor?\n")

        if humor in ["yes", "y"]:
            score += 1

        friends = input("Do you have a healthy close group of friends?\n")

        if friends in ["yes", "y"]:
            score += 1

        murcia = input("Do you like Murcia?\n")

        if murcia in ["yes", "y"]:
            score += 1

        religion = input("Do you believe in God?\n")

        if religion in ["yes", "y"]:
            score += 1

        growth = input("Do you seek personal growth?\n")

        if growth in ["yes", "y"]:
            score += 1

        relationship = input("Do you see yourself in a long-term relationship?\n")

        if relationship in ["yes", "y"]:
            score += 1

        children = input("Do you want to have kids?\n")

        if children in ["yes", "y"]:
            score += 3

        animals = input("Do you want to have a dog?\n")

        if animals in ["yes", "y"]:
            score += 3
        if score >= 25:
            print(f"Congratulations, {name}! You qualify to be {answer.capitalize()}'s husband!")
        else:
            print("Sorry, you don't qualify this time. But don't give up!")


    elif answer in ["hanna", "hann"]:

        older = input("Are you older than 22?\n")

        if older in ["yes", "y"]:
            score += 3

        tennis = input("Do you like tennis?\n")

        if tennis in ["yes", "y"]:
            score += 3

        time = input("Are you always on time?\n")

        if time in ["yes", "y"]:
            score += 3

        lemon_pie = input("Do you like lemon pies?\n")

        if lemon_pie in ["yes", "y"]:
            score += 3

        suits = input("Do you like wearing suits?\n")

        if suits in ["yes", "y"]:
            score += 3
        if score >= 15:
            print(f"Congratulations, {name}! You qualify to be {answer.capitalize()}'s husband!")
        else:
            print("Sorry, you don't qualify this time. But don't give up!")

    elif answer in ["vale", "v", "valeria"]:
        stable = input("Are you emotionally stable?\n")
        if stable in ["yes", "y"]:
            score += 3

            tall = input("Are you taller than Valeria?\n")
            if tall in ["yes", "y"]:
                score += 3

            self_esteem = int(input("From 1 to 10, how would you rate your self-esteem?\n"))
            if 1 <= self_esteem <= 10:
                score += self_esteem
            else:
                print("Please enter a number between 1 and 10.")
                return

            workout = input("Do you deadlift more than 90 kilos?\n")
            if workout in ["yes", "y"]:
                score += 3

            travel = int(input("From 1 to 10, how much do you like to travel?\n"))
            if 1 <= travel <= 10:
                score += travel
            else:
                print("Please enter a number between 1 and 10.")
                return
            adventure = input("Are you willing to try new experiences and get out of your comfort zone?\n")

            if adventure in ["yes", "y"]:
                score += 1
            communication = int(input("From 1 to 10, how well do you communicate your needs and feelings?\n"))
            if 1 <= communication <= 10:
                score += communication
            else:
                print("Please enter a number between 1 and 10.")
                return
            relationship = input("Do you see yourself in a long-term relationship?\n")

            if relationship in ["yes", "y"]:
                score += 1

            children = input("Do you want to have kids?\n")

            if children in ["yes", "y"]:
                score += 3

            cats = input("Do you LOVE cats?\n")

            if cats in ["yes", "y"]:
                score += 1

            if score >= 29:
                print(f"Congratulations, {name}! You qualify to be {answer.capitalize()}'s husband!")
            else:
                print("Sorry, you don't qualify this time. But don't give up!")

    else:
        print("Invalid input. Please choose Oli, Nati, Hanna, or Vale.")
        return


    print("Thank you for your response. Your total score is:", score)

    return score


def start_again():
    restart = input("Would you like to restart? Type 'start' to begin again, or any other key to exit.\n").lower()
    if restart == "start":
        test_husband_requirements()


test_husband_requirements()
start_again()