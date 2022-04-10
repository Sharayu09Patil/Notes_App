#import_blprnt,temps,req,jsonfy
#importfrom_flask


from flask import Blueprint, render_template, request, flash, jsonify

#importlogin
#.,
#importfrom_flsklogin

from flask_login import login_required, current_user
#modls_note

from .models import Note
#.
#databse

from . import db

#jsn_imprt

import json
#nam_bluprnt

views = Blueprint('views', __name__)
#route_gt_pst

@views.route('/', methods=['GET', 'POST'])

#requird_logn
#.
#home
#main


@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
#nte_lngth
  
    if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
#temp_retrn

    return render_template("home.html", user=current_user)

#rout_view

#deletion_note_prgm


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    
    #if_stmt_delete
    
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
#return
    return jsonify({})
#.
