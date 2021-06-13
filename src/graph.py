from matplotlib import pyplot


class Graph:
    def __init__(self):
        self.temps = []

        for i in range(10):
            self.temps.append(0)

    def add(self, temp):
        self.temps.append(temp)
        del self.temps[-1]

    def show_graph(self):
        pyplot.ion()

        times = []

        for i in range(10):
            times.append(-9 + i)

        pyplot.clf()
        pyplot.scatter(times, self.temps)
        pyplot.plot(times, self.temps)

        pyplot.show()

    def hide_graph(self):
        pyplot.ioff()
