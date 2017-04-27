from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from social_django.models import UserSocialAuth
from twython import Twython, TwythonAuthError, TwythonError
from rest_framework.response import Response
from TwitterAPI import TwitterAPI

from splittweets.settings import SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET, SOCIAL_TWITTER_ACCESS_TOKEN, \
    SOCIAL_TWITTER_ACCESS_TOKEN_SECRET




@csrf_exempt
def tweeted(request):
    if request.method == 'GET':
        x = request.GET
        mainstr = x['textareamain']
        api = TwitterAPI(SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET, SOCIAL_TWITTER_ACCESS_TOKEN,SOCIAL_TWITTER_ACCESS_TOKEN_SECRET)
        if len(mainstr) >560 :
            # print mainstr[0:140]
            # print mainstr[140:280]
            # print mainstr[280:420]
            # print mainstr[420:560]
            r = api.request('statuses/update', {'status': mainstr[0:140]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[140:280]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[280:420]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[420:560]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[560:]})
            print(r.status_code)
            # mainstr.replace(mainstr[:140],'')
            # return HttpResponse('hello post')

        elif len(mainstr) > 420 :
            r = api.request('statuses/update', {'status': mainstr[0:140]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[140:280]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[280:420]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[420:560]})
            print(r.status_code)            # mainstr.replace(, '')
            # return HttpResponse('hello post')

        elif len(mainstr) > 280 :
            r = api.request('statuses/update', {'status': mainstr[0:140]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[140:280]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[280:420]})
            print(r.status_code)
        # mainstr.replace(, '')
            # return HttpResponse('hello post')

        elif len(mainstr) > 140:
            r = api.request('statuses/update', {'status': mainstr[0:140]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[140:280]})
            print(r.status_code)


        else:
            r = api.request('statuses/update', {'status': mainstr[0:140]})
            print(r.status_code)



            # mainstr.replace(, '')
            # return HttpResponse('hello post')

        # return HttpResponse('Hello done')



    if request.method == 'POST':
        x = request.POST
        print(x['textareamain'])
        mainstr = x['textareamain']
        api = TwitterAPI(SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET, SOCIAL_TWITTER_ACCESS_TOKEN,
                         SOCIAL_TWITTER_ACCESS_TOKEN_SECRET)

        if len(mainstr) >560 :
            # print mainstr[0:140]
            # print mainstr[140:280]
            # print mainstr[280:420]
            # print mainstr[420:560]
            r = api.request('statuses/update', {'status': mainstr[0:140]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[140:280]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[280:420]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[420:560]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[560:]})
            print(r.status_code)
            # mainstr.replace(mainstr[:140],'')
            # return HttpResponse('hello post')

        elif len(mainstr) > 420 :
            r = api.request('statuses/update', {'status': mainstr[0:140]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[140:280]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[280:420]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[420:560]})
            print(r.status_code)            # mainstr.replace(, '')
            # return HttpResponse('hello post')

        elif len(mainstr) > 280 :
            r = api.request('statuses/update', {'status': mainstr[0:140]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[140:280]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[280:420]})
            print(r.status_code)
        # mainstr.replace(, '')
            # return HttpResponse('hello post')

        elif len(mainstr) > 140:
            r = api.request('statuses/update', {'status': mainstr[0:140]})
            print(r.status_code)
            r = api.request('statuses/update', {'status': mainstr[140:280]})
            print(r.status_code)
            # mainstr.replace(, '')
            # return HttpResponse('hello post')

        else:
            r = api.request('statuses/update', {'status': mainstr[0:140]})
            print(r.status_code)

    return HttpResponse('All done, move to previous page to tweet again')


# @login_required
def home(request):
    return render(request, 'core/home.html')


