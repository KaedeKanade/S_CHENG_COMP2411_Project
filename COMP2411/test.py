from account import AccountManagementSystem

if __name__ == "__main__":
    system = AccountManagementSystem()
    
    # Create accounts
    account1 = system.create_account('user1@example.com', 'password1', 'user1', 'basic')
    account2 = system.create_account('user2@example.com', 'password2', 'user2', 'premium')
    
    # Read an account
    print(system.read_account(account1.user_id))
    
    # List all accounts
    print(system.list_accounts())
    
    # Delete an account
    system.delete_account(account1.user_id)
    
    # List all accounts after deletion
    print(system.list_accounts())