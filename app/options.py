from flask import session, redirect, url_for


def is_logged():
    if session.get('logged') is None:
        return False