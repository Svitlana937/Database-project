from neo4j import GraphDatabase

uri = "neo4j://127.0.0.1:7687"
user = "neo4j"
password = "password!"

driver = GraphDatabase.driver(uri, auth=(user, password))

def get_session():
    return driver.session()