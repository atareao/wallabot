#!/usr/bin/env python3
import requests
import json

class WallabagApi():
    def __init__(self, base_uri, client_id, client_secret, username, password):
        self._base_uri = base_uri
        self._client_id = client_id
        self._client_secret = client_secret
        self._username = username
        self._password = password
        self._access_token = None
        self._refresh_token = None
        self.auth()

    def auth(self):
        data = {"grant_type": "password",
                "client_id": self._client_id,
                "client_secret": self._client_secret,
                "username": self._username,
                "password": self._password}
        url = self._base_uri + "/oauth/v2/token"
        response = requests.post(url, json=data)
        if response.status_code == 200:
            data = response.json()
            self._access_token = data["access_token"]
            self._refresh_token = data["refresh_token"]
        else:
            print(response.content)

    def post(self, entry_url):
        headers = {"Authorization": "Bearer {}".format(self._access_token)}
        data = {"url": entry_url}
        url = self._base_uri + '/api/entries.json'
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()
        return None
