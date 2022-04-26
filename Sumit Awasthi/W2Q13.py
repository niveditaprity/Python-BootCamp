city=input("Enter any city (Delhi, Agra, Jaipur, Lucknow, Kanpur) : ")
city=city.lower()
if city=="delhi":
    print("Monument: Red Fort")
elif city=="agra":
    print("Monument: Taj Mahal")
elif city=="jaipur":
    print("Monument: Jal Mahal")
elif city=="lucknow":
    print("Monument: Bara Imambara") 
elif city=="kanpur":
    print("Monument: Jagannath Temple")     
else:
    print("You entered another city from the list")
