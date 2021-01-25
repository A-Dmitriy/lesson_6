from time import sleep

class TrafficLightAuto:
    __color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        i = 0
        while i < 3:
            print(f"Сфетофор: {TrafficLightAuto.__color[i]}")
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(9)
            i += 1


TrafficLightAuto = TrafficLightAuto()
TrafficLightAuto.running()
