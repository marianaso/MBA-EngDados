import boto3

def insert_into_S3():
    
    s3_client = boto3.client('s3')

    bucket_name = 'igti-bootcamp-ed-2021-494654695792'

    # Carrega o arquivo CSV no bucket S3
    s3_client.upload_file('./dados/dadosMongoDB.csv', bucket_name, 'dadosMongoDB.csv')
    s3_client.upload_file('./dados/dadosIBGE.csv', bucket_name, 'dadosIBGE.csv')