import boto3

client = boto3.resource('dynamodb')

tabel_name = 'url_db'

table = client.Table(tabel_name)

def get_db_item(short_url):
    try:
        response = table.get_item(
            Key={
                'short_url': short_url
                }
        )
        return response['Item'].get('original_url')
    except Exception as e:
        return False