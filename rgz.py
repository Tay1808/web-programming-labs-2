from flask import Blueprint, render_template, request, redirect, session
rgz = Blueprint('rgz',__name__)

@rgz.route('/rgz/')
def main():
    return render_template('rgz/menurgz.html')
