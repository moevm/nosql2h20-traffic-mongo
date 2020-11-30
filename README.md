# nosql2h20-traffic-mongo

## Docker deploy

**Перед запуском проверьте, что у вас свободны порты: 80, 5000, 27017**

```bash
bash build.sh
```

> go to http://localhost

## Local deploy

### backend

Перейти в директорию `backend`

```bash
python3 -m venv venv 
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

Перейти в директорию `frontend`

### frontend

```bash
npm i
npm start
```

> React должен сам открыть окно браузера


### Demo reading/writing to mongodb
![Demo](https://github.com/moevm/nosql2h20-traffic-mongo/blob/master/docs/media/demo.gif?raw=true)

