from django.urls import path
from channels.routing import URLRouter
from chat import Chatconsumer
#from .wsgi import *

ws_application=URLRouter[

    path("ws/channels/",Chatconsumer.as_asgi())

]
