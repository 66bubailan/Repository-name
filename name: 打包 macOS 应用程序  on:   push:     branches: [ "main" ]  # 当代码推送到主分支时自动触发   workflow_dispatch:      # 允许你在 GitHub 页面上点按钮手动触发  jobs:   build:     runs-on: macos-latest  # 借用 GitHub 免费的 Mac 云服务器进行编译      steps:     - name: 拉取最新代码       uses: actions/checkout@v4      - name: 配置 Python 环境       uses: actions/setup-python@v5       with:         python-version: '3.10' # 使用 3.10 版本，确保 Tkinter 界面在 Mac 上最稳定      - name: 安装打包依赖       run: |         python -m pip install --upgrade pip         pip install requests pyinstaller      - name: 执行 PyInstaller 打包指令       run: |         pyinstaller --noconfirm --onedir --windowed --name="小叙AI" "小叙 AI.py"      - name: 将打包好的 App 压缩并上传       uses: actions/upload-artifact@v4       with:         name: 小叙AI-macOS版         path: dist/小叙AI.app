name: 打包 macOS 应用程序

on:
  push:
    branches: [ "main" ]  # 当代码推送到主分支时自动触发
  workflow_dispatch:      # 允许你在 GitHub 页面上点按钮手动触发

jobs:
  build:
    runs-on: macos-latest  # 借用 GitHub 免费的 Mac 云服务器进行编译

    steps:
    - name: 拉取最新代码
      uses: actions/checkout@v4

    - name: 配置 Python 环境
      uses: actions/setup-python@v5
      with:
        python-version: '3.10' # 使用 3.10 版本，确保 Tkinter 界面在 Mac 上最稳定

    - name: 安装打包依赖
      run: |
        python -m pip install --upgrade pip
        pip install requests pyinstaller

    - name: 执行 PyInstaller 打包指令
      run: |
        pyinstaller --noconfirm --onedir --windowed --name="小叙AI" "小叙 AI.py"

    - name: 将打包好的 App 压缩并上传
      uses: actions/upload-artifact@v4
      with:
        name: 小叙AI-macOS版
        path: dist/小叙AI.app
