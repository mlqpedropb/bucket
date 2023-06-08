import os 
import boto3

class GerenciarS3:
    def __init__(self, nome_bucket):
        self.nome_bucket = nome_bucket
        self.s3 = boto3.client('s3')
        
    def lista_arquivos(self):
        try:
            respostas = self.s3.list_objects_v2(Bucket=self.nome_bucket)
            
            if 'Contents' in respostas:
                files = [obj['Key'] for obj in respostas['Contents']]
                print("Arquivos no S3: ")
                for file in files:
                    print(file)
            else:
                print("nenhum arquivo encontrado no S3")
        except Exception as e:
            print(f"erro ao listar os arquivos do S3: {e}")
            
    def delete_arquivo(self, nome_arquivo):
        try:
            self.s3.delete_object(Bucket=self.nome_bucket, Key=nome_arquivo)
            print(f"Arquivo {nome_arquivo} excluído do S3 com sucesso.")
        except Exception as e:
            print(f'Erro ao excluir o arquivo do S3: {e}')
            
    def upload_arquivo(self, caminho_arquivo, nome_arquivo=None):
        if nome_arquivo is None:
            nome_arquivo= caminho_arquivo
        try:
            self.s3.upload_file(caminho_arquivo, self.nome_bucket, nome_arquivo)
            print(f"Arquivo {nome_arquivo} enviado para S3 com sucesso.")
        except Exception as e:
            print(f"Erro ao enviar o arquivo para o S3: {e}")
        
    def download_arquivo(self, nome_arquivo, caminho_arquivo):
        try:
            caminho_completo= os.path.join(caminho_arquivo, nome_arquivo)
            self.s3.download_file(self.nome_bucket, nome_arquivo, caminho_completo)
            print(f"Arquivo {nome_arquivo} baixado do S3 com sucesso")
        except Exception as e:
            print(f"Erro ao baixar o arquivo do S3: {e}") 