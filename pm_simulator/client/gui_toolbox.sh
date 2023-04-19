#!/bin/bash

cd "$(dirname "$0")"

# Contant variables
DIALOG_CANCEL=1
DIALOG_ESC=255
HEIGHT=0
WIDTH=0

while true; do
  exec 3>&1
  selection=$(dialog \
    --backtitle "GUI Toolbox" \
    --clear \
    --cancel-label "Exit" \
    --menu "Please select:" $HEIGHT $WIDTH 0 \
    "1" "修改背景颜色为粉红色" \
    "2" "修改背景颜色为浅黄色" \
    "3" "标题调大一点" \
    "4" "标题大小调成20像素" \
    "5" "超链接颜色改为黄色" \
    "6" "Do not display footer" \
    "7" "算了，还是原来的样式吧 / Undo and use last version" \
    "8" "语音输入(通过电脑麦克风输入，仅支持英文)" \
    "9" "重制CSS文件" \
    2>&1 1>&3)
  exit_status=$?
  exec 3>&-
  case $exit_status in
    $DIALOG_CANCEL)
      clear
      echo "Program terminated."
      exit
      ;;
    $DIALOG_ESC)
      clear
      echo "Program aborted." >&2
      exit 1
      ;;
  esac

  case $selection in
    0 )
      clear
      echo "Program terminated."
      exit 0
      ;;
    1 )
      ./client.py "修改背景颜色为粉红色"
      ;;
    2 )
      ./client.py "修改背景颜色为浅黄色"
      ;;
    3 )
      ./client.py "标题调大一点"
      ;;
    4 )
      ./client.py "标题大小调成20像素"
      ;;
    5 )
      ./client.py "超链接颜色改为黄色"
      ;;
    6 )
      ./client.py "Do not display footer"
      ;;
    7 )
      ./client.py "算了，还是原来的样式吧"
      ;;
    8 )
      ./voice_client.py
      ;;
    9 )
      ./reset_css_file.sh
      ;;
  esac

  read -n 1 -s -r -p "Press any key to continue"

done