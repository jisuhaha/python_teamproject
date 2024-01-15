from flask import Blueprint

from flask import Blueprint, render_template, abort

board_page = Blueprint('board_page', __name__, url_prefix='/board')

@board_page.route('/')
def main():
    return render_template('board_main.html')