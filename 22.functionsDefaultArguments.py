def location(country="India"):
    print(country)
    
location()          # If argument is not passed, the default argument will print
location("America") # In case if a argument is passed explicitly, then it would be
                    # given a higher precidence against the default one's
