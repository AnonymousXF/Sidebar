def alert_success(message):
    return '<div class="alert alert-success alert-dismissible fade show" role="alert">' \
            '<strong>{message}</strong>' \
            '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' \
            '<span aria-hidden="true">&times;</span>' \
            '</button>' \
            '</div>'.format(message=message)

def alert_warning(message):
    return '<div class="alert alert-warning alert-dismissible fade show" role="alert">' \
           '<strong>{message}</strong>' \
           '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' \
           '<span aria-hidden="true">&times;</span>' \
           '</button>' \
           '</div>'.format(message=message)

def aler_danger(message):
    return '<div class="alert alert-danger alert-dismissible fade show" role="alert">' \
           '<strong>{message}</strong>' \
           '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' \
           '<span aria-hidden="true">&times;</span>' \
           '</button>' \
           '</div>'.format(message=message)
