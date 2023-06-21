import csv 
users  = [{"username": "sarahjones", "password": "mysecretpassword", "email": "sarahjones@example.com"},
          {"username": "tomsmith", "password": "password123", "email": "tomsmith@example.com"},
          {"username": "janedoe", "password": "mypassword", "email": "janedoe@example.com"},
          {"username": "johndoe", "password": "secretpassword", "email": "johndoe@example.com"}]

keys = ['username', 'password', 'email']
with open('empty.csv','w') as f:  ## crete file empty.csv if not exists in the same directory or it can crete automatically
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
    