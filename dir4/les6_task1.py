import time


class TrafficLight:
    colors = ['red', 'yellow', 'green']

    def running(self):
        print(TrafficLight.colors[0])
        time.sleep(7)
        print(TrafficLight.colors[1])
        time.sleep(2)
        print(TrafficLight.colors[2])
        time.sleep(3)


n = TrafficLight()
n.running()
