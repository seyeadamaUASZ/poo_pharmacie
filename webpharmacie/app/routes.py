import os
from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
from flask_login import current_user, login_required
from .models import Category, Client, Medicament, Vente

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates', static_folder='static')


@main_bp.route('/', defaults={'path': 'index.html'})
@main_bp.route('/<path>')
@login_required
def index(path):
    content = None
    try:

        # try to match the pages defined in -> pages/<input file>
        return render_template('layouts/default.html',
                               content=render_template('pages/'+path, current_user=current_user))
    except:

        return render_template('layouts/auth-default.html',
                               content=render_template('pages/404.html'))


# Render the profile page
@main_bp.route('/profile.html')
@login_required
def profile():

    return render_template('layouts/default.html',
                           content=render_template('pages/profile.html'))


@main_bp.route('/harvested_canabis.html')
@login_required
def medicaments():
    medicament_list = Medicament.query.all()
    category_list = Category.query.all()
    return render_template(
        'layouts/default.html',
        content=render_template(
            'pages/harvested_canabis.html',
            allMedicaments=medicament_list,
            allCategory=category_list,
            current_user=current_user,
            checkCategorie=checkCategorie
        )
    )


@main_bp.route('/insert', methods=['POST'])
@login_required
def insert():
    if request.method == 'POST':
        name = request.form['name']
        prixu = request.form['prixu']
        quantite = request.form['quantite']
        designation = request.form['designation']
        category_id = request.form['category_id']

        medicament = Medicament(
            name, prixu, designation, quantite, category_id)
        Medicament.save(medicament)
        flash('Médicament ajouté avec succés')
        return redirect(url_for('main_bp.medicaments'))

    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/harvested_canabis.html'))


@main_bp.route('/packaged_canabis.html')
@login_required
def categories():
    category_list = Category.query.all()
    return render_template(
        'layouts/default.html',
        content=render_template(
            'pages/packaged_canabis.html',
            allCategory=category_list,
            current_user=current_user
        )
    )


@main_bp.route('/insertcategory', methods=['POST'])
@login_required
def insertcategory():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        category = Category(name, description)
        Category.save(category)
        flash('categorie ajouté avec succés')
        return redirect(url_for('main_bp.categories'))

    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/packaged_canabis.html'))


@main_bp.route('/clients.html')
@login_required
def clients():
    client_list = Client.query.all()
    return render_template(
        'layouts/default.html',
        content=render_template(
            'pages/clients.html',
            clients=client_list,
            current_user=current_user
        )
    )


@main_bp.route('/ventes.html')
@login_required
def ventes():
    vente_list = Vente.query.all()
    #liste des medicaments
    medicament_liste=Medicament.query.all()
    client_liste = Client.query.all()
    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/ventes.html',
                               ventes=vente_list,
                               current_user=current_user,
                               medicament_liste=medicament_liste,
                               client_liste=client_liste,
                               checkMedoc=checkMedoc,
                               checkClient=checkClient,
                               checkCategorie=checkCategorie
                               
                           ))


@main_bp.route('/insertclient',methods=['POST'])
@login_required
def insertclient():
    if request.method=='POST':
        lastname=request.form['lastname']
        firstname=request.form['firstname']
        adresse=request.form['adresse']
        telephone = request.form['telephone']
        numsecurite=request.form['numsecurite']
        
        client = Client(lastname,firstname,telephone,adresse,numsecurite)
        Client.save(client)
        flash('client ajouté avec succés')
        return redirect(url_for('main_bp.clients'))

    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/clients.html'))


#les deletings et modify

@main_bp.route('/deleteclient/<client_id>',methods=['POST','GET'])
@login_required
def delete_client(client_id):
    if current_user.is_admin ==False:
        return render_template('layouts/auth-default.html',
                               content=render_template('pages/403.html'))
    client = Client.query.get(client_id)
    if request.method=='POST':
        Client.delete(client)
        flash('Client supprimé avec succés')
        return redirect(url_for('main_bp.clients'))
    
    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/delete_client.html',
                               client=client,
                               client_id = client.id
                           ))    
        

@main_bp.route('/deletecategory/<category_id>',methods=['POST','GET'])
@login_required
def delete_category(category_id):
    if current_user.is_admin ==False:
        return render_template('layouts/auth-default.html',
                               content=render_template('pages/403.html'))
    category = Category.query.get(category_id)
    if request.method=='POST':
        Category.delete(category)
        flash('Catégorie supprimée avec succés')
        return redirect(url_for('main_bp.categories'))
    
    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/delete_category.html',
                               category=category,
                               category_id = category.id
                           ))
    
@main_bp.route('/deletemedicament/<medicament_id>',methods=['POST','GET'])
@login_required
def delete_medicament(medicament_id):
    if current_user.is_admin == False:
        return render_template('layouts/auth-default.html',
                               content=render_template('pages/403.html'))
    medicament = Medicament.query.get(medicament_id)
    if request.method=='POST':
        Medicament.delete(medicament)
        flash('Médicament supprimé avec succés!!!')
        return redirect(url_for('main_bp.medicaments'))
    
    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/delete_medicament.html',
                               medicament=medicament,
                               medicament_id=medicament.id
                           ))
    
    
#donner la catégorie appartenant

def checkCategorie(id):
    category = Category.query.get(id)
    return category.name


#donner l'objet medicament et l'objet client 

def checkMedoc(id):
    return Medicament.query.get(id)

def checkClient(id):
    return Client.query.get(id)