"""
AWS_ACCESS_KEY_ID=ASIAXSB255HBAITN3KZO;AWS_DEFAULT_REGION=us-west-2;AWS_SECRET_ACCESS_KEY=F/B87mUx/SHyCmn+rElAXhNkFsHLZrUTmFwhwdiN;AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEOP//////////wEaCXVzLWVhc3QtMSJHMEUCIQDdAddtDeXq63edIxqLwyOvs8OECKrXIZhZrsOO6tQT8AIgcp6FSUGC/c0VHiZ1goq9bwH8SJQkF2y8Ua/oJyjb284qogIIjP//////////ARACGgw1MTk4MTQ2MzgwMTgiDJser6fWlbIdfW3J2ir2AXAB8p8mPkopqLDxDYXFJ1G59Qndogox+WOFXOuddCONpFF3NRyMd0SxF1Q8XLWAJVzZ9Olonbu7E7Z9r5ZuElmg1ffY2y5rV1R4+f8Varee1YopfTWYaZ9Y/ez6PTOqqqtxKNsVQdlKoLw/oRRk+EXc08pUXVZBJWlmoskev36yGeOCCsPNzD/iealRlZUQD8o0RuEms3WNsWxcZRBQRpaKExQ1Slp8hU7PPepkTBF/yCvgv3i+do46XyJ9NKLFYq+BV9URaVAGhOrrIj9RD2Fh+to5SvzVz9YZpVbCoC4BphSlonjUf4uSTrVWZySsMUuzZoZ2tDCk79+zBjqdAZhhOsxPmJPq/qVBxMziiaROzKF7XTbvJK2ToXf0NuH7GtdvW3MxkWl8nFnRWclP0cLMj0B7NTNP+oToGNsn4u8E2EafLIJXHLpXGMAZtV12bL9528pj5/F3olAJZOUF5Nc78pQfOAJIG1GFiFvVbxgfsTmY3hqBfRiCc0VdTNKKDiUCQ8AuMz1rZZUBydibkTx8OPuniHhBSP1AcwE=;PYTHONUNBUFFERED=1
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
