#!/usr/bin/env python3

# Turn on debug mode
import os
import sys
import importlib
import cgitb
cgitb.enable()

import json
from werkzeug.wrappers import  Request,Response
from beaker.middleware import SessionMiddleware

pth = os.path.dirname(os.path.abspath(__file__))
if pth not in sys.path:
    sys.path.append(pth)
    sys.path.append(os.path.dirname(pth))

import config




def application(environ, start_response):

    session = environ['beaker.session']
    sessionid = session.__getattr__('id')

    request = Request(environ)
    
    
    # print(urllib.parse.parse_qsl(request.get_data()))


    if request.method == "POST" and request.content_type == 'application/x-www-form-urlencoded':
        request.POST = pd = request.form.to_dict()

    elif request.method == "POST" and request.content_type == 'application/json':
        if request.headers.get('authorization') == None:
            request.POST = pd = {'q':'Not Autorized', 'r': 'Abort'}
            
        else:
            if request.headers.get('authorization') == config.AUTH_KEY:
                rq = request.get_data()
                sd = json.loads(rq.decode('utf-8'))
                request.POST = pd = sd
            else:
                request.POST = pd = {'q':'Not Autorized', 'r': 'Abort'}
        
    else:
        request.POST = pd = request.args.to_dict()


    if 'f' in request.POST and 'm' in request.POST:
        if len(request.cookies.keys()) == 0:
            rd = 'Bad Request'

        elif len(request.cookies.keys()) > 0:

            if request.cookies['beaker.session.id'] != sessionid:
                rd = 'Bad Request'
            else:
                c = config.classpath
                f = request.POST['f']
                m = request.POST['m']
                modulepath = c + '.' + f
                # modulex = __import__(modulepath)
                # xclass = getattr(modulex, f)
                # xmethod = getattr(xclass, m)
                module = importlib.import_module(modulepath)
                my_class = getattr(module, f)
                my_method = getattr(my_class, m)
                rd = my_method(my_class(pd))
                
    elif 'q' in request.POST:
        rd = {'error':'Authorization Denied'}      
    else:
        rd = {'error':'Request was rejected. Server Error'} 
                

    status = '200 OK'
    contenttype=[
        ('Content-type','application/json')
    ]

    response = Response([json.dumps(rd).encode()],status)
    # response.headers ='Access-Control-Allow-Origin', 'http://localhost:4200')
    # 05160595228
    # 92139229522
    # start_response(status,contenttype)
    

    return response(environ,start_response)



session_opts ={
    'session.type': 'memory',
    'session.cookie_expires': True,
    'session.auto': True
}
application = SessionMiddleware(application,session_opts)