from flask import render_template

def user_main_service():
    return render_template('/user/main.html')

def user_login_service():
    return render_template('/user/login.html')

def user_join_service():
    return render_template('/user/join.html')

def user_profile_service():
    return render_template('/user/profile.html')
