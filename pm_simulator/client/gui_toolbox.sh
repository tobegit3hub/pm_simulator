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
    --backtitle OpenMLDB \
    --clear \
    --cancel-label "Exit" \
    --menu "Please select:" $HEIGHT $WIDTH 0 \
    "1" "修改背景颜色为粉红色" \
    "2" "修改背景颜色为浅黄色" \
    "3" "标题调大一点" \
    "4" "标题大小调成20像素" \
    "5" "超链接颜色改为黄色" \
    "6" "Do not display footer" \
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
  esac

  read -n 1 -s -r -p "Press any key to continue"

done