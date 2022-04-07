
get_tags_response = s3_client.get_object_tagging(
    Bucket='your-bucket-name',
    Key='folder-if-any/file-name.extension',
)

put_tags_response = s3_client.put_object_tagging(
    Bucket='your-bucket-name',
    Key='folder-if-any/file-name.extension',    
    Tagging={
        'TagSet': [
            {
                'Key': 'tag-key',
                'Value': 'tag-value'
            },
        ]
    }
)