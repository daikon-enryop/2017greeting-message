def greet(name):
    from datetime import datetime
    message = 'Hello, ' + name + '-san!'
    from datetime import datetime
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'
    print(message)


greet('Inoue')
