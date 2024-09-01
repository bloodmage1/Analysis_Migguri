from flask import Flask, Blueprint, render_template, request, make_response, jsonify, redirect, url_for
from blog_control.user_mgmt import User
from flask_login import login_user, current_user, logout_user
import datetime
from app_insta import app

import os

blog_abtest = Blueprint('blog',__name__)


@blog_abtest.route('/set_email', methods = ['GET', 'POST']) # 라우팅 경로와 함수명을 같게 하는 게 편함
def set_email():
    if request.method =='GET':
        print('set_email', request.headers)
        print('set_email', request.args.get('user_email'))
        return redirect(url_for('blog.test_blog'))
    else:
        # print('set_email', request.headers)
        # print('set_email',request.form['user_email'])
        user = User.create(request.form['user_email'], 'A')
        login_user(user, remember=True, duration=datetime.timedelta(days=365)) # 1년동안 이메일정보 기억

        return redirect(url_for('blog.test_blog'))

@blog_abtest.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('blog.test_blog'))

@blog_abtest.route('/test_blog')
def test_blog():
    tr_baby_list = os.listdir(os.path.join(app.static_folder, 'img/tr_baby'))
    tr_mid_list = os.listdir(os.path.join(app.static_folder, 'img/tr_mid'))
    tr_mom_list = os.listdir(os.path.join(app.static_folder, 'img/tr_mom'))

    anal_baby_list1 = os.listdir(os.path.join(app.static_folder, 'img/anal_baby'))
    anal_baby_list2 = os.listdir(os.path.join(app.static_folder, 'img/anal_baby2'))
    anal_baby_list3 = os.listdir(os.path.join(app.static_folder, 'img/anal_baby3'))

    anal_mid_list1 = os.listdir(os.path.join(app.static_folder, 'img/anal_mid'))
    anal_mid_list2 = os.listdir(os.path.join(app.static_folder, 'img/anal_mid2'))
    anal_mid_list3 = os.listdir(os.path.join(app.static_folder, 'img/anal_mid3'))

    anal_mom_list1 = os.listdir(os.path.join(app.static_folder, 'img/anal_adult'))
    anal_mom_list2 = os.listdir(os.path.join(app.static_folder, 'img/anal_adult2'))
    anal_mom_list3 = os.listdir(os.path.join(app.static_folder, 'img/anal_adult3'))


    if current_user.is_authenticated:
        return render_template('blog_B.html', 
                               user_email=current_user.user_email,
                               tr_baby_list = tr_baby_list[:8],
                               tr_mid_list = tr_mid_list[:8],
                               tr_mom_list = tr_mom_list[:8],

                               anal_baby_list1 = anal_baby_list1[:8],
                               anal_baby_list2 = anal_baby_list2[:8],
                               anal_baby_list3 = anal_baby_list3[:2],
                               
                               anal_mid_list1 = anal_mid_list1[:8],
                               anal_mid_list2 = anal_mid_list2[:8],
                               anal_mid_list3 = anal_mid_list3[:2],
                               
                               anal_mom_list1 = anal_mom_list1[:8],
                               anal_mom_list2 = anal_mom_list2[:8],
                               anal_mom_list3 = anal_mom_list3[:2])
    else:
        return render_template('blog_A.html',
                               tr_baby_list = tr_baby_list[:8],
                               tr_mid_list = tr_mid_list[:8],
                               tr_mom_list = tr_mom_list[:8])
    
