
weather: dict = {'time': '12:00',
                 'weather': {'morning': 'rain',
                             'evening': 'more rain'}}


users: dict = {1: 'Bob', 2: 'Luigi'}
print(users)
del users[2]
users[1] = 'James'
print(users)
users.pop(2)
print(users)

print(weather['time'])
print(weather['weather']['morning'])
print(weather['weather']['evening'])
