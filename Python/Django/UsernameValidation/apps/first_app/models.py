from django.db import models

#UserManager
class UserManager(models.Manager):
    def register(self, postData):
        #check if email exists in database and catch DoesNotExist error if it doesnt
        try:
            preExist = self.get(email = postData)
        except self.model.DoesNotExist:
            preExist = False

        #if entry exists, preExist will not be false, return error, else continue validations
        if preExist is False:
            #check whether length of email is at least 8 characters
            if(len(postData) >= 8):
                #ensure it is fewer than 16
                if(len(postData) < 50):
                    self.create(email = postData)
                    return True
                else:
                    return {'error': 'Greater than 16'}
            else:
                return {'error': 'Less than 8'}
        else:
            return {'error': 'Already in DB!'}

class Users(models.Model):
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
