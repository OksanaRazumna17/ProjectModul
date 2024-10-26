import mysql.connector

def get_statistics():
    # Соединение с базой данных
    connection = mysql.connector.connect(
        host='38.180.108.211',
        port=3306,
        user='freevet',
        password='Str0ngPassw@rd!',
        database='freevetDB'
    )

    cursor = connection.cursor()

    # SQL запрос для получения статистики
    query = """
    SELECT 
        (SELECT COUNT(*) FROM auth_user) AS total_users, 
        (SELECT COUNT(*) FROM questions_question) AS total_questions, 
        (SELECT COUNT(*) FROM vetbook_clinicvisit) AS total_clinic_visits;
    """
    cursor.execute(query)

    # Получение данных
    result = cursor.fetchone()

    # Закрытие соединения
    cursor.close()
    connection.close()

    # Возврат статистики
    return {
        "total_users": result[0],
        "total_questions": result[1],
        "total_clinic_visits": result[2]
    }
