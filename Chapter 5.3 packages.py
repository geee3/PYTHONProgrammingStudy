# by GEEE3, February 4, 2021

'''
패키지(Packages)는 도트(.)를 사용하여 파이썬 모듈을 계층적으로 관리할 수 있게 해준다
예를 들어 모듈 이름이 A.B인 경우에 A는 패키지 이름이 되고 B는 A 패키지의 B 모듈이 된다
파이썬 패키지는 디렉터리와 파이썬 모듈로 이루어지며 구조는 다음과 같다

game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py

__init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다
패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다
'''