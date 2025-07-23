import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth
import base64
import datetime
from rest_framework.exceptions import APIException

class DarajaAPI:
    def __init__(self):
        self.consumer_key = settings.DARAJA_CONSUMER_KEY
        self.consumer_secret = settings.DARAJA_CONSUMER_SECRET
        self.business_shortcode = settings.DARAJA_SHORTCODE
        self.passkey = settings.DARAJA_PASSKEY
        self.base_url = "https://sandbox.safaricom.co.ke"
        self.callback_url = settings.DARAJA_CALLBACK_URL

def get_access_token(self):
    url = f"{self.base_url}/oauth/v1/generate?grant_type=client_credentials"
    try:
        response = requests.get(url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
        # Check if the response status is successful
        if response.status_code == 200:
            try:
                return response.json()['access_token']  # This return is correctly inside the function
            except (ValueError, KeyError) as e:
                raise APIException(f"Failed to parse access token: {str(e)}. Response: {response.text}")
        else:
            raise APIException(
                f"Failed to get access token. Status: {response.status_code}, Response: {response.text}"
            )
    except requests.RequestException as e:
        raise APIException(f"Error connecting to Daraja API: {str(e)}")
    

    def stk_push(self, phone_number, amount, account_reference, transaction_desc):
        access_token = self.get_access_token()
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        password = base64.b64encode(f"{self.business_shortcode}{self.passkey}{timestamp}".encode()).decode()

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "BusinessShortCode": self.business_shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": int(amount),  
            "PartyA": phone_number,
            "PartyB": self.business_shortcode,
            "PhoneNumber": phone_number,
            "CallBackURL": self.callback_url,
            "AccountReference": account_reference,
            "TransactionDesc": transaction_desc,
        }
        url = f"{self.base_url}/mpesa/stkpush/v1/processrequest"
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
    