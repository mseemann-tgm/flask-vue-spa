##Report
### Rest Schnittstelle
##### Definieren Sie einen Test-Endpunkt auf localhost mit der Port Nummer 8080. Was müssen Sie dafür beim Flask-Server konfigurieren
- Im Flask Server in der app.py muss der Funktionsaufruf app.run mit Parametern aufgerufen werden. app.run(port=8080)

##### Implementieren Sie eine Todo-Liste mit Flask mit folgenden Elementen: {id, todo, assignee, done}. Was haben Sie geändert oder welche Elemente haben Sie neu definiert?
- In der app.py ein neues directory erstellen dieses heißt TODO danach id, todo, assignee, done hinzufügen. 
Es muss die @app.route angepasst werden und alle Attribute in der Methode.
Mit ``all_todos`` können Todos hinzugefügt werden. Mit ``single_todo`` können todos mit der id ausgelesen werden. Mit ``remove_todo`` können Todos entfernt werden.

##### Bereiten Sie die grafische Oberfläche für eine einfache Erstellung, Anzeige, Löschung und Anpassung der TODOs vor. Welche Komponenten müssen dafür erstellt werden?
- Es muss eine TODO.vue Komponente erstellt werden. In dieser muss eine Liste mit allen notwendigen Methoden erstellt werden.
Außerdem muss in der index.js Datei root importiert werden und als Route hinzugefügt werden 
``    path: '/',
      name: 'Todo',
      component: Todo,
      ``

##### Ermöglichen Sie die einfache Erweiterung der grafischen Oberfläche und beschreiben Sie notwendige Schritte um neue Komponenten zur Anmeldung oder persönlichen Definition von personenbezogenen TODOs zu ermöglichen.

##### Wie würden Sie eine einfache Authentifizierung implementieren? Beschreiben Sie die notwendigen Schritte!

#### Python Client

##### Implementieren Sie einen Client in Python, der sich mit der vorhandenen Server-Einheit verbindet und die Daten in eine eigene JSON Struktur lädt.


##### Was würden Sie bei der Server-API anders definieren, damit verschiedene Clients auf die angebotenenen Funktionen zugreifen könnten?
- Hierfür muss Cors verwendet werden. Cors wird wie folgt in der App.py aktiviert ``# enable CORS CORS(app)`` 
CORS ermöglicht es die Sicherheitseinschränkungen der SOP in definierten Fällen zu umgehen, was Clients Cross-Origin-Requests ermöglicht

#### Testing

##### Welche Tools würden Sie einsetzen, und wie würden die entsprechenden Konfigurationsdateien aussehen? Erstellen Sie ein Konzept!
- Ich würde Tox, Cypress, Pytest und TravisCi zum ausführen verwenden.

- Durch Tox können die Pytests Lokal ausgeführt werden
- Durch TravisCi können die Pytests automatisch bei jedem Push ausgeführt werden
- Durch Cypress kann die graphische Oberfläche getestet werden
 
- Cypress
 wird installiert mit ``npm install cypress``
 kann mit tox ausgeführt werden --> tox.ini 
 
 ``[tox] envlist = py36, cypress-dashboard, cypress-explore, eslint``
 
- Pytest
 Pytests müssen in einer Test Klasse geschrieben werden
 Danach in der tox.ini folgende hinzufügen, dasss sie ausgeführt werden können
 ``[pytest]
 testpaths = testing/pytest
 python_files = test_'.py
 python_classes = Test``
 
- Anschließend kann dies auf TravisCi gepusht werden wo das Projekt cloud-basiert integriert werden.
##### Bereiten Sie einen einfachen Test für den Aufruf der Random Funktion vor. Wie würden Sie diesen starten?

##### Implementieren Sie einen einfachen grafischen Test. Worauf achten Sie dabei?

##### Definieren Sie eine Konfiguration mit TravisCI für eine kontinuierliche Integration. Was müssen Sie dabei für die Python Tests und was für die grafischen Tests vorsehen?
Es muss ein travis.yml File erstellt werden.
- mit folgendem Inhalt für die pytests
 
 ``- stage: Tox Test name: "Unit Tests" language: python python: - 3.6 install: pip install tox-travis script: tox``
 
- und folgendem Inhalt für Cypress:
 
 ``- stage: Cypress Test name: "End to End testing Cypress" language: node_js node_js: - 10 cache: npm: true directories: - ~/.npm - ~/.cache - node_modules node_js: - '8' install: - cd src/router - npm ci script: - npm run cy:run``

##### Welche Tests würden Sie für die Grenzen der Random Funktion vorsehen?
Die Grenzen der Random Funktion können mit pytests welche von tox oder travis ausgeführt werden getestet werden.
So kann die Obergrenze und Untergrenze einfach überprüft werden.
