from __future__ import print_function

import os

import httplib2
import oauth2client
from apiclient import discovery
from oauth2client import client
from oauth2client import tools

import get_flag

import argparse
flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()


class Donors:
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Google Sheets API Python Quickstart'
    SPREADSHEET_ID = '1rzXA07j23NHxE8wHgSy7ugLetHKLhBJN_jH3za0zLmA'
    RANGE = 'Test!A2:E'

    def get_donors(self):
        credentials = self._get_credentials()
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)
        result = service.spreadsheets().values().get(
            spreadsheetId=self.SPREADSHEET_ID, range=self.RANGE).execute()
        values = result.get('values', [])

        retArray = []
        flag_manager = get_flag.Flag()
        if not values:
            print('No data found.')
        else:
            for row in values:
                add_row = {"name": row[0], "country": row[2], "amount": row[3],
                           "flag": flag_manager.get_flag(row[2])}
                retArray.append(add_row)

        return retArray

    def _get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'sheets.googleapis.com-python-quickstart.json')

        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run_flow(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials
