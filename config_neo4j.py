from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
user = "neo4j"
password = "password" 

driver = GraphDatabase.driver(uri, auth=(user, password))

def get_session():
    return driver.session()