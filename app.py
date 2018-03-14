from abc import ABCMeta, abstractmethod
from random import randint

class Account:
	@abstractmethod
	def createAccount():
		return 0

	@abstractmethod
	def authenticate():
		return 0

	@abstractmethod
	def withdraw():
		return 0

	@abstractmethod          
	def deposite():
		return 0

	@abstractmethod
	def displaybalance():
		return 0


class SavingAccount(Account):
	def __init__(self):
		self.savingAccounts = {"11111" : ["hemil",1]}
	def createAccount(self, name, initialDeposite):
		self.accountNumber = randint(10000,99999)
		self.savingAccounts[self.accountNumber] = [name, initialDeposite]
		print "Your account is successfully created, Your account number is {}".format(self.accountNumber)
	def authenticate(self, name, accountNumber):
		if accountNumber in self.savingAccounts.keys():
			if self.savingAccounts[accountNumber][0] == name:
				print "Authentication Successful!"
				self.accountNumber = accountNumber
			return True
		else:
			print "all keys >>>>>>>>>>>>>" + str(self.savingAccounts.keys())
			print "name you enter>>>>>>>>>" + name
			print "name in database>>>>>>>" + self.savingAccounts[accountNumber][0]
			print "Authentication failed"
			return False

	def withdraw(self, withdrawAmount):
		if withdrawAmount > self.savingAccounts[self.accountNumber][1]:
			print "Insufficient Balance"    
		else:
			self.savingAccounts[self.accountNumber][1] -= withdrawAmount
			print "Withdraw Successful" 
			self.displaybalance(self.accountNumber)

	def deposite(self, depositeAmount):
		self.savingAccounts[self.accountNumber][1] += depositeAmount
		print "deposite Successful" 
 		self.displaybalance(self.accountNumber)

	def displaybalance(self, accountNumber):
		print "Available balance: {}".format(self.savingAccounts[accountNumber][1])


savingAccount = SavingAccount()

while True:
	print "Enter 1 to open an acc"
	print "Enter 2 to acess existing account"
	print "Enter 3 to exit"
	userChoice = int(raw_input(""))
	if userChoice == 1:
		name = raw_input("Enter your name: ")
		initialDeposite = int(raw_input("Enter initialDeposite"))
		savingAccount.createAccount(name,initialDeposite)

	elif userChoice == 2:
		name = raw_input("Enter name: ")
		accountNumber = int(raw_input("Enter accountNumber: "))
		authenticateStatus = savingAccount.authenticate(name, accountNumber)
		if authenticateStatus is True:
			while True:
				print "enter 1 to withdraw"
				print "Enter 2 to deposite"
				print "Enter 3 to displaybalance"
				print "Enter 4 to exit"
				userChoice = int(raw_input(""))
				if userChoice == 1:
					withdrawAmount = int(raw_input("Enter withdrawAmount : "))
					savingAccount.withdraw(withdrawAmount)
				elif userChoice == 2:
					depositeAmount = int(raw_input("Enter depositeAmount : "))
					savingAccount.deposite(depositeAmount)
				elif userChoice == 3:
					savingAccount.displaybalance(accountNumber)
				elif userChoice == 4:
					break
		

	elif userChoice == 3:
		quit()