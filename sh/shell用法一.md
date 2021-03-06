## Shell用法：

**Shell 文件比较符：**        
-e 判断对象是否存在     
-d 判断对象是否存在，并且为目录   
-f 判断对象是否存在，并且为常规文件     
-L 判断对象是否存在，并且为符号链接     
-h 判断对象是否存在，并且为软链接  
-s 判断对象是否存在，并且长度不为0     
-r 判断对象是否存在，并且可读        
-w 判断对象是否存在，并且可写        
-x 判断对象是否存在，并且可执行       
-O 判断对象是否存在，并且属于当前用户        
-G 判断对象是否存在，并且属于当前用户组       
-nt 判断file1是否比file2新  `[ "/data/file1" -nt "/data/file2" ]`       
-ot 判断file1是否比file2旧  `[ "/data/file1" -ot "/data/file2" ]`     
-n 来判定字符串非空

man用法：
usage: man [-adfhktwW] [section] [-M path] [-P pager] [-S list]
	[-m system] [-p string] name ...
help用法：
command —help

**分解这个组合：“>/dev/null 2>&1” :**      
即 标准输出和标准错误输出两部分        
1：> 代表重定向到哪里，例如：echo "123" > /home/123.txt      
2：/dev/null 代表空设备文件     
3：2> 表示stderr标准错误       
4：& 表示等同于的意思，2>&1，表示2的输出重定向等同于1     
5：1 表示stdout标准输出，系统默认值是1，所以">/dev/null"等同于 "1>/dev/null"
因此，>/dev/null 2>&1
也可以写成“1> /dev/null 2> &1”       
**那么本文标题的语句执行过程为：**     
1>/dev/null ：首先表示标准输出重定向到空设备文件，也就是不输出任何信息到终端，说白了就是不显示任何信息。      
2>&1 ：接着，标准错误输出重定向 到 标准输出，因为之前标准输出已经重定向到了空设备文件，所以标准错误输出也重定向到空设备文件。      
``  倒引号。命令替换。在倒引号内部的shell命令首先被执行，其结果输出代替用倒引号括起来的文本，不过特殊字符会被shell解释。

字符串表达式
-------------------------
'expr'支持模式匹配和字符串操作。字符串表达式的优先级高于数值表达式和逻辑关系表达式。
 
'STRING : REGEX'
     执行模式匹配。两端参数会转换为字符格式，且第二个参数被视为正则表达式(GUN基本正则)，它默认会隐含前缀"^"。随后将第一个参数和正则模式做匹配。
 
     如果匹配成功，且REGEX使用了'\('和'\)'，则此表达式返回匹配到的。
     如果匹配失败，如果REGEX中使用了'\('和'\)'，则此表达式返回空字符串，否则返回为0。
     只有第一个'\(...\)'会引用返回的值；其余的'\(...\)'只在正则表达式分组时有意义。
     在正则表达式中，'\+'，'\?'和'\|'分表代表匹配一个或多个，0个或1个以及两端任选其一的意思。
 
'match STRING REGEX'
     等价于'STRING : REGEX'。
 
'substr STRING POSITION LENGTH'
     返回STRING字符串中从POSITION开始，长度最大为LENGTH的子串。如果POSITION或LENGTH为负数，0或非数值，则返回空字符串。
 
'index STRING CHARSET'
     CHARSET中任意单个字符在STRING中最前面的字符位置。如果在STRING中完全不存在CHARSET中的字符，则返回0。见后文示例。
    
'length STRING'
     返回STRING的字符长度。
 
'+ TOKEN'

 `将TOKEN解析为普通字符串，即使TOKEN是像MATCH或操作符"/"一样的关键字。这使得'expr length + "$x"'或'expr + "$x" : '.*/\(.\)''可以正常被测试，即使"$x"的值可能是'/'或'index'关键字。这个操作符是一个GUN扩展。
 通用可移植版的应该使用'" $token" : ' \(.*\)''来代替'+ "$token"'。`
 
   要让expr将关键字解析为普通的字符，必须使用引号包围。
 
算术表达式
--------------------------
 
'expr'支持普通的算术操作，算术表达式优先级低于字符串表达式，高于逻辑关系表达式。
 
'+ -'
     加减运算。两端参数会转换为整数，如果转换失败则报错。
 
'* / %'
     乘，除，取模运算。两端参数会转换为整数，如果转换失败则报错。
 
逻辑关系表达式
---------------------------
 
'expr'支持普通的逻辑连接和逻辑关系。它的优先级最低。
 
'|'
     如果第一个参数非空且非0，则返回第一个参数的值，否则返回第二个参数的值，但要求第二个参数的值也是非空或非0，否则返回0。如果第一个参数是非空或非0时，不会计算第二个参数。
    
     经过测试，以上手册内容是错误的。正确的应该是：如果第一个参数非0，则返回第一个参数的值，否则返回第二个参数。但如果任意一个参数为空，则报错。除非空字符串使用引号包围，此时将和0的处理方式一样。
 
'&'
     如果两个参数都非空且非0，则返回第一个参数，否则返回0。如果第一个参为0或为空，则不会计算第二个参数。
    
     经过测试，以上手册内容是错误的。正确的应该是：如果两个参数都非0，则返回第一个参数，否则返回0。但任意一个参数为空，则报错。除非空字符串使用引号包围，此时将和0的处理方式一样。
 
'< <= = == != >= >'
     比较两端的参数，如果为true，则返回1，否则返回0。"=="是"="的同义词。"expr"首先尝试将两端参数转换为整数，并做算术比较，如果转换失败，则按字符集排序规则做字符比较。
 
括号'()'可以改变优先级，但使用时需要使用反斜线对括号进行转义。
 
'expr'使用示例 —————————
以下为expr的一些示例，其中有将shell的元字符使用引号包围的示例。        
```

   将shell中变量'foo'的值增加1：
      foo=$(expr $foo + 1)
    输出变量路径变量'$fname'中不包含'/'的文件名部分：
      expr $fname : '.*/\(.*\)' '|' $fname
         解释：其中的'|'是expr中的连接符，只不过是被引号包围防止被shell解析。例如$fname=/etc/hosts，则此表达式返回hosts，如果$fname=/usr/share/，则此表达式'|'的左边为空，所以返回'|'右边的值，即$fname，即返回/usr/share/。
    An example showing that '\+' is an operator:
      expr aaa : 'a\+'    # 解释：因为REGEX部分没有使用\(\)，所以返回匹配的字符数
     => 3
      expr abc : 'a\(.\)c'  # 解释：因为REGEX部分使用了\(\)，所以返回匹配的字符
     => b
     expr index abcdef cz
     => 3
     expr index index a    # 解释：因为第二个index是关键字
     error-> expr: syntax error
     expr index + index a  # 解释：使用+将index关键字解析为普通字符串
     => 0
```

常用命令：
set 赋值；

