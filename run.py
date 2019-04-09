#!/usr/bin/env python3.6
import pyperclip
from user import User
from credentials import Credential
def create_user(fname,lname,password):
	'''
    Function to create a new user account
    '''
	new_user = User(fname,lname,password)
	return new_user
def save_user(user):
	'''
    Function to save a new user account
    '''
	User.save_user(user)


def verify_user(password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = User.check_user(password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(user_name, site_name, password):
	'''
	Function to create a new credential
	'''
	new_credential = Credential(user_name, site_name, password)
	return new_credential

def save_credential(credential):
	'''/home/pricilla
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def display_credentials():
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials()


def copy_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(site_name)

def main():
	print(' ')
	print('Hello! Welcome to Password Locker.')
	while True:
		print(' ')
		print("*"*10)
		print('Use these codes to navigate: 1: ca-Create an Account 2: li-Log In 3: ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()

		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print("*"*10)
			print(' ')
			print('To create a new account:')
			first_name = input('Enter your first name - ').strip()
			last_name = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(first_name,last_name,password))
			print(' ')
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')
		elif short_code == 'li':
			print("*"*10)
			print(' ')
			print('To login, enter your account details:')
			user_name = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))

			if verify_user(password):
				print(' ')
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				print("*"*10)
				print('Navigation codes: 1: cc-Create a Credential 2: dc-Display Credentials 3: copy-Copy Password 4: ex-Exit')
				short_code = input('Enter a choice: ').lower().strip()
				print("*"*10)
				if short_code == 'ex':

					print(' ')
					print(f'Bye{user_name}')
					break

				elif short_code == 'cc':
					print('Enter your credential details:')
					site_name = input('Enter the site\'s name- ').strip()
					print(' ')
					print("*"*10)
					print('Please choose an option for entering a password: 1: ep-enter existing password 2: gp-generate a password 3: ex-exit')
					psw_choice = input('Enter an option: ').lower().strip()
					print("*"*10)
					if psw_choice == 'ep':
						print(' ')
						password = input('Enter your password: ').strip()
					elif psw_choice == 'gp':
						password = generate_password()
					elif psw_choice == 'ex':
						break
					else:
						print('Oops! Wrong option entered. Try again.')
					save_credential(create_credential(user_name, site_name, password))
					print(' ')
					print(f'Credential Created: User Name: {user_name} - Site Name: {site_name} - Password: {password}')
					print(' ')

				elif short_code == 'dc':
					print(' ')
					if display_credentials():
						print('Here is a list of all your credentials')
						print(' ')
						for credential in display_credentials():
							print(f'User Name: {credential.user_name} - Site Name: {credential.site_name} - Password: {credential.password}')
							print(' ')
					else:
						print(' ')
						print("You don't seem to have any credentials saved yet")
						print(' ')
				elif short_code == 'copy':
					print(' ')
					chosen_site = input('Enter the site name for the credential password to copy: ')
					copy_credential(chosen_site)
					print('')


				else:
					print(' ')
					print('Oops! Wrong details entered. Try again or Create an Account.')

			else:
				print("*"*10)
				print(' ')
				print('Oops! Wrong option entered. Try again.')


if __name__ == '__main__':
	main()
