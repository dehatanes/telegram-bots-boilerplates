# Boilerplates para Bots do Telegram
Arsenal de boilerplates diversos para criar seus chatbots/bots no telegram usando Flask.

## Sobre
A ideia aqui é disponibilizar boilerplates com pedaços de código para ajudar a criar um bot
no telegram usando Flask e Python 3.8 sem que você precise se preocupar com a parte repetitiva
e foque apenas em criar um processamento legal para o seu bot :star:

PS: Os boilerplates não estão adaptados para desenvolvimento local, foram criados com a intenção
de irem direto para um servidor (como o [PythonAnywhere](https://www.pythonanywhere.com/)).


## Códigos disponíveis
> Obs: quando eu falar `token do telegram` aqui nas docs eu quero dizer o token fornecido
> pelo [botfather](https://t.me/botfather) no momento de criação do bot no telegram.

|arquivo | descrição|
| - | - |
| [minimal\_endpoint.py](minimal_endpoint.py) | Arquivo com um endpoint para webhook que apenas pega o corpo da mensagem enviada pelo telegram e gera um log de que ela chegou. Não reponde o usuário nem realiza outras ações.|
| [send\_text\_resp\_bot.py](send_text_resp_bot.py) | Arquivo com um endpoint para webhook que pega o corpo da mensagem enviada pelo telegram e a usa para enviar uma mensagem em resposta ao usuário. Essa mensagem utiliza a própria mensagem do usuário e seu nome para montar a resposta. **Lembre de alterar o valor do token do telegram no arquivo**. |
| [crush\_percentage\_bot.py](crush_percentage_bot.py) | Exemplo criado a partir do arquivo anterior. Ao receber uma mensagem, calcula uma porcentagem e a retorna com um texto customizado de resposta. **Lembre de alterar o valor do token do telegram no arquivo**. |
| [send\_custom\_audio\_bot.py](send_custom_audio_bot.py) | Arquivo com um endpoint que pega o texto recebido de mensagem e o converte em áudio (narrado estilo google tradutor) para enviá-lo para a pessoa. **Lembre de alterar o valor do token do telegram no arquivo**. Esse código necessita que libs externas sejam instaladas. |

