from datetime import datetime
	
class mpesa:
	datetime.now()



	"""
	this is my billion dollar idea
	attributes				functions
							transfer money
	phone_number			buy airtime
	name					pay bill
	id_number				withdraw
	age						deposit
	balance					check balance
							get loan
							pay loan

	"""
	def __init__(self,phone_number,first_name,last_name):	
		self.phone_number=phone_number
		self.first_name=first_name
		self.last_name=last_name
		self.balance=0
		self.deposits =[]
		self.withdraws =[]

	def show_balance(self):
		return self.balance
		

	def deposit(self,amount):
		self.balance+= amount
		d=datetime.now().strftime("%c")
		message="Dear {} {}, you have deposited {} at {}. Your new mpesa balance is {}".format(self.first_name,self.last_name,amount,d,self.balance)
		description ={"date": d, "amount":amount}
		self.deposits.append(description)
		return message

	def ministatement(self):
		for deposit in self.deposits:
			print("on{}, you deposited {}".format(deposit["date"],deposit["amount"]))
		for withdraw in self.withdraws:
			print("on{}, you withdrew {}".format(withdraw["date"],withdraw["amount"]))
		return

		



	def withdraw(self):
		amount = int(input("Please enter the withdrawal amount"))

		if self.balance<=amount:
			return "Dear michelle murithi,you have insufficient amount to withdraw from yor balance."
		else:
			self.balance-= amount
			d=datetime.now().strftime("%c")
			message="Dear {} {}, you have withdrawn {} at {}. Your new mpesa balance is {}".format(self.first_name, self.last_name,amount,d,self.balance)
			description ={"date":d, "amount":amount}
			self.withdraws.append(description)	
			return message

		
		

	



