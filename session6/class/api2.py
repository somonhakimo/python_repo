
import requests
import pprint


url = "https://backend.akumotechnology.com/api/users/me"
cookie = {'access_token_cookie': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoYXNvbW9uOTVAZ21haWwuY29tIiwiZXhwIjoxNzUwMTI2Njc2fQ.g4JQlgZ9Zu7UeLpiKEzMJnVCnPnGOR9yTlkQ0eYvtwI'}
about_me = requests.get(url, cookies=cookie)

pprint.pprint((about_me.json()))






