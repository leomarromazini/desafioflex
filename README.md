# Para utilizar o projeto

Acesse o frontend da aplicação (em construção) ou crei sua propria aplicação com as rotas do backend

## link para a aplicação front

### https://certificate-manager-xi.vercel.app/


## Rotas backend



### ROTA GET
#### https://desafio-flex-back-end.herokuapp.com/certificate/

###ROTA POST
#### https://desafio-flex-back-end.herokuapp.com/certificate/
Exemplo de envio:
{
 	"name": "leomar",
	"username": "user_leomar",
  	"description": "certificado de conclusão de curso",
  	"groups": [1, 15],
	"expiration": 20
}

### ROTA DELETE
#### https://desafio-flex-back-end.herokuapp.com/certificate/{id}


### ROTA PATCH
#### https://desafio-flex-back-end.herokuapp.com/certificate/{id}
Campos aceitos:

"name"
"description"
"groups"
"expiration": 20


