class RemoteException(Exception):
    '''
    服务器错误
    '''
    def __init__(self):
        err = 'Server Error'
        Exception.__init__(self, err)



class LoginException(Exception):
    '''
    Custom exception types
    '''
    def __init__(self):
        err = 'Login Error'
        Exception.__init__(self, err)
