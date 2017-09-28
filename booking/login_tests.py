def is_organizer(user):
    for group in user.groups.all():
        if str(group) == 'organizer':
            return True
    return False



def is_booking_manager(user):
    for group in user.groups.all():
        if str(group) == 'booking_manager':
            return True
    return False

def is_artist_manager(user):
    for group in user.groups.all():
        if str(group) == 'artist_manager':
            return True
    return False

def is_booker(user):
    for group in user.groups.all():
        if str(group) == 'booker':
            return True
    return False


def is_technician(user):
    # Following commented lines are for reference as to what is possible
    # Note that print statements show up in terminal when page loads,
    # not on page or dev tools (in browser as javascript does)

    # print('Hallo from is_technician function in login_test.py')
    # print(user.groups)
    # print(user.is_authenticated())
    # print(user.is_staff)
    # print(user.groups.all())

    for group in user.groups.all():
        if str(group) == 'technician':
            # print('In group technician')
            return True

    # print('Not in group')
    return False
