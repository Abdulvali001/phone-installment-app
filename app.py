if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(email='abdulvali6091@gmail.com').first():
            admin = User(
                name='Abdulvali',
                email='abdulvali6091@gmail.com',
                password=generate_password_hash('admin123'),
                role=ROLE_ADMIN
            )
            db.session.add(admin)
            db.session.commit()

    app.run(debug=True)
