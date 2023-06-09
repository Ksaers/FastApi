### FastApi 
Clone this repo:
```
git clone https://github.com/Ksaers/FastApi.git
```
Create new environment:

```
virtualenv --python=python3.9 venv
```

Activate environment:

```
. venv/bin/activate
```

Install backend package:

```
pip install -e .
```

Copy or create config file `.env`:

```
cp .env.example .env
```
Transition to the launch of the project:

```
cd app
```
Run project:

```
uvicorn main:app --reload
```

Run tests:

```
export IS_TEST=True && pytest tests
```

Go to application

```
http://127.0.0.1:8000/docs
```
