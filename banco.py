import sqlite3

# Função para conectar ao banco de dados e consultar os contatos
def consultar_contatos():
    # Conectar ao banco de dados (altere o caminho do arquivo se necessário)
    conn = sqlite3.connect('database.db')  # Altere o caminho para o seu banco
    cursor = conn.cursor()

    # Consulta SQL
    cursor.execute("SELECT * FROM contatos")  # Aqui você pode personalizar a consulta

    # Recuperar todos os registros
    contatos = cursor.fetchall()

    # Fechar a conexão
    conn.close()

    return contatos

# Exemplo de uso da função
if __name__ == "__main__":
    contatos = consultar_contatos()
    for contato in contatos:
        print(contato)  # Exibir os dados recuperados
