import API_Connection
from Google import Create_Service, convert_to_RFC_datetime


class Event():


    def __init__(self):

        self.API = API_Connection.API()
        self.New_Event()





    def New_Event(self):


        self.summary = "First Event"
        self.location_street_nbr = "Unterfeldstrasse 4"
        self.location_city = "Alberswil"
        self.location_nummber = "6248"
        self.description = "My first event over the API"

        self.start_time_year = "2021"
        self.start_time_month = "12"
        self.start_time_day = "26"
        self.start_time_time = ""
        self.start_time_zone = "(GMT+01:00)Mitteleuropäische Zeit-Zürich"

        self.end_time_year = "2021"
        self.end_time_month = "12"
        self.end_time_day = "26"
        self.end_time_time = ""
        self.end_time_zone = "(GMT+01:00)Mitteleuropäische Zeit-Zürich"

        self.recurrance = "RRULE:FREQ=DAILY;COUNT=2"
        self.mail1 = "sommer.silvan3@gmail.com"
        self.mail2 = "siki.cemmii@gmail.com"
        self.reminders_method = "popup"
        self.reminders_method2 = "popup"
        self.reminders_min_hrs = "minutes"
        self.reminders_time = ""


        self.event = {
            'summary': self.summary,
            'location': f"{self.location_street_nbr} {self.location_nummber} {self.location_city}",
            'description': self.description,
            'start': {
            'dateTime': convert_to_RFC_datetime(2021, 12, 27, 13, 00),
            'timeZone': f'{self.start_time_zone}',
            },
            'end': {
            'dateTime': convert_to_RFC_datetime(2021, 12, 27, 17, 00),
            'timeZone': f'{self.end_time_zone}',
            },
            'recurrence': [
            #f'{self.recurrance}'
            ],
            'attendees': [
            {'email': f'{self.mail1}'},
            #{'email': f'{self.mail2}'},
            ],
            'reminders': {
            'useDefault': False,
            'overrides': [
            #{'method': f'{self.reminders_method}', f'{self.reminders_min_hrs}': 24 * 60},
            #{'method': f'{self.reminders_method2}', f'{self.reminders_min_hrs}': 10},
            ],
            },
        }



    def Send_event(self):

        self.API.Make_Service()

        self.event = self.API.service.events().insert(
            calendarId="vpgdt0edloadplu2ui99f4dqcg@group.calendar.google.com",
            body=self.event
        ).execute()













