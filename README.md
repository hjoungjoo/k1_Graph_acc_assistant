# k1_Graph_acc_assistant
이 프로젝트는 파이썬 없이 쉽게 상용자들이 밸트 탠셔닝절차를 실행하고 그 결과를 쉽게 볼수 있도록 만들었습니다.
This project aims to make it easy for users who have little knowledge of Python to run Belt tensioning procedure( Klipper's Graph_accelerometer ) on Windows and view the resulting recommendations.

# 🔌Usage
우선 gcode_macro.cfg 에 아래 메크로를 추가한뒤 실행합니다.
copy below macro somewhere into your gcode_macro.cfg and run that macro 

[gcode_macro BELT_TEST] 
description: Run resonance test to analyze belts 
gcode: 
  G28
  TURN_OFF_HEATERS 
  M107 
  TEST_RESONANCES AXIS=1,1 OUTPUT=raw_data NAME=b 
  TEST_RESONANCES AXIS=1,-1 OUTPUT=raw_data NAME=a

테스트가 완료되면 /tmp 디렉토리에 2개의 엑셀파일 결과물이 생성됩니다.(raw_data_axis=1.000,-1.000_a.csv,raw_data_axis=1.000,1.000_b.csv)
once the resonance test is finished for both axis 2 excel files will be generated in tmp diractory(raw_data_axis=1.000,-1.000_a.csv,raw_data_axis=1.000,1.000_b.csv)
SSH등을 이용하여 두 파일을 본 프로젝트의 실행파일이 있는 폴더로 복사 합니다.
access your K1/Max via SSH and locate the folder, drag&drop those 2 files into your PC in this program diractory.
그리고 실행합니다.
and run it.

이것은 단지 지침일 뿐입니다. 프린터가 좋은 상태로 잘 제작되지 않았다면 벨트를 수동으로 조정하는 것이 더 나을 수도 있습니다…
Don’t forget this is just guidance, if the printer isn’t well built with good tolernaces you might be better off tuning your belts manually…


# 📦Download
[Releases](https://github.com/theycallmek/Klipper-Input-Shaping-Assistant/releases)

EXE packaged by pyinstaller. Build cmd:
pyinstaller -w main.py --onefile --add-data="extras/*;extras" -n Klipper-graph-acc-Assistant
