"""
根据标题生成markdown 目录
"""
import re
import sys
import logging
import hashlib

append_lines = []
mend_lines = []


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)
md = hashlib.md5()


def add_link(file_name):
    with open(file=file_name, mode="r", encoding="utf-8") as f:
        s1 = r"`目录：`" + "\r\n"
        append_lines.append(s1)
        is_dir_content = True
        for l in f.readlines():
            # 匹配md的标题
            # 先移除之前有的标签
            r = re.search("<span id=.*/>", l)
            line = l
            if r is not None:
                span = r.span()
                line = l[:span[0]] + l[span[1]:-1]
            if re.search("^# ", line):
                # md5一下
                md.update(line[2:].encode("utf-8"))
                _id = md.hexdigest()
                s = r'# <span id="' + _id + '"/>' + line[2:] + "\n"
                s1 = '- [' + line[2:] + '](#' + _id + ')' + "\n"
                append_lines.append(s1)
                mend_lines.append(s)
                is_dir_content = False
            elif re.search("^#{2} ", line):
                # md5一下
                md.update(line[3:].encode("utf-8"))
                _id = md.hexdigest()
                s = r'## <span id="' + _id + '"/>' + line[3:] + "\n"
                s1 = '  - [' + line[3:] + '](#' + _id + ')' + "\n"
                append_lines.append(s1)
                mend_lines.append(s)
                is_dir_content = False
            elif re.search("^#{3} ", line):
                # md5一下
                md.update(line[4:].encode("utf-8"))
                _id = md.hexdigest()
                s = r'### <span id="' + _id + '"/>' + line[4:] + "\n"
                s1 = '    - [' + line[4:] + '](#' + _id + ')' + "\n"
                append_lines.append(s1)
                mend_lines.append(s)
                is_dir_content = False
            elif re.search("^#{4} ", line):
                # md5一下
                md.update(line[5:].encode("utf-8"))
                _id = md.hexdigest()
                s = r'#### <span id="' + _id + '"/>' + line[5:] + "\n"
                s1 = '      - [' + line[5:] + '](#' + _id + ')' + "\n"
                append_lines.append(s1)
                mend_lines.append(s)
                is_dir_content = False
            elif re.search("^#{5} ", line):
                # md5一下
                md.update(line[6:].encode("utf-8"))
                _id = md.hexdigest()
                s = r'##### <span id="' + _id + '"/>' + line[6:] + "\n"
                s1 = '        - [' + line[6:] + '](#' + _id + ')' + "\n"
                append_lines.append(s1)
                mend_lines.append(s)
                is_dir_content = False
            else:
                # 之前的目录不需要了
                if not is_dir_content:
                    mend_lines.append(line)
        append_lines.append("\r" + "---" + "\r\n")

    with open(file=file_name, mode="w+", encoding="utf-8") as fw:
        for l in append_lines:
            fw.write(l)
        for l in mend_lines:
            fw.write(l)

    pass


if __name__ == '__main__':
    argv_ = sys.argv[1]  # 获取当前文件夹下的文件
    add_link(argv_)
