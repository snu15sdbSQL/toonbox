#-*- coding:utf-8 -*-

from application import app

from flask import Flask, redirect, url_for, render_template

@app.route('/')
def main():
   return render_template('main.html')
