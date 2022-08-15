from django.contrib.auth.models import User
from random import randrange
from django.contrib.auth import authenticate

def CreateUser(**kargs) :
    username, email,password,passsowrd_con = kargs['username'], kargs['email'], kargs['password1'] ,kargs['password2']
    errors = []

    if password != passsowrd_con :
        errors.append("Two Password field didn't match")
    
    try : 
        User.objects.get(username=username)
        user_key = []
        for i in range(9):user_key.append(randrange(0,9))
        username = f'{username}'+ "".join(map(str,user_key))
    except User.DoesNotExist as erorr:
        pass

    if errors:
        msg = {
            'create':False,
            'errors':"".join(errors)
        }
    else :
        u = User.objects.create(
            username=username,
            email=email,
        )
        u.set_password(password)
        u.save()
        msg = {
            'create':True,
            'username':username
        }
    return msg 



def LoginForm (**info) :
    email, passsword = info['email'], info['password']
    errors = []

    try : 
        u = User.objects.get(email=email)
        auth = authenticate(username=u.username,password=passsword)
        if auth != None :
            msg = {
                'login':True,
                'user':auth
            }
        else :
            msg = {
                'login':False,
                'error':'wrong email or password !'
            }

    except User.DoesNotExist as error:
        errors.append("this email doesn't exist on the system")
        msg = {
            'login':False,
            'error':''.join(errors)
        }

    return msg



