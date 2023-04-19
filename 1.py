

def day_weather(day, month, temperature):
    if temperature > 0:
        print(f"Сегодня {day}.{month} . На улице {temperature} градусов")
    else:
        print(f"Сегодня {day}.{month} . На улице {temperature} градусов")
        print("Холодно, лучше остаться дома")
day_weather(1, 2, -2)
