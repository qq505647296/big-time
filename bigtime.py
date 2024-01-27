import tkinter as tk
import datetime

def update_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)  # 更新时间，每隔1秒

# 创建窗口
window = tk.Tk()
window.title("系统时间")
window.geometry("200x50")

# 创建用于显示时间的标签
time_label = tk.Label(window, font=("Helvetica", 20))
time_label.pack()

# 启动更新时间的函数
update_time()

# 运行窗口的主循环
window.mainloop()
