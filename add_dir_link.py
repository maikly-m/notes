"""
根据标题生成markdown 目录
"""
import re
import sys

append_lines = []
mend_lines = []


def add_link(file_name):
    with open(file=file_name, mode="r", encoding="utf-8") as f:
        s1 = r"`目录：`" + "\r\n"
        append_lines.append(s1)
        for line in f.readlines():
            # 匹配md的标题
            if re.search("^# ", line):
                s = r'# <span id="md_' + line[2:-1] + '"/>' + line[2:-1] + "\n"
                s1 = '- [' + line[2:-1] + '](' + '#md_' + line[2:-1] + ')' + "\n"
                append_lines.append(s1)
                mend_lines.append(s)
            elif re.search("^#{2} ", line):
                s = r'## <span id="md_' + line[3:-1] + '"/>' + line[3:-1] + "\n"
                s1 = '  - [' + line[3:-1] + '](' + '#md_' + line[3:-1] + ')' + "\n"
                append_lines.append(s1)
                mend_lines.append(s)
            elif re.search("^#{3} ", line):
                s = r'### <span id="md_' + line[4:-1] + '"/>' + line[4:-1] + "\n"
                s1 = '    - [' + line[4:-1] + '](' + '#md_' + line[4:-1] + ')' + "\n"
                append_lines.append(s1)
                mend_lines.append(s)
            elif re.search("^#{4} ", line):
                s = r'#### <span id="md_' + line[5:-1] + '"/>' + line[5:-1] + "\n"
                s1 = '      - [' + line[5:-1] + '](' + '#md_' + line[5:-1] + ')' + "\n"
                append_lines.append(s1)
                mend_lines.append(s)
            elif re.search("^#{5} ", line):
                s = r'##### <span id="md_' + line[6:-1] + '"/>' + line[6:-1] + "\n"
                s1 = '        - [' + line[6:-1] + '](' + '#md_' + line[6:-1] + ')' + "\n"
                append_lines.append(s1)
                mend_lines.append(s)
            else:
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
