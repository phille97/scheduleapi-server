# -*- coding: utf-8 -*-

from flask import (
    Blueprint, render_template, abort, flash, session, request,
    redirect, url_for
)
from flask.ext.login import login_required, current_user
from jinja2 import TemplateNotFound

from ..database.models import Apikey
from ..forms.useractions import UserSettings as UserSettingsForm
from ..controllers.database import get_session
from ..controllers.users import generate_apikey, fetch_apikeys, remove_apikey


bp = Blueprint('generic', __name__)


@bp.route('/')
def serve_frontpage():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@bp.route('/about')
def serve_aboutpage():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)


@bp.route('/ping')
def serve_pong():
    return "PONG", 200


@bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings_yo():
    form = UserSettingsForm(request.form)
    if request.method == 'POST' and form.validate():
        if save_settings(form):
            pass
    try:
        return render_template('forms/settings.html', form=form)
    except TemplateNotFound:
        abort(404)


@bp.route('/settings/apikeys', methods=['GET'])
@login_required
def get_apikeys():
    try:
        return render_template('forms/apikeys.html', apikeys=fetch_apikeys(user=current_user))
    except TemplateNotFound:
        abort(404)


@bp.route('/settings/apikeys/new', methods=['GET'])
@login_required
def new_apikey():
    api_key = generate_apikey(user=current_user)
    return redirect(url_for('generic.get_apikeys'))


@bp.route('/settings/apikeys/<id>/delete', methods=['GET'])
@bp.route('/settings/apikeys/<id>', methods=['DELETE'])
@login_required
def del_apikey(id):
    session = get_session()
    apikey = session.query(Apikey).filter(
        Apikey.user_id == current_user.id).filter(Apikey.id == id).first()
    if remove_apikey(apikey):
        flash("API key was removed")
    else:
        flash("API key could not be removed")

    return redirect(url_for('generic.get_apikeys'))
