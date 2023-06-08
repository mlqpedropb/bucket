from classe.GerenciarS3 import GerenciarS3

class MenuGerenciadorS3:
    def __init__(self, nome_bucket):
        self.gerenciardor = GerenciarS3(nome_bucket)
        
        def exibir_menu(self):
            print("--- MENU ---")
            print("1. Lista arquivos")
            print("2. Enviar arquivo")
            print("3. Baixar arquivo")
            print("4. Excluir arquivo")
            print("0. Sair")
            
        def listar_arquivos(self):
            self.gerenciador.lista_arquivos()
            
        def enviar_arquivo(self):
            caminho_arquivo = input(' digite o caminho do arquivo: ')
            nome_arquivo = input (' digite o nome do arquivo(opcional): ')
            self.gerenciador.upload_arquivo(caminho_arquivo, nome_arquivo)
            
        def baixar_arquivo(self):
            nome_arquivo = input (' digite o nome do arquivo: ')
            caminho_arquivo = input( ' digite o caminho para salavr o arquivo: ')
            self.gerenciador.download_arquivo(nome_arquivo, caminho_arquivo)
            
        def excluir_arquivo(self):
            nome_arquivo = input(' digite o nome do arquivo que deseja excluir: ')
            self.gerenciador.delete_arquivo(nome_arquivo)
            
        
        def executar(self):
            while True:
                self.exibir_menu()
                opcao = input(' digite a opção desejada: ')
                if opcao =='1':
                    self.listar_arquivos()
                elif opcao == '2':
                    self.enviar_arquivo()
                elif opcao == '3':
                    self.baixar_arquivo()
                elif opcao == '4': 
                    self.excluir_arquivo()
                elif opcao == '0':
                    print(' encerrando o programa. ')
                    break
                else:
                    print('opção invalida. Digite novamente.')
                
            