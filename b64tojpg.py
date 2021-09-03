# author:  ZhaoKun
# contact: 1161678627@qq.com
# datetime:2020-01-08 15:19
# software: PyCharm

import base64

def b642jpg(b64str, name):
    data=base64.b64decode(b64str)
    with open('{}'.format(name), 'wb') as f:
        f.write(data)
        print('打印完毕')

if __name__ == '__main__':
    b64str = '''
    iVBORw0KGgoAAAANSUhEUgAAABQAAAAdCAIAAAAl5NuSAAACy0lEQVQ4EZ1UTWgTQRSeJNtsNyXbxmZF3BWkgpocRC9NDyYn8RD04A9YKKRUiCAV8VAPimg9VEE8KaV6Cg1YgxRyEAoePGgvaS+tCLYg7Sk5yBooW9Nk003i7My83c2mFnVZeN977/vem3m7M54jR4+j/324DqHcGrtVHTn3SxF13kx6kc6rmz3zs8KzvIvsaessD9dy98sK33SxiOtXP/ePprk1O+e1oZzaWXisOpS8ruPXB4y6lPiRyxoy+Oai2CMbLyfKInMCK2/l5ImDJ0/h9/DwVLio00RTjG09T4HEEo893TpDtoiQUJjqvzzptZa3lBXij8Iqk1SHRmsxhmlnuX41VqURfbVvImvVBpAXZpYE5iiVm5coJGI5rUdZJlDIcSWQOG0m1wPNd6JJOlEivn66wnia8Mn9PaDCgn9DY1ga2CVjM8WNqLzLwiUuA+QO6/tW6mJBsXHeREQswZRVtfOnsYtsaJAVDbJNLE42QIu0n2QbNr8NzZX84NeVYQwxOdxi3wgJqvV9gPVHa9bZr1OHcI2DkdEUFkcMa9kd9P0D/9TZXQqL3YtxU2xfsUdLgm2ddSliM/dAwRYEfdo6hli87oUxNHmYO5Da7IWwAb5PW6biZUuMRDsNNIeNiiDWuBUzbi67q1hkFFE24LixiMM0ozI71vqmf85MmGJPoWQdt9rIoIPvhIP1YxL1uza+0P+UDCyTD8Bx2x5K73mBoSvpikK1evD9E4qIGOWFQpEiJCW0F3FnR4LjtTuJHYK86pLwiuWZxHN7NgQz3744vfU61bIuuliqujhdZm210Mwk0+D92lfvWLb8MEbLk8r46jStwfMN1knvnR8X7y4yDyFfb18/c1bxziOtswN1dmq5Bme+8GNooTcPgvc+WkoMHGLsfV3ozm/2KIeQFGryHJ2cX1ODKx8O3LjW/e67U4mxY9muzF+4vwHPdM7J2FS8qwAAAABJRU5ErkJggg==
    '''
    b642jpg(b64str, 'test')