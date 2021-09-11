# qutils
量化交易常用 utils 
```
├── email_utils.py # 收发邮件
├── __init__.py
├── logger.py # 日志， 包括机器人、本地、终端多种输出
├── README.md 
├── redis_utils.py # 常用redis 操作
├── utils.py  # 字符串、时间、文件等操作
└── wecom_bot_utils.py  # 机器人
```

# 使用：
clone 到目录 <br>
```
vim ~/.bashrc
export PYTHONPATH=$PYTHONPATH:/you/qutils/root/path
```

可以通过 
```
ipython
import sys
print(sys.path)
``` 
查看是否导入系统环境了 

vscode 还需要设置
```
vim .vscode/setting.json

{
    "python.analysis.extraPaths": [
        "ConvertBondWheel",
        "/root/workSpace/investProject",
    ]
}
```