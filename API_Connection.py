from Google import Create_Service
from pprint import pprint



class API():

    def __init__(self):

        self.API_key = "AIzaSyDp8w9qoxCQyLoKV2kSXKHlui4eNVvLyxM"
        self.Credentials = "115809173719742046559"

        self.CLIENT_SECRET_FILE = "client_secret.json"
        self.API_NAME = "calendar"
        self.API_VERSION = "v3"
        self.SCOPES = ["https://www.googleapis.com/auth/calendar"]
        self.service = None


    def Make_Service(self):

        self.service = Create_Service(self.CLIENT_SECRET_FILE, self.API_NAME, self.API_VERSION, self.SCOPES)






