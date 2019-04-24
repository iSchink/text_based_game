# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

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

# def story(): #von seifert
#     story_nr = request.args(0)
#     aktuelle_story = db.Story[story_nr]
#
#     if request.method == 'POST':   #  wenn der user eine antwort schickt
#         antwort = request.post_vars['antwort']  # dann ist die variable antwort das, was im HTML formular namens "antwort" steht
#         if antwort == aktuelle_story.Antwort1:  #  wenn die varble antwort gleich der antwort 1 in der datenbank ist
#             response.redirect(URL('story', args=[aktuelle_story.konsequenz1]))  #  soll die konsequenz 1 zutreffen
#         elif antwort == aktuelle_story.antwort2:
#             response.redirect(URL('story', args=[aktuelle_story.konsequenz2]))
#         else:
#             # TODO
#             #  wenn der user unsinn tippt
#             pass
#     else:
#         return dict(quest_text=aktuelle_story.Textteil)
def story():
    story_nr = request.args(0) # Die Id des Quests kommt aus der URL
                                # /default/mein_quest/42 für Quest 42
    aktuelle_story = db.Story[story_nr] # Hole Daten mit id==42 aus der Tabelle
    if request.method == 'POST':
            antwort = request.post_vars['antwort'] # Formulardaten holen
            if antwort == aktuelle_story.Antwort1:
            # Zum Quest "konsequenz1" umleiten
                redirect(URL('story', args=[aktuelle_story.Konsequenz1]))
            elif antwort == aktuelle_story.Antwort2:
            # Zum Quest "konsequenz2" umleiten
                redirect(URL('story', args=[aktuelle_story.Konsequenz2]))
            else:
            # Wehin jetzt? Wieder zum selben Quest.
                redirect(URL('story', args=[aktuelle_story]))
                # Den Quest-Text darstellen

    return dict(quest_text=aktuelle_story.Textteil)



