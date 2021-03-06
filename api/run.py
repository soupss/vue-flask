"""
run.py
- creates an application instance and run the dev server
"""

if __name__ == '__main__':
    from app.app import create_app
    app = create_app()
    app.run()
