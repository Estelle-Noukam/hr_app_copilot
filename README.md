# HR Management Application

Application web de gestion des ressources humaines développée avec **Flask**, **PostgreSQL**, **SQLAlchemy** et une interface HTML/Jinja.

Elle permet de gérer :
- les départements
- les employés
- les congés
- les absences
- les documents
- (module Évaluations optionnel)


## 🚀 Fonctionnalités

### ✔️ Gestion des départements
- Créer, modifier, supprimer un département
- Lister tous les départements

### ✔️ Gestion des employés
- Ajouter un employé
- Modifier un employé
- Supprimer un employé
- Voir la liste des employés

### ✔️ Gestion des congés
- Créer une demande de congé
- Modifier / supprimer une demande
- Lister les congés

### ✔️ Gestion des absences
- Ajouter une absence
- Modifier / supprimer une absence
- Lister les absences

### ✔️ Gestion des documents
- Ajouter un document (métadonnées)
- Modifier / supprimer
- Lister les documents


## 🗂️ Structure du projet

hr_app/
│
├── app.py             
├── models.py             
├── models_user.py      
├── forms.py           
│
├── routes/             
│   ├── employees.py
│   ├── departments.py
│   ├── leaves.py
│   ├── absences.py
│   ├── documents.py
│   └── (reviews.py)      
│
├── templates/            
│   ├── layout.html
│   ├── index.html
│   ├── employees/
│   ├── departments/
│   ├── leaves/
│   ├── absences/
│   └── documents/
│
├── static/             
│   └── style.css
│
├── requirements.txt      
└── docker-compose.yml   

Code


## 🛠️ Installation

### 1. Cloner le projet

```bash
git clone https://github.com/Estelle-Noukam/hr_app.git
cd hr_app
2. Créer un environnement virtuel
bash
python3 -m venv venv
source venv/bin/activate
3. Installer les dépendances
bash
pip install -r requirements.txt
🗄️ Configuration PostgreSQL
Créer la base et l’utilisateur :

sql
CREATE DATABASE hr_db;
CREATE USER hr_user WITH PASSWORD 'ton_mot_de_passe';
GRANT ALL PRIVILEGES ON DATABASE hr_db TO hr_user;
Configurer pg_hba.conf :

Code
host    hr_db   hr_user   127.0.0.1/32   scram-sha-256
host    hr_db   hr_user   ::1/128        scram-sha-256
Redémarrer PostgreSQL :

bash
sudo systemctl restart postgresql
🔌 Configuration Flask
Dans app.py :

python
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg://hr_user:motdepasse@localhost:5433/hr_db"
Créer les tables :

bash
flask shell
python
from hr_app import db
db.create_all()
▶️ Lancer l’application
bash
flask run --host=0.0.0.0 --port=5000
Accéder à l’interface :

Code
http://127.0.0.1:5000
🔐 Création d’un compte administrateur
bash
flask shell
python
from models_user import User
from hr_app import db

u = User(username="admin", role="admin")
u.set_password("test1234")
db.session.add(u)
db.session.commit()
