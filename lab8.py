from flask import Blueprint,  render_template, request, redirect, jsonify, session, current_app
from os import path
import sqlite3
import psycopg2
from psycopg2.extras import RealDictCursor
import datetime

lab8 = Blueprint('lab8',__name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/lab8.html')