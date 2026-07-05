from database.database import get_connection
import mysql.connector


# Create User (Register)
def create_user(name, email, password):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO users (name, email, password)
            VALUES (%s, %s, %s)
        """

        values = (name, email, password)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return {"message": "User created successfully"}

    except mysql.connector.Error as err:
        return {"error": str(err)}


# Login User
def login_user(email, password):
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT * FROM users
            WHERE email = %s AND password = %s
        """

        values = (email, password)

        cursor.execute(query, values)
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:
            name = user.get('name', '')
            # Make fazil admin (case-insensitive check)
            role = 'admin' if 'fazil' in name.lower() else 'user'
            return {"message": "Login successful", "name": name, "role": role}
        else:
            return {"message": "Invalid email or password"}

    except mysql.connector.Error as err:
        return {"error": str(err)}