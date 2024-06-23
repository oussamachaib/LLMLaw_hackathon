"""
"""
import boto3, json

SYS_PROMPT = [{'text': "You are an legal contract expert. Respond to the following queries:"}]


class Message:
    def __init__(self, role, content):
        self.role = role
        self.content = content

    def json_msg(self):
        return {"role": self.role, "content": self.content}


def send_request(content: Message):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')

    message_list = [content.json_msg()]

    response = bedrock.converse(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        system=SYS_PROMPT,
        messages=message_list,
        inferenceConfig={
            "maxTokens": 100,
            "temperature": 0
        },
    )

    response_message = response['output']['message']
    msg = json.dumps(response_message, indent=4)
    return msg


if __name__ == "__main__":
    print(send_request(None))
