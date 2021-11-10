class Bank

	=begin
		:type balance: Integer[]
	=end
		def initialize(balance)
			@balance = [0, *balance]
			@current = [0, *balance]
		end
	
	
	=begin
		:type account1: Integer
		:type account2: Integer
		:type money: Integer
		:rtype: Boolean
	=end
		def transfer(account1, account2, money)
			if account1 <= 0 or account1 >= @balance.length or account2 <= 0 or account2 >= @balance.length
				return false
			end
			
			if @current[account1] < money
				return false
			end
			@current[account1] -= money
			@current[account2] += money
			return true
			
		end
	
	
	=begin
		:type account: Integer
		:type money: Integer
		:rtype: Boolean
	=end
		def deposit(account, money)
			if account <= 0 or account >= @balance.length
				return false
			end
			@current[account] += money
			return true
		end
	
	
	=begin
		:type account: Integer
		:type money: Integer
		:rtype: Boolean
	=end
		def withdraw(account, money)
			if account <= 0 or account >= @balance.length
				return false
			end
			if @current[account] < money
				return false
			end
			@current[account] -= money
			return true
		end
	
	
	end
	
	# Your Bank object will be instantiated and called as such:
	# obj = Bank.new(balance)
	# param_1 = obj.transfer(account1, account2, money)
	# param_2 = obj.deposit(account, money)
	# param_3 = obj.withdraw(account, money)