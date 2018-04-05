# -*- coding: utf-8 -*

import json
mongo = local_import('MongoModule')
constants = local_import('ConstantsModule')


# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------



# ---- example index page ----
def index():
    # los valores que van en el json deben ser parametrizados y validados (lenght, tipo, etc)
    # ademas el pwd debe hacercele un hash para que no este almacenado como plain text en la BD
    # les recomiendo este link: http://web2py.com/books/default/chapter/36/09/control-de-acceso
    try:
        data = mongo.DataManager()
        json = {"name":"airam","last_name":"aguero","pwd":"123456789",
                "role":"user","school":"computacion",
                "email":"july@gmail.com","document_id":"V-85963204"}

        #calling database module
        result = data.createAccount(json)

        if result:
            return dict(message=T(result))
        else:
            return dict(message=T())

    except Exception as e:
        return dict(message=T())

      

'''
# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
'''