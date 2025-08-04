import boto3

# This script updates an item in a DynamoDB table using Boto3

client = boto3.resource('dynamodb')

table_name = 'url_db'
table = client.Table(table_name)

def update_db_item(short_url, original_url):
    try:
        item = {
             'short_url': short_url,
            'original_url': original_url
        }
        response = table.put_item(
            Item=item
        )
      
        
        return True
    except Exception as e:
        return False

   