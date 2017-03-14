import transaction
from sqlalchemy import desc
from sqlalchemy.orm import aliased
from sqlalchemy import exc
from blog.models.basemodel import (Session, blog, comment)
from blog.utility.functions import (generate_random_string, process_result)


def create_blog(blog_info):
    # create session object
    session = Session()

    blog_info['id'] =  generate_random_string(15)
    b1 = blog(**blog_info) 
    session.add(b1)
    session.flush()
    #session.refresh(b1)
    if b1.id == blog_info['id']:  # id created
        return {'status' : 201, 'msg' : 'Blog created successfully', 'bid' : b1.id}
    else:
        return {'status' : 500, 'msg' : 'Blog couldn\' t be created'}
     

def read_blogs(offset = 0):
    # create session object
    session = Session() 

    # alias
    b = aliased(blog)

    #todo replace 5 by config.limit
    result = session.query(b).order_by(desc(b.dateCreated)).slice(offset, offset + 5).all() # slice for limit and offset 
    if result:
        #list of dictionaries
        result = process_result(result)
        return {'status' : 200, 'msg' : 'Blogs fetched successfully', 'data': result}
    else:
        return {'status' : 404, 'msg' : 'No Blogs found'}


def read_blog(id = 0):
    # create session object
    session = Session() 

    # alias
    b = aliased(blog)

    result = session.query(b).filter(b.id == id).order_by(desc(b.dateCreated)).first() # slice for limit and offset 

    if result:
        #list of dictionaries
        return {'status' : 200, 'msg' : 'Blog fetched successfully', 'data': result}
    else:
        return {'status' : 404, 'msg' : 'Blog doesn\'t exist'}


def create_comment(comment_info):
    # create session object
    session = Session()

    c1 = comment(**comment_info) 
    session.add(c1)
    try:
        session.flush()
    except exc.IntegrityError:
        return {'status' : 404, 'msg' : 'Incorrect Blog Id'}
    #session.refresh(c1)    
    if c1.id:
        return {'status' : 201, 'msg' : 'Comment created successfully', 'cid' : c1.id}
    else:
        return {'status' : 500, 'msg' : 'Comment couldn\' t be created'}


def read_comments(bid):
    # create session object
    session = Session() 

    # alias
    c = aliased(comment)
    result = session.query(c).filter(c.bid == bid).order_by(desc(c.dateCreated)).all() # slice for limit and offset 
    if result:
        #list of dictionaries
        result = process_result(result)
        return {'status' : 200, 'msg' : 'Comments fetched successfully', 'data': result}
    else:
        return {'status' : 404, 'msg' : 'No Comments found'}
