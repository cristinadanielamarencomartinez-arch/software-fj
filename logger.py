class Logger:

    def __init__(self):
        self.logs = []

    def info(self, mensaje):
        log = "[INFO] " + mensaje
        self.logs.append(log)
        print(log)

        with open("logs.txt", "a") as archivo:
            archivo.write(log + "\n")

    def error(self, mensaje):
        log = "[ERROR] " + mensaje
        self.logs.append(log)
        print(log)

        with open("logs.txt", "a") as archivo:
            archivo.write(log + "\n")