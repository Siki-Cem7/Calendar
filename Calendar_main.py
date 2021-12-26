import API_Connection
import Set_Event


class Main():


    def __init__(self):

        self.API = API_Connection.API()
        self.Event = Set_Event.Event()


        self.Event.Send_event()



if __name__ == "__main__":

    main = Main()
