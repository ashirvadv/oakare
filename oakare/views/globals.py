from oakare.model import get_db

class User:

	def __init__(self):
		'''Construct user object.'''
		self.username = None
		self.first_name = None
		self.last_name = None
		self.email = None
		self.password = None
		self.date_of_birth = None
		self.family_links = []

	def set_username(self, _username):
		'''Set username.'''
		self.username = _username

	def set_first_name(self, _name):
		'''Set first name.'''
		self.first_name = _name

	def set_last_name(self, _name):
		'''Set last name.'''
		self.last_name = _name

	def set_email(self, _email):
		'''Set email.'''
		self.email = _email

	def set_password(self, _password):
		'''Set password.'''
		self.password = _password

	def set_date_of_birth(self, _dob):
		'''Set date of birth.'''
		self.date_of_birth = _dob

	def add_family_member(self, member):
		'''Add family member.'''
		self.family_links.append(member)

	def set_family_members(self, members):
		'''Set family members.'''
		for member in members:
			self.add_family_member(member)

	def initialize_user(self, _username, _first, _last, _email, _password, _dob, _members):
		'''Initialize user.'''
		self.set_username(_username)
		self.set_first_name(_first)
		self.set_last_name(_last)
		self.set_email(_email)
		self.set_password(_password)
		self.set_date_of_birth(_dob)
		self.set_family_members(_members)



def get_logo_path():
	'''Get logo path.'''
	return '/static/images/logo.jpg'

def get_all_table(table_name):
	"""Get all data from table table_name."""
	database = get_db()
	cursor = database.execute('SELECT * FROM ' + table_name)
	return cursor.fetchall()

def get_user(username):
	"""Get post with postid from posts table."""
	database = get_db()
	cursor = database.execute('SELECT * FROM users WHERE username = ?', (username, ))
	return cursor.fetchone()

def get_general_row(username):
	'''Get general row.'''
	database = get_db()
	cursor = database.execute('SELECT * FROM general WHERE user = ?', (username, ))
	return cursor.fetchone()

def add_user(user):
	'''Add user of user class to database.'''
	return