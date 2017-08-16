from __future__ import unicode_literals
import re, bcrypt
from django.db import models
from datetime import datetime
from django.contrib import messages, sessions
# Create your models here.
class UserManager(models.Manager):
    def login(self, postData):
        error_msgs = []
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

        try:
            user = User.objects.get(email=postData['email'])
        except:
            error_msgs.append("Invalid user!")
            return {'errors':error_msgs}

        if not bcrypt.hashpw(postData['password'].encode(), user.password.encode()) == user.password.encode():
            error_msgs.append("Wrong Password!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            return {'theuser':user.name, 'username':user.username, 'userid':user.id, 'points':user.point}

    def register(self, postData):
        error_msgs = []
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        try:
            if User.objects.get(email=postData['email']):
                error_msgs.append("Email already in use!")
        except:
            pass

        if len(postData['name']) < 4:
            error_msgs.append("Name is too short!")

        if len(postData['username']) < 4:
            error_msgs.append("Username is too short!")

        if not email_regex.match(postData['email']):
            error_msgs.append("Invalid email!")

        if len(postData['password']) < 8:
            error_msgs.append("Password is too short!")

        if not postData['password'] == postData['confirm']:
            error_msgs.append("Passwords do not match!")

        if error_msgs:
            return {'errors':error_msgs}
        else:
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(email=postData['email'], name=postData['name'], username=postData['username'], password=hashed)
            return {'theuser':user.name, 'username':user.username, 'userid':user.id}

class User(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    point = models.IntegerField(default=0)
    donor = models.BooleanField(default=False)
    member = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class AlgoManager(models.Manager):
    def addAlgo(self, postData):
        error_msgs = []
        if len(postData['question']) < 1:
            error_msgs.append("You need to add the question")

        if len(postData['solution']) < 1:
            error_msgs.append("You need to add a solution!")

        if len(postData['points']) < 1:
            error_msgs.append("You need to add a point value!")

        if error_msgs:
            return {'errors':error_msgs}
        else:

            algo = Algo.objects.create(question=postData['question'], solution=postData['solution'], second_solution=postData['second_solution'], hint=postData['hint'], explanation=postData['explanation'], level=postData['level'], params=postData['params'], points=postData['points'])
            return {'algoid':algo.id}

# //////////////////////alpha logic///////////////
    # def checkAlgo(self, postData, id):
    #     error_msgs = []
    #     msg = []
    #     try:
    #         check = Algo.objects.get(id=postData['id'])
    #     except:
    #         error_msgs.append("Woops! Server Mismatch")
    #         return {'errors':error_msgs}

    #     userObj = User.objects.get(id=id)
    #     # UserAlgo.objects.filter(userJoin=userObj.id, algo_id=check.id).delete()
    #     try:
    #         algo = UserAlgo.objects.filter(userJoin=userObj.id,algo_id=check.id)
    #         try:
    #             if algo.exists():
    #                 userAttempt = UserAlgo.objects.get(userJoin=id,algo_id=check)
    #             if len(postData['solution']) < 1:
    #                 error_msgs.append("You must enter a value")
    #                 return {'errors':error_msgs}
    #             if not (postData['solution'] == check.solution):
    #                     error_msgs.append("Incorrect")
    #                     userAttempt.fails += 1
    #                     userAttempt.save()
    #                     return {'errors':error_msgs}

    #             if(postData['solution'] == check.solution):
    #                 print postData['solution'], '3333333333333333333333333'
    #                 print check.solution, '4444444444444444444444444'
    #                 print msg, "2222222222222222222"
    #                 userAlgo = UserAlgo.objects.get(id=userAttempt.id)
    #                 userAlgo.solved = True
    #                 userAlgo.save()
    #                 return {'messageCorrect':msg}
        #     except:
        #         return {'errors':["somthing went wrong"]}
        # except:
        #     print "hit the except"
        #     firstAttempt = UserAlgo.objects.create(userJoin=userObj,algo_id=check)
        #     return {'answer':check}

# //////////////////beta algo checker logic///////////////////////////////////////

    # def checkAlgo(self, postData, id):
    #     error_msgs = []
    #     msg = []
    #     try:
    #         check = Algo.objects.get(id=postData['id'])
    #     except:
    #         error_msgs.append("Woops! Server Mismatch")
    #         return {'errors':error_msgs}
    #     userObj = User.objects.get(id=id)
    #     #UserAlgo.objects.filter(userJoin=userObj.id, algo_id=check.id).delete()
    #     try:
    #         algo = UserAlgo.objects.filter(userJoin=userObj.id,algo_id=check.id)
    #         try:
    #             if algo.exists():
    #                 userAttempt = UserAlgo.objects.get(userJoin=id,algo_id=check)
    #             if userAttempt.solved == True:
    #                 if len(postData['solution']) < 1:
    #                     error_msgs.append("You must enter a value")
    #                     return {'errors':error_msgs}
    #                 if not (postData['solution'] == check.solution):
    #                         error_msgs.append("Incorrect")
    #                         return {'errors':error_msgs}
    #                 else:
    #                     return {'messageCorrect':msg}

    #             if userAttempt.solved == False:
    #                 if len(postData['solution']) < 1:
    #                     error_msgs.append("You must enter a value")
    #                     return {'errors':error_msgs}
    #                 if not (postData['solution'] == check.solution):
    #                         error_msgs.append("Incorrect")
    #                         userAttempt.fails += 1
    #                         userAttempt.save()
    #                         return {'errors':error_msgs}

    #                 if(postData['solution'] == check.solution):
    #                     userAlgo = UserAlgo.objects.get(id=userAttempt.id)
    #                     userAlgo.solved = True
    #                     userAlgo.save()
    #                     userObj.point += check.points
    #                     userObj.save()
    #                     return {'messageCorrect':msg}
    #         except:
    #             firstAttempt = UserAlgo.objects.create(userJoin=userObj,algo_id=check)
    #             return
    #     except:
    #         print "hit the except"
    #         return {'answer':check}

# //////////////////////beta 2.0 algo checker logic//////////////////

    def checkAlgo(self, postData, id, page):
        error_msgs = []
        msg = []
        try:
            check = Algo.objects.get(id=page)
        except:
            error_msgs.append("Woops! Server Mismatch")
            return {'errors':error_msgs}
        userObj = User.objects.get(id=id)
        #UserAlgo.objects.filter(userJoin=userObj.id, algo_id=check.id).delete()
        try:
            algo = UserAlgo.objects.filter(userJoin=userObj.id,algo_id=check.id)
            if not algo.exists():
                firstAttempt = UserAlgo.objects.create(userJoin=userObj,algo_id=check)
            try:
                if algo.exists():
                    userAttempt = UserAlgo.objects.get(userJoin=id,algo_id=check)
                if userAttempt.solved == True:
                    if len(postData['solution']) < 1:
                        error_msgs.append("You must enter a value")
                        return {'errors':error_msgs}
                    if not (postData['solution'] == check.solution):
                            error_msgs.append("Incorrect")
                            return {'errors':error_msgs}
                    else:
                        return {'messageCorrect':msg}

                if userAttempt.solved == False:
                    if len(postData['solution']) < 1:
                        error_msgs.append("You must enter a value")
                        return {'errors':error_msgs}
                    if not (postData['solution'] == check.solution):
                            error_msgs.append("Incorrect")
                            userAttempt.fails += 1
                            userAttempt.save()
                            return {'errors':error_msgs}

                    if(postData['solution'] == check.solution):
                        userAlgo = UserAlgo.objects.get(id=userAttempt.id)
                        userAlgo.solved = True
                        userAlgo.save()
                        userObj.point += check.points
                        userObj.save()
                        return {'messageCorrect':msg}
            except:
                return
        except:
            print "hit the except"
            return {'answer':check}

# ///////////////////algo validation if not logged in. //////////////

    def checkAlgo_nologin(self, postData, id):
        error_msgs = []
        msg = []
        check = Algo.objects.get(id=id)
        if len(postData['solution']) < 1:
            error_msgs.append("You must enter a value")
            return {'errors':error_msgs}
        if not (postData['solution'] == check.solution):
                error_msgs.append("Incorrect")
                return {'errors':error_msgs}

        if(postData['solution'] == check.solution):
            return {'messageCorrect':msg}

class Algo(models.Model):
    question = models.CharField(max_length=255)
    hint = models.TextField(max_length=500, null=True)
    solution = models.TextField(max_length=500, null=True)
    second_solution = models.TextField(max_length=500, null=True)
    explanation = models.TextField(max_length=500, null=True)
    params = models.CharField(max_length=255, null=True)
    level = models.IntegerField(default=10, null=True)
    points = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AlgoManager()

class UserAlgo(models.Model):
    userJoin = models.ForeignKey(User, related_name="userAlgos")
    algo_id = models.ForeignKey(Algo, related_name="algoAlgos")
    fails = models.IntegerField(default=0)
    solved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AlgoManager()
