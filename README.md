# IMGRED

## Instalation
```

Criar o arquivo ENV com as seguintes variáveis de ambiente.

DB_HOST
DB_NAME
DB_USER
DB_PASS
SECRET_KEY
THROTTLE_ANON
THROTTLE_USER
ALLOWED_HOSTS
MAIN_APP_URL

Depois executar o comando.

Para ambiente local 
docker-compose build

Para ambiente de produção
docker-compose -f docker-compose-deploy.yml build
```

## Run

```
Rodar o servidor Localmente
docker-compose up

Rodar o servidor de Produção
docker-compose -f docker-compose-deploy.yml up
```


## Configurar e rodar a fila de execução.

python manage.py shell

from django_q.models import Schedule

Schedule.objects.create(
    func='app.tasks.start_schedule',  
    minutes=1, 
    repeats=-1  
)


Para rodar a fila
```
docker-compose -f docker-compose.yml run --rm app sh -c "python manage.py qcluster"

```

### Post api/images-to-resize/

Porta 8100
```Request post para redimencionar imagens.

Post Multipart Form
{
	"user_id_from_request": 1,
	"image_to_resize": "123456",
	"image_id_from_request": 1,
}
// RESPONSE STATUS -> HTTP 201
```