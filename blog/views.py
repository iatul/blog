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
from blog.utility.functions import valid_payload

blogs = Service(name='blogs', path='/blogs', description='Blog Api')
blogs_comments = Service(name='comments', path='/blogs/{bid}/comments',
                         description='Blog Comment Api')





@blogs.post(validators=valid_payload)
def create_blog(request):
    """Create Blog."""

    params = request.matchdict
    print params
    return {'create': 'blog'}


@blogs.get()
def read_blogs(request):
    """Returns Hello in JSON."""

    params = request.matchdict
    if 'id' in params:
        # read_blog
        return {'read': 'blog'}
    else:
        # read_blogs use offset
        return {'read': 'blogs'}


@blogs_comments.get()
def read_comments(request):
    params = request

    # check bid
    return {'read': 'comments'}


@blogs_comments.post(validators=valid_payload)
def create_comment(request):
    params = request
    return {'create': 'comments'}


			