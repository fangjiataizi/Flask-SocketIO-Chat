
import dashscope
dashscope.api_key="sk-4ef10939e882469292719d55e0a045b5"

from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
from dashscope import ImageSynthesis
from dashscope import Generation
from dashscope.api_entities.dashscope_response import Role




def call_with_prompt(prompt):
    response = dashscope.Generation.call(
        model=dashscope.Generation.Models.qwen_max,
        prompt=prompt,
    )
    # The response status_code is HTTPStatus.OK indicate success,
    # otherwise indicate request is failed, you can get error code
    # and message from code and message.
    if response.status_code == HTTPStatus.OK:
        print(response.output)  # The output text
        print(response.usage)  # The usage information
        return response.output.text
    else:
        print(response.code)  # The error code.
        print(response.message)  # The error message.
        return 'ERROR'




def simple_call(prompt):
    prompt = '{}生成的菜谱图片'.format(prompt)
    rsp = ImageSynthesis.call(model=ImageSynthesis.Models.wanx_v1,
                              prompt=prompt,
                              n=1,
                              size='480*320')
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
        # save file to current directory
        for result in rsp.output.results:
            file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
            print("file_name:{}".format(file_name))
            with open('static/{}'.format(file_name), 'wb+') as f:
                f.write(requests.get(result.url).content)
        return file_name
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))
        return 'ERROR'


if __name__ == '__main__':
    simple_call()