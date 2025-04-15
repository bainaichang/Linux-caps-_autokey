# Enter script code
import time

# 获取当前行内容并复制到下一行
def duplicate_line():
    # 保存当前剪贴板内容
    clipboard_store = clipboard.get_clipboard()
    
    # 移动到行首
    keyboard.send_keys("<home>")
    # 选择整行
    keyboard.send_keys("<shift>+<end>")
    # 复制行
    keyboard.send_keys("<ctrl>+c")
    # 等待一小段时间确保复制完成
    time.sleep(0.05)
    # 移动到行尾
    keyboard.send_keys("<end>")
    # 插入新行
    keyboard.send_keys("<up>")
    time.sleep(0.05)
    keyboard.send_keys("<end>")
    keyboard.send_keys("<enter>")
    time.sleep(0.05)
    # 粘贴
    keyboard.send_keys("<ctrl>+v")
    
    # 恢复剪贴板内容
    time.sleep(0.05)
    clipboard.fill_clipboard(clipboard_store)

# 调用函数
duplicate_line()
