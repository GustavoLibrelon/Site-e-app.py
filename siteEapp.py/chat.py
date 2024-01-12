#pip install flet no cmd
#Titulo do site conversus
#Botao para iniciar site 
    #Popup
        #Bem vindo ao conversus
        #Escreva seu nome
        #Entrar no site
#Chat
    #Gustavo entrou no chat
    #Mensagem do usuario
#Campo para enviar mensagem 
#Botao enviar
#aqui abaixo estou criando em formato de app
import flet as ft 

def main(pagina): #def= definindo uma funcao que se chama main.
    #para criar um texto no flat usar ft.Text
    titulo = ft.Text("Conversos")
     
    nome_usuario = ft.TextField(label="Escreva seu nome") #campo de texto que o usuario pode escrever
    
    chat= ft.Column()
    
    #criando um tunel de comunicaçao entre ususarios
    def enviar_mensagem_tunel(informacoes): 
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)



    def enviar_mensagem(evento):
        #o que eu quero que esse botao faça, pegue o texto do campo mensagem e adicione no chat
         #colocar nome do usuario na mensagem
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
       

        #enviar mensagem do campo ususario para o tunel e todos poderem ver a mensagem
        pagina.pubsub.send_all(texto_campo_mensagem)
        
        #limpar o campo mensagem
        campo_mensagem.value = ""
        pagina.update()#serve p atualizar a pagina pq fiz ediçoes

    campo_mensagem = ft.TextField(label = "Escreva sua mensagem aqui", on_submit=enviar_mensagem)

    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)


    def entrar_chat(evento):
        #o que eu quero que esse botao faça?
        #1 feche o popup
        popup.open = False
        #2 tire o botao "iniciar chat da tela"
        pagina.remove(botao_iniciar)
        # adicionar chat
        pagina.add(chat)
        #3 criar o campo de enviar mensagem 
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(linha_mensagem)
        #4botao de enviar msg
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()


    #criando popup, para criar popup usar AlertDialog
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Conversos"),#titulo
        content=nome_usuario,#conteudo
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]#açoes
        )
    

    #abri o popup
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    

    #para criar um botao ft.ElevatedButton
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    

    #para mostrar coisas na pagina adicionar aqui abaixo
    pagina.add(botao_iniciar)
    pagina.add(titulo)
#ft.app(main) rodar em formato de aplicativo, como tranformar isso em um aplicativo? tenho que fazer um processo de deploy e disponibilizar ele em um servidor
    #para aprofundar mais nas possibilidades pesquisar flet Python e estudar a documentaçao
ft.app(main, view=ft.WEB_BROWSER)


        

