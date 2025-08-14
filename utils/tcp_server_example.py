import socket

# -------------------------------
# 設定伺服器的 IP 和 Port
# -------------------------------
# "0.0.0.0" 表示接收所有網卡（即所有外部或本地來源的連線）
host = "0.0.0.0"
port = 8888

# -------------------------------
# 建立 TCP socket
# -------------------------------
# AF_INET 表示使用 IPv4
# SOCK_STREAM 表示使用 TCP 協定
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -------------------------------
# 綁定 IP 和 Port，並開始監聽
# -------------------------------
server_socket.bind((host, port))
server_socket.listen(5)  # 最多允許 5 個等待中的 client

print(f"[Server] Listening on {host}:{port} ...")

# -------------------------------
# 主迴圈：接受並處理每一個 client 連線
# -------------------------------
while True:
    # 等待 client 連進來，一旦有連線就回傳 client 的 socket 和位址
    client_socket, addr = server_socket.accept()
    print(f"[Server] Connection from {addr}")

    try:
        # 接收 client 傳來的資料（最多 1024 bytes）
        data = client_socket.recv(1024)
        print(f"[Server] Received: {data.decode()}")

        # 回覆 client 一個確認訊息
        client_socket.sendall(b"Received your message")

    except Exception as e:
        print(f"[Server] Error: {e}")

    finally:
        # 關閉與該 client 的連線（不影響主 socket）
        client_socket.close()
        print(f"[Server] Closed connection with {addr}")
