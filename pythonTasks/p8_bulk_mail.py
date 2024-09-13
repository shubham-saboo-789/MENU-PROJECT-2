import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import p1_mail

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1mSykufAPtClIkTL-4WF7s0AHb9AbSASQUXwH6YfuOCE"


def main():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        # Call the Sheets API
        sheets = service.spreadsheets()

        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1!A1:B").execute()
        values = result.get("values", [])
        result_len = len(values)

        subject = "this is a bulk email testing by shubham saboo"
        body = "hopefully this test email reaches the correct email"
        for row in range(2, result_len+1):
            name_data = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!A{row}").execute().get("values")[0][0]
            email_data = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!B{row}").execute().get("values")[0][0]

            print(name_data, email_data, "sending...")
            try:
                p1_mail.mail_noinput(email_data, subject, body)
            except Exception as e:
                print(f"An error occurred while sending the email: {e}")

            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!C{row}",
                                   valueInputOption="USER_ENTERED", body={"values" : [["row"]]}).execute()
            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!D{row}",
                                   valueInputOption="USER_ENTERED", body={"values": [["Done"]]}).execute()

    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()
