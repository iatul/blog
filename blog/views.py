#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Cornice services.
"""

import json
import logging
import colander
from cornice import Service
from pyramid.response import Response
from blog.app import app
from blog.utility.exceptions import BlogException
from blog.utility.functions import sanitize_payload

blogs = Service(name='blogs', path='/blogs', description='Blog Api')
blogs_comments = Service(name='comments', path='/blogs/{bid}/comments',
                         description='Blog Comment Api')
logger = logging.getLogger(__name__)

@blogs.post()
def create_blog(request):
    """Create Blog."""
    data = sanitize_payload(request,'blog')
    return app.create_blog(data)


@blogs.get()
def read_blogs(request):
    """Returns Hello in JSON."""
    #logger.info(request)
    params = request.GET
    if 'id' in params:
        # read_blog
        return app.read_blog(params['id'])
    else:
        return app.read_blogs(params.get('offset',0))


@blogs_comments.get()
def read_comments(request):
    bid = str(request.matchdict['bid'])
    if bid:
        return app.read_comments(bid)
    else:
        return {'status':400, 'msg':'Blog id is missing'}


@blogs_comments.post()
def create_comment(request):
    bid = str(request.matchdict['bid'])
    data = sanitize_payload(request, 'comment')
    if bid:
        data['bid'] = bid
        return app.create_comment(data)
    else:
        return {'status':400, 'msg':'Blog id is missing'}
    
