#!/bin/bash

# 发生错误时立即退出
set -e

# 获取脚本所在目录的绝对路径，确保在任何地方执行该脚本都能准确定位到项目根目录
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

echo "=========================================="
echo "🚀 开始部署 Cutton Cat 后端服务..."
echo "=========================================="

# 1. 拉取最新代码（如果你在服务器上执行，可以取消下面两行的注释）
# echo "📦 正在拉取最新代码..."
# git pull origin main

# 2. 检查并创建完整的虚拟环境（保证可重入性：如果没有 activate 脚本，说明没建好或损坏）
if [ ! -f "venv/bin/activate" ]; then
    echo "🐍 未找到完整的虚拟环境，正在清理并重新创建 venv..."
    rm -rf venv
    python3 -m venv venv
fi

# 3. 激活虚拟环境
echo "🔌 激活虚拟环境..."
# 在 bash 脚本中，直接 source 可能因为路径或非交互式 shell 环境出问题
# 推荐使用点号(.)来执行
. venv/bin/activate

# 4. 安装/更新依赖
echo "📦 安装项目依赖..."
pip install -r requirements.txt

# 5. 停止旧的服务进程（保证可重入性：先杀掉旧进程，再起新进程）
PORT=8000
echo "🛑 尝试停止端口 $PORT 上的旧服务进程..."

# 查找并杀掉正在运行的 runserver 进程
# pgrep 寻找进程，pkill 杀掉进程
if pgrep -f "python manage.py runserver 0.0.0.0:$PORT" > /dev/null; then
    echo "发现正在运行的服务，正在停止..."
    pkill -f "python manage.py runserver 0.0.0.0:$PORT"
    sleep 2  # 等待进程彻底释放端口
else
    echo "没有发现运行中的旧服务。"
fi

# 6. 在后台启动新服务，并将输出重定向到日志文件
# nohup (no hang up) 保证终端退出后程序继续运行，& 表示放入后台
LOG_FILE="app.log"
echo "🌟 在后台启动新服务，端口: $PORT ..."
nohup python manage.py runserver 0.0.0.0:$PORT > "$LOG_FILE" 2>&1 &

# 7. 检查启动结果
sleep 2
if pgrep -f "python manage.py runserver 0.0.0.0:$PORT" > /dev/null; then
    echo "✅ 部署成功！"
    echo "📝 服务正在后台运行，日志已输出到 $PROJECT_DIR/$LOG_FILE"
    echo "💡 你可以使用命令查看实时日志: tail -f $LOG_FILE"
else
    echo "❌ 启动失败，请检查日志 $LOG_FILE 排查问题。"
    exit 1
fi

echo "=========================================="
