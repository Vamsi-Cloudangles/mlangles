import boto3
def load_data():
    s3 = boto3.client(
    's3',
    aws_access_key_id='AKIA3YG72WSKAY3DQARO',
    aws_secret_access_key='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',
    region_name='us-east-1')
    obj = s3.get_object(Bucket='mlops-storage1', Key='Vamsi/dimond.csv')
    dataset = obj['Body'].read().decode('utf-8').splitlines() 
    return dataset
