### 查看/更改git代理

查看git代理
```bash
git config --global --get http.proxy
git config --global --get https.proxy
```

更改git代理
```bash
git config --global http.proxy http://localhost:端口号
git config --global https.proxy http://localhost:端口号
```

移除git代理
```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

### 代码提交

将文件添加到暂存区
```bash
git add .
```

添加提交消息
```bash
git commit -m "提交消息"
```

提交代码
```bash
git push origin <分支名>
```

使用密钥提交
```bash
git -u push origin <分支名>
# 登陆时密码填写密钥即可
# 8HwqgT3yQn6vnf71G8Zv
```

强制提交（不建议使用）
```bash
git push -f origin <分支名>
```

### 拉取代码

拉取整个仓库
```bash
git clone <仓库URL>
```

拉取指定目录
```bash
git clone <仓库URL> <目标目录路径>
```


### 分支

查看所有分支
```bash
git branch
```

创建分支
```bash
git branch <分支名>
```

切换分支
```bash
git checkout <分支名>
```
