from city_file import cities_dict
import turtle
import pandas


screen = turtle.Screen()
screen.setup(1600, 800)
image = "turkiye_map.gif"
screen.addshape(image)
turtle.shape(image)

# to get coordinates in cities.csv
''' 
def get_mouse_click_coor(x, y):
     cities_dict["x"].append(int(x))
     cities_dict["y"].append(int(y))      
turtle.onscreenclick(get_mouse_click_coor) '''

df_city_dict = pandas.DataFrame(cities_dict)
df_city_dict.to_csv("cities.csv")
data = pandas.read_csv("cities.csv")

city_array = data["city"]
guessed_cities = []



score = 0
while len(guessed_cities) <= 81:

    text = turtle.Screen()
    title = f"Write the City? {score}/81"
    answer_city = text.textinput(title=title, prompt="Type Another City You Know in Türkiye?").title()
    answer_line = data[data["city"] == answer_city]

    if not answer_line.empty and answer_city not in guessed_cities:
        guessed_cities.append(answer_city)
        coordinate = (int(answer_line["x"]), int(answer_line["y"]))
        city_to_write = turtle.Turtle()
        city_to_write.hideturtle()
        city_to_write.penup()
        city_to_write.goto(coordinate)
        city_to_write.write(answer_line["city"].item(), align="center", font=("Arial", 12, "normal"))
        score += 1

    if answer_city == "Exit":
        remainder_city = []
        for element in city_array:
            if element not in guessed_cities:
                remainder_city.append(element)

        fill_the_city = turtle.Turtle()
        fill_the_city.hideturtle()
        fill_the_city.penup()
        fill_the_city.speed("fastest")

        for city in remainder_city:
            temp_line = data[data["city"] == city]
            fill_the_city.goto(int(temp_line["x"]), int(temp_line["y"]))
            fill_the_city.write(temp_line["city"].item(), align="center", font=("Arial", 12, "normal"))
        break

turtle.mainloop()

