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
    for group in user.groups.all():
        if str(group) == 'technician':
            return True
    return False


def is_booking_manager_or_organizer(user):
    return is_organizer(user) or is_booking_manager(user)


def is_pr_man(user):
    for group in user.groups.all():
        if str(group) == 'pr_man':
            return True
    return False
