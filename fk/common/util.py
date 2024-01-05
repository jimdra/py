import base64
import random
import string
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from io import BytesIO

from flask import make_response


class Captcha:
    '''生成验证码类'''

    def rnd_color(self):
        '''随机颜色'''
        return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

    def gene_text(self, num):
        '''生成num位验证码'''
        return ''.join(random.sample(string.ascii_letters + string.digits, num))

    def draw_lines(self, draw, num, width, height):
        '''划线'''
        for num in range(num):
            x1 = random.randint(0, width // 2)
            y1 = random.randint(0, height // 2)
            x2 = random.randint(0, width)
            y2 = random.randint(height // 2, height)
            draw.line(((x1, y1), (x2, y2)), fill='black', width=1)

    def get_verify_code(self, num=4, is_base64=False):
        '''生成验证码图形'''
        code = self.gene_text(num)
        # 图片大小120×50
        width, height = 100, 40
        # 新图片对象
        im = Image.new('RGB', (width, height), 'white')
        # 字体
        font = ImageFont.truetype('./static/arial.ttf', 35)
        # draw对象
        draw = ImageDraw.Draw(im)
        # 绘制字符串
        for item in range(num):
            draw.text((5 + random.randint(-3, 3) + 23 * item, 5 + random.randint(-3, 3)),
                      text=code[item], fill=self.rnd_color(), font=font)
        # 划线
        self.draw_lines(draw, 2, width, height)
        # 高斯模糊
        im = im.filter(ImageFilter.GaussianBlur(radius=1))
        # im.show()
        # 图片以二进制形式写入
        buf = BytesIO()
        im.save(buf, 'jpeg')
        buf_str = buf.getvalue()
        if is_base64:
            image = base64.b64encode(buf_str).decode('utf-8')
            image = "data:image/png;base64," + image
        else:
            # 把buf_str作为response返回前端，并设置首部字段
            image = make_response(buf_str)
            image.headers['Content-Type'] = 'image/gif'

        return image, code
