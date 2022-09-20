'''
register username password
	If registration was successful, return "Registered successfully"
 	If user already exists, return "Username already exists"
login username password
	If the login was successful, return "Logged in successfully"
 	If login unsuccessful, return "Login unsuccessful"
logout username
	If the logout was successful, return "Logged out successfully"
 	If the given username wasn't logged in, return "Logout unsuccessful"  

'''

'''
store username: password in dict
register checks dict

store logged in users in a set
log in: check against dict
	if successful, add username to set
 
log out: check logged in set
	if found, return successful
 	if not found, return unsuccessful

'''

class AmazonDummySite:
	def __init__(self):
		self.creds = {}
		self.loggedIn = set()

	def register(self, username, password):
		if username in self.creds:
			return 'Username already exists'
		else:
			self.creds[username] = password
			return 'Registered successfully'

	def login(self, username, password):
		if username in self.loggedIn or \
			username not in self.creds or \
			self.creds[username] != password:
			return 'Login unsuccessful'
		else:
			self.loggedIn.add(username)
			return 'Logged in successfully'

	def logout(self, username):
		if username in self.loggedIn:
			self.loggedIn.remove(username)
			return 'Logged out successfully'
		else:
			return 'Logout unsuccessful'

	def parseLog(self, log):
		#log is assumed to be a list
		res = []
		for i in log:
			req = i.split(' ')
			command = req[0]
			if command == 'register':
				res.append(self.register(req[1], req[2]))
			elif command == 'login':
				res.append(self.login(req[1], req[2]))
			elif command == 'logout':
				res.append(self.logout(req[1]))

		return res

log = ['register user05 qwerty', 'login user05 qwerty', 'logout user05']
log2 = ['logout user05', 'login user05 qwerty', 'register user05 qwerty', 'register user05 soafjsoa', 'login user05 qwerty', 'register user01 123', 'login user01 645', 'logout user01', 'logout user05', 'logout user05']
# ['logout unsuc', 'login unsuc', 'registered', 'user already exist', 'login successful', 'registered', 'login unsuccessful', 'logout unsuc', 'logout suc', 'logout unsuc']

dummySite = AmazonDummySite()
returns = dummySite.parseLog(log2)
print(returns)
