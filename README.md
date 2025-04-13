先下载autokey，还有gnome-tweaks工具
在gnome-wteaks中把capsLock映射成hyper
然后把py文件复制到sample scripts文件夹中
然后去做映射，在下面hotkey那里点设置（set），先设置按键然后点hyper
要把super建的快捷键都关了，不然就会运行快捷键了，比如 super+d，+p,+l等
我建议使用sudo apt install dconf-editor这个工具
然后将行了
里面不一定和windows上caps++的按键一样，自己做自定义很简单的
下面是目前的按键映射
cap + e -> up 光标上移
    + d -> down 光标下移
    + s -> left 光标左移
    + f -> right 光标右移
    + w -> backspace 光标左边删除一个
    + r -> delete 光标右边删除一个
    + a -> 左移一个单词
    + g -> 右移一个单词
    + c -> ctrl+shift+c 终端上的复制
    + v -> ctrl+shift+v 终端上的粘贴
    + q -> 单击ctrl,因为我输入法设置的ctrl切换中英文
    + t -> page_up 向上翻页
    + b -> page_down 向下翻页
    + i -> 向上选中
    + k -> 向下选中
    + j -> 向左选中
    + l -> 向右选中
    + z -> esc 发送esc键
    + , -> 选中当前单词
    + m -> 向左选中单词
    + . -> 向右选中单词