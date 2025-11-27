# Add a stop() method
# Add a new method in Engine called stop() and call it from the Car class.
# Expected Output:
# Car is running.
# Engine Started.
# Engine Stopped.

class Engine:
    def start(self):
        print("Engine Started.")
    
    def stop(self):
        print("Engine Stopped.")

class Car:
    def __init__(self):
        self.engine = Engine()

    def stop(self):
        print("Car is running.")
        self.engine.start()
        self.engine.stop()

E = Engine()
c = Car(E)
c.stop()

