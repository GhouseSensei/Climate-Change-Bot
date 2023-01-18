import telebot
import time
import weatherr
import airQ
import co2emiss

bot = telebot.TeleBot("YOUR BOT API")

def extract_arg(arg):
    s=''
    for i in arg.split()[1:]:
        if(s!=""):
            s = s+" "+i
        else:
            s=s+i;
    return s

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "This bot can help you get weather report and AQI of cities.\nIt can also calculate the amount of co2 you emit by your daily habits.\n/help for more")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "/help - this message\n/weather_report <City name> - Gives weather details and AQI of given city\n/meat_emission <chicken/mutton/beef/pork> - Calculates amount of co2 emitted based on quatity you consumed\n/lpg_emission - Calculates amount of co2 emitted(approx) based on quatity you used\n/car_emission - Calculates the amount of co2 you emitted based on the distance you travelled\n/bike_emission - Calculates the amount of co2 you emitted based on the distance you travelled\n/flight_emission - Calculates amount of CO2 emitted per person traveling in a flight depending on departure and destination locations.\n\nNote: All the calculated values are approximate values, they may be close but not exact")

@bot.message_handler(commands = ['weather_report'])
def weather_report(message):
    txt = message.text
    mess = weather.climet(extract_arg(txt))
    if(len(mess) == 1):
        bot.reply_to(message, mess[0]);
    else:
        temp = mess[0]
        press = mess[1]
        humi = mess[2]
        desc = mess[3]
        spid = mess[4]
        bot.reply_to(message, f"Temperature in Celsius = {temp}\n\nPressure in hPa unit = {press}\n\nHumidity in % = {humi}\n\nWeather Description = {desc}\n\nWind speed in kmph = {spid}" )
        mess2 = airQ.aqii(extract_arg(txt))
        if(len(mess2)==0):
            bot.reply_to(message, "No AQI Station for given city")
        else:
            aqiii = mess2[0]
            mean = mess2[1]
            impli = mess2[2]
            bot.reply_to(message, f"AQI = {aqiii}\n\nIndex meaning = {mean}\n\nHealth Implications = {impli}")
@bot.message_handler(commands = ['meat_emission'])
def meat(message):
    txt = extract_arg(message.text)
    print(txt)
    txt = txt.lower()
    if txt == "chicken":
        msg = bot.reply_to(message, 'Enter the amount consumed(in grams)')
        bot.register_next_step_handler(msg, chicken)
    elif txt == "pork":
        msg = bot.reply_to(message, 'Enter the amount consumed(in grams)')
        bot.register_next_step_handler(msg, pork)
    elif txt == "mutton":
        msg = bot.reply_to(message, 'Enter the amount consumed(in grams)')
        bot.register_next_step_handler(msg, mutton)
    elif txt == "beef":
        msg = bot.reply_to(message, 'Enter the amount consumed(in grams)')
        bot.register_next_step_handler(msg, beef)
    else:
        bot.reply_to(message, "Syntax: /meat_emission <chicken/mutton/beef/pork>")
def chicken(message):
    x = co2emiss.chicken(message.text)
    bot.reply_to(message, f"The amount of CO2 emitted from your non vegetarian diet is {x[0]} Kg, whereas if it were veg, it would emit only around {x[1]} Kg to {x[2]} Kg")
def mutton(message):
    x = co2emiss.mutton(message.text)
    bot.reply_to(message, f"The amount of CO2 emitted from your non vegetarian diet is {x[0]} Kg, whereas if it were veg, it would emit only around {x[1]} Kg to {x[2]} Kg")
def beef(message):
    x = co2emiss.beef(message.text)
    bot.reply_to(message, f"The amount of CO2 emitted from your non vegetarian diet is {x[0]} Kg, whereas if it were veg, it would emit only around {x[1]} Kg to {x[2]} Kg")
def pork(message):
    x = co2emiss.pork(message.text)
    bot.reply_to(message, f"The amount of CO2 emitted from your non vegetarian diet is {x[0]} Kg, whereas if it were veg, it would emit only around {x[1]} Kg to {x[2]} Kg")

@bot.message_handler(commands = ['lpg_emission'])
def lpg(message):
    msg = bot.reply_to(message, "Enter the volume of LPG you used (in litres)")
    bot.register_next_step_handler(msg, lpgg)
def lpgg(message):
    x = co2emiss.lpg(message.text)
    bot.reply_to(message, f"The amount of CO2 emitted by your LPG usage is {x} Kg, which could have been neglected if you had used electric powered stove instead")

@bot.message_handler(commands=["car_emission"])
def car(message):
    msg = bot.reply_to(message, "Enter the fuel of your vehicle")
    bot.register_next_step_handler(msg, fuel)
def fuel(message):
    if(message.text.lower() == "petrol"):
        msg = bot.reply_to(message, "Enter the distance travelled in kilometers")
        bot.register_next_step_handler(msg, petrol)
    elif(message.text.lower() == "diesel"):
        msg = bot.reply_to(message, "Enter the distance travelled in kilometers")
        bot.register_next_step_handler(msg, diesel)
    else:
        bot.reply_to(message, "Not in my data")
def petrol(message):
    x = co2emiss.petrol(message.text)
    bot.reply_to(message, f"The amount of CO2 emitted by your car is {x} Kg, which could have been neglected if you had used electric vehicle or minimized if you had used publc transport")
def diesel(message):
    x = co2emiss.diesel(message.text)
    bot.reply_to(message, f"The amount of CO2 emitted by your car is {x} Kg, which could have been neglected if you had used electric vehicle or minimized if you had used publc transport")

@bot.message_handler(commands=["bike_emission"])
def bike(message):
    msg = bot.reply_to(message, "Enter the distance travelled in kilometers")
    bot.register_next_step_handler(msg, bikee)
def bikee(message):
    x = co2emiss.bike(message.text)
    bot.reply_to(message, f"The amount of CO2 emitted by your bike is {x} Kg, which could have been neglected if you had used electric vehicle or minimized if you had used publc transport")

@bot.message_handler(commands = ["flight_emission"])
def flight(message):
    msg = bot.reply_to(message, "Enter the Departure and Destination Cities in the format of City1, City2")
    bot.register_next_step_handler(msg, flite)
def flite(message):
    txt = message.text
    txt = txt.split(",")
    x = co2emiss.flight(txt[0], txt[1])
    if(len(x)!=1):
        bot.reply_to(message, f"The amount of CO2 emitted by your flight per passenger varies from {x[0]} to {x[1]} Kg")
    else:
        bot.reply_to(message, f"The amount of CO2 emitted by your flight per passenger is minimum of {x[0]} Kg")



while True:
    try:
        bot.polling()
    except:
        time.sleep(15)
